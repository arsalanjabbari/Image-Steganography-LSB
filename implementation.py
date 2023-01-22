import cv2
import numpy as np


def makePicture(pic):
    img1 = []
    img2 = []
    row = pic[-1][0] + 1
    col = pic[-1][1] + 1
    for i in range(row):
        for j in range(col):
            index = i * col + j
            img1 += [[np.uint8(pic[index][4]), np.uint8(pic[index][3]), np.uint8(pic[index][2])]]
        img2 += [img1]
        img1 = []
    return np.array(img2)


def getTextFromFile(filename):
    file = open(filename, 'r')
    return file.read()


def getPicture(filename):
    img = cv2.imread(filename)
    lis = img.shape
    piclist = []
    row = lis[0]
    col = lis[1]
    for i in range(row):
        for j in range(col):
            pix_b = img[i][j][0]
            pix_g = img[i][j][1]
            pix_r = img[i][j][2]
            piclist += [[i, j, pix_r, pix_g, pix_b]]
    return piclist


def putDataInPixel(index, sixBinary, pixels):
    pixels[index][2] &= 252
    pixels[index][3] &= 252
    pixels[index][4] &= 252
    pixels[index][2] |= int(sixBinary[0:2], 2)
    pixels[index][3] |= int(sixBinary[2:4], 2)
    pixels[index][4] |= int(sixBinary[4:6], 2)


def exportDataFromPixel(index, pixels):
    temp = ""
    temp += str(pixels[index][2])
    temp += str(pixels[index][3])
    temp += str(pixels[index][4])
    return temp


def stg(message,pixels):
    messageLength = len(message)
    messageLengthBin = bin(messageLength)[2:]
    messageLengthBin = (24 - len(messageLengthBin)) * "0" + messageLengthBin
    pixelIndex = 0
    for i in range(0, 24, 6):
        putDataInPixel(pixelIndex, messageLengthBin[i: i + 6],pixels)
        pixelIndex += 1
    messageInBin = ""
    for char in message:
        binaryStr = bin(ord(char))[2:]
        binaryStr = (8 - len(binaryStr)) * "0" + binaryStr
        messageInBin += binaryStr
        messageInBin += (6 - (len(messageInBin) % 6)) * "0"
    for i in range(0, len(messageInBin), 6):
        putDataInPixel(pixelIndex, messageInBin[i: i + 6], pixels)
        pixelIndex += 1

def decrypt(pixels):
    msgLenInBinary = ""
    secretMsgInBinary = ""
    pixelIndex = 0
    for index in range(0,24,6):
        msgLenInBinary += exportDataFromPixel(index, pixels)
        pixelIndex += 1
    msgLen = int(msgLenInBinary)
    numCheckingBits = msgLen*8
    for i in range(pixelIndex,numCheckingBits,2):
        secretMsgInBinary += exportDataFromPixel(i, pixels)
    secretMsg = ""
    for j in range(0,numCheckingBits,8):
        secretMsg += chr(int(secretMsgInBinary[j:j+8]))
    return secretMsg


def main():
    print("Welcome!")
    print("1. Encrypt a message in an image.")
    print("2. Store an image in cloud.")
    print("3. Quit")
    while True:
        task_number = int(input("Enter number of your wanted task: "))
        if task_number == 1:
            pixels = []
            pictureName = input("Enter the picture's file name, which you're gonna use: ")
            messageText = input("Enter the text file name, which you're gonna encrypt: ")
            messageText = getTextFromFile(messageText)
            pixels += getPicture(pictureName)
            stg(messageText, pixels)
            encryptedPicture = makePicture(pixels)
            dbWrite = 'encrypted_' + pictureName
            itsPassword = input("Enter a password for your encrypted text: ")
            newP = open("passwords.txt","a")
            newP.write(itsPassword)
            newP.write("\n")
            newP.close()
            cv2.imwrite(dbWrite, encryptedPicture)
        elif task_number == 2:
            pixels = []
            pictureName = input("Enter the picture's file name, which you're gonna use: ")
            upcoming = input("Press an <Enter> to save your image.")
            if upcoming == "":
                print("\nLoading ...")
                print("Done!")
            else:
                password = upcoming
                checkP = open("passwords.txt","r")
                lines = checkP.readlines()
                for i in lines:
                    i = i[:-1]
                    if password == i:
                        pixels += getPicture(pictureName)
                        theSecretMsg = decrypt(pixels)
                        includingFile = open(pictureName + "_export.txt", "x")
                        includingFile.write(theSecretMsg)
                        includingFile.close()

        elif task_number == 3:
            quit()
        else:
            print("Invalid task.")


if __name__ == "__main__":
    main()