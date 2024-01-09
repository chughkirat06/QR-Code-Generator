# QR Code Generator

The QR Code Generator is a simple Python script that generates QR codes for a given URL or data using the qrcode library.

## Installation

1. Clone the repository:
   git clone https://github.com/chughkirat06/QR-Code-Generator.git

## Setup

1. Navigate to project directory:
   cd QR-Code-Generator

2. Install the required dependencies:
   pip install qrcode

## Usage

1. To generate a QR code, run the script and provide the URL or data when prompted:
   python qrcodegenerator.py
The generated QR code will be saved as "qr.png" in the project directory.

## Customzation
You can customize the QR code generation by modifying the parameters in the QRCodeGenerator class. Open the qrcodegenerator.py file and adjust the values in the __init__ method to suit your preferences.
### Example customization
qrcode_generator = QRCodeGenerator(version=15, box_size=10, border=5, fill_color="black", back_color="orange")



   
