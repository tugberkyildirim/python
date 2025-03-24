# QR Code and Barcode Generator Application

This application is designed to generate various barcode types and QR codes. Users can run the application without installation requirements, easily generate barcodes and QR codes, and save them in the specified folders.

## Features

- **QR Codes**: Users can create QR codes using text, URL, or other data.
- **Barcodes**: Supported barcode types include popular formats such as EAN, UPC, Code128, Code39, and more.
- **Save Feature**: Generated QR codes and barcodes are saved in the `Data/QR Code` and `Data/Barcode` folders, respectively.
- **Supported Barcode Types**: The program supports the following barcode types:
  - **EAN-13**
  - **EAN-8**
  - **UPC-A**
  - **UPC-E**
  - **Code128**
  - **Code39**
  - **Interleaved 2 of 5**
  - **ITF-14**
  - **EAN-14**
  - **Codabar**
  - **MSI Plessey**
  - **ISBN**
  - **ISBN-13**
  - **ISSN**

## Installation

### Windows Application

This application is a standalone `.exe` file.
1. Run the downloaded `.exe` file to launch the application.

## Usage

1. **Generate QR Code**:
   - On the main screen, enter the text or URL for the QR code you want to create.
   - Click the "Generate QR Code" button.
   - The QR code will be saved in the `Data/QR Code` folder in `.png` format.

2. **Generate Barcode**:
   - On the main screen, enter the text for the barcode you want to create.
   - Select the barcode type (e.g., EAN-13, Code128, etc.).
   - Click the "Generate Barcode" button.
   - The barcode will be saved in the `Data/Barcode` folder in `.png` format.

### Supported Barcode Types

The following barcode types are supported:

- **EAN-13**: EAN-13 Barcode
- **EAN-8**: EAN-8 Barcode
- **UPC-A**: UPC-A Barcode
- **UPC-E**: UPC-E Barcode
- **Code128**: Code128 Barcode
- **Code39**: Code39 Barcode
- **Interleaved 2 of 5**: Interleaved 2 of 5 Barcode
- **ITF-14**: ITF-14 Barcode
- **EAN-14**: EAN-14 Barcode
- **Codabar**: Codabar Barcode
- **MSI Plessey**: MSI Plessey Barcode
- **ISBN**: ISBN Barcode
- **ISBN-13**: ISBN-13 Barcode
- **ISSN**: ISSN Barcode

### Save Location

The generated QR codes and barcodes are saved in the following folders:
- **QR Codes**: `Data/QR Code`
- **Barcodes**: `Data/Barcode`

## Program Flow

1. **Generate QR Code**:
   - Users can enter text or URL to generate a QR code.
   - The generated QR code will be saved in the specified folder.

2. **Generate Barcode**:
   - Users enter barcode data and select the barcode type.
   - The selected barcode will be generated and saved in the specified folder.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
