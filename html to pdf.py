import weasyprint
from PIL import Image
import os
import getpass

url = 'https://www.google.com/'
filename = '/home/' + getpass.getuser() + '/Downloads/09.jpg'


def html_to_pdf_converter(url):
    pdf = weasyprint.HTML(url).write_pdf()
    open('/home/' + getpass.getuser() + '/Downloads/googlee.pdf', 'wb').write(pdf)


html_to_pdf_converter(url)


def img_to_pdf_converter(filename):
    image1 = Image.open(filename)
    im1 = image1.convert('RGB')
    newfilename = filename[:-3] + "pdf"
    if not os.path.exists(newfilename):
        im1.save(newfilename)
        print("save")


img_to_pdf_converter(filename)
