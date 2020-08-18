import sys


class Converter:

    def img_to_binary_convert(self):
        with open('/home/ezeia/Downloads/09.jpg', 'rb') as f:
            img = f.read()
        data = bin(int.from_bytes(img, byteorder=sys.byteorder))
        print(data)


if __name__ == '__main__':
    cnt = Converter()
    cnt.img_to_binary_convert()
