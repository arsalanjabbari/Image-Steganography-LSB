# Image-Steganography-LSB

Image-Steganography-LSB is a command-line application that enables users to perform steganography using the Least Significant Bit (LSB) algorithm on images. This technique allows you to hide sensitive information within image files in a way that is not detectable by the human eye.

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Conclusion](#conclusion)

## Introduction

Welcome to the Image-Steganography-LSB repository! This project aims to provide an intuitive and user-friendly tool for hiding information within image files using the LSB algorithm. Steganography is an art of covert communication, and LSB steganography involves replacing the least significant bit of pixel values with hidden data, making it imperceptible to casual observers.

## Project Overview

The Image-Steganography-LSB application allows you to embed text-based data (such as messages or secret codes) into image files without visibly altering the image. The LSB algorithm is employed to achieve this, as it operates on the principle that changing the least significant bit of a pixel value has minimal impact on the image's visual appearance.

## Features

- **Text Embedding**: Seamlessly embed textual data into image files.
- **Image Extraction**: Extract hidden text from steganographically modified images.
- **User-Friendly TUI**: Enjoy a simple and interactive text-based user interface (TUI) for ease of use.
- **Compatible Image Formats**: Support for common image formats like PNG, JPEG, and BMP.
- **Customizable LSB Depth**: Adjust the number of least significant bits altered to balance data capacity and image distortion.

## Getting Started

To use the Image-Steganography-LSB application, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/Image-Steganography-LSB.git
   ```

2. **Navigate to the Directory**: Move into the project directory:

   ```bash
   cd Image-Steganography-LSB
   ```

3. **Install Dependencies**: Install any necessary dependencies. For example:

   ```bash
   pip install pillow
   ```

4. **Run the Application**: Execute the application by running:

   ```bash
   python main.py
   ```

5. **Follow the TUI**: The TUI will guide you through the process of embedding and extracting text in/from images using the LSB algorithm.

## Conclusion

Image-Steganography-LSB provides a valuable tool for concealing information within images while maintaining visual integrity. By leveraging the power of the LSB algorithm, this project demonstrates how technology can be used creatively for covert communication. Feel free to explore, experiment, and contribute to enhance the capabilities of this image steganography application.

If you encounter any issues, have suggestions, or want to contribute, don't hesitate to open an issue or submit a pull request. Happy coding and steganographing!

**Note**: Remember that while steganography can be fun and educational, it's important to use technology responsibly and ethically. Always respect privacy and legal boundaries when working with hidden information.