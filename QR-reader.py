from pyzbar.pyzbar import decode

from PIL import Image

def decoded (img):
	decodeObject = decode(img)
	for obj in decodeObject:
		print(f"type:{obj.type} ")
		print(f"data:{obj.data} , {type(obj.data)}")
		print(f"rect:{obj.rect} ")
		print(f"polygon:{obj.polygon} ")


def qr_data(img):
	decodeObject = decode(img)
	for obj in decodeObject:
		d = obj.data.decode('UTF-8')
	
	return d




if __name__ == '__main__':
	imgPATH = "/home/mehdi/Downloads/myqrcode.png"
	img = Image.open(imgPATH) 

	print(f"data of QR-Code is :{qr_data(img)}")
	
	