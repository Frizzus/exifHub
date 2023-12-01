import argparse

parser = argparse.ArgumentParser(prog = "exifHub", description = "exif tool for jpeg/png/pdf")
parser.add_argument("file_path")
parser.add_argument("-o", "--output", help = "Specify the output files where data will be written.")

args = parser.parse_args()

img_file = open(args.file_path, "rb")
img_bytes = img_file.read()

in_app1 = False
app1_hexs:list[str] = []
i = 0
while i < len(img_bytes):
    if in_app1:
        app1_hexs.append(hex(img_bytes[i]))
        if hex(img_bytes[i]) == "0xff":
            in_app1 = False
            app1_hexs = app1_hexs[:-1]
            print(app1_hexs)
            print("début du marker suivant")
        i += 1
    else:
        if hex(img_bytes[i]) == "0xff" and hex(img_bytes[i+1]) == "0xe1":
            print("l'index du marqueur APP1 se trouve à l'index : ", i)
            in_app1 = True
        i += 2
