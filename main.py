from PIL import Image, ImageFilter,ImageOps
import argparse


def blur(image, value, output):
    image.filter(ImageFilter.GaussianBlur(int(value))).save(output)

def copy(image, output):
    image.save(output)

def rotate(image, value, output):
    image.rotate(int(value)).save(output)

def crop(image, value, output):
    split_value = value.split(",")
    new_array = []
    for i in split_value:
        new_array.append(int(i))

    try:
        if (image.size[0] < new_array[0] or image.size[1] < new_array[1]):
            raise ValueError()
        image.crop(tuple(new_array)).save(output)
    except ValueError:
        print("Resmin boyutu {} bu ölçülerdedir, lütfen bu değerlere göre kırpınız.".format(image.size))

def colorize(image,value,output):
    try:
        new_image = image.convert(mode='L')
        ImageOps.colorize(new_image, value, 'white').save(output)
    except OSError:
        print("Filtre işlemi uygulanırken bir hata oluştu.Tekrar deneyiniz.")


def resize(image, value, output):
    print(image, value, output)
    split_value = value.split(",")
    new_array = []
    for i in split_value:
        new_array.append(int(i))
    image.thumbnail(tuple(new_array))
    image.save(output)

parser = argparse.ArgumentParser(description='')
parser.add_argument('image',
                    help='İşleme uygulamak istediğiniz resmin yolu ')

parser.add_argument('--mode', type=str,
                    help='Yapmak istediğiniz işlem tipi')

parser.add_argument('--value',
                    help='Yapmak istediğiniz işlemin değeri')

parser.add_argument('--output',
                    help='Yapılan işlem sonucu çıkan resmin yeni yolu')

args = parser.parse_args()
image_path = args.image
mode = args.mode
value = args.value
output = mode + ".jpg" if args.output is None else args.output
opened_image = Image.open(image_path)

if mode == "blur":
    blur(opened_image, value, output)
elif mode == "copy":
    copy(opened_image, output)
elif mode == "rotate":
    rotate(opened_image, value, output)
elif mode == "crop":
    crop(opened_image, value, output)
elif mode == "colorize":
    colorize(opened_image, value, output)
elif mode == "resize":
    resize(opened_image, value, output)
else:
    print("Yanlış mod girildi.")

print(args.image, args.mode, args.value, args.output)
