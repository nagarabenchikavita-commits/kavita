import barcode
from barcode.writer import ImageWriter
from Ipython.display import Image, display

def generate_barcode(data):
    BarcodeClass = barcode.get_barcode_class('code128')
    code = BarcodeClass(data,writer=Imagewriter())
    barcode_filename = code.save("barcode")

    print("Barcode Generated.")

    dispaly(Image(filname=barcode_filename))

data = '1234-5678-9012'
generate_barcode(data)