import qrcode


class QRCodeGenerator:

    def __init__(self, version=10, box_size=5, border=5, fill_color="black", back_color="white"):
        """ Initialize the QRCode object
        with the specified parameters """
        self.qr = qrcode.QRCode(
            version=version,
            box_size=box_size,
            border=border
        )
        self.fill_color = fill_color
        self.back_color = back_color

    def generate_qrcode(self, data, fit=True):
        """ Clears existing data,
         add new data, and
         generates the QR code """
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=fit)
        # Create the QR code image with the specified color properties
        img = self.qr.make_image(fill=self.fill_color, back_color=self.back_color)
        return img

    def save_qrcode(self, data, filename="qr.png"):
        """ Generates the QR Code image
         and save it to a file """
        img = self.generate_qrcode(data)
        img.save(filename)


if __name__ == "__main__":
    # User input
    data = input("Enter the URL or data for QR code: ")

    # Instance of QRCodeGenerator
    qrcode_generator = QRCodeGenerator()

    # Generate and save QR code based on user input
    qrcode_generator.save_qrcode(data)
