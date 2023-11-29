import argparse

parser = argparse.ArgumentParser(prog = "exifHub", description = "exif tool for jpeg/png/pdf")
parser.add_argument("file_path")
parser.add_argument("-o", "--output", help = "Specify the output files where data will be written.")

args = parser.parse_args()

img_file = open(args.file_path, "rb")
img_bytes = img_file.read()

for i in range(len(img_bytes)-1):
    # print(hex(img_bytes[i]))
    if hex(img_bytes[i]) == "0xff" and hex(img_bytes[i+1]) == "0xe1":
        print("l'index du marqueur APP1 se trouve à l'index : ", i)
