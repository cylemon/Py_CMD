# -*- coding=utf-8 -*-

from PIL import Image
import argparse

def parse_param():
	parser = argparse.ArgumentParser()
	parser.add_argument('in_file')
	parser.add_argument('out_file')
	parser.add_argument('--width', type = int, default = 120) 
	parser.add_argument('--height', type = int, default = 70)

	args = parser.parse_args()
	in_file = args.in_file
	out_file = args.out_file
	width = args.width
	height = args.height
	return in_file, out_file, width, height

def get_char(r,g,b,alpha = 256):
	if alpha == 0:
		return ' '
	gray = (2126 * r + 7152 * g + 722 * b) / 10000
	ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
	length = len(ascii_char)
	unit = (256.0 + 1)/length
	return ascii_char[int(gray/unit)]

def write_file(out_file_name, content):
	if out_file_name:
		with open(out_file_name,'w') as f:
			f.write(content)
	else:
		with open("output.txt",'w') as f:
			f.write(content)


def main(file_name,width,height,out_file_name):
	text = ""
	im = Image.open(file_name)
	im = im.resize((width,height),Image.NEAREST)
	for i in range(height):
		for j in range(width):
			content = im.getpixel((j, i))
			text += get_char(*content)
		text += '\n'
		print(text)
		write_file(out_file_name, text)


if __name__ == '__main__':
	in_f, out_f, width, height = parse_param()
	main(file_name=in_f, width=width, height=height, out_file_name=out_f)

