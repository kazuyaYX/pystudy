from PIL import Image
import os


def resize_image(path, max_h, max_w):
    for file in os.listdir(path):
        img = Image.open(path+'/'+file)
        width, height = img.size
        if height > max_h or width > max_w:
            n = max(height/max_h, width/max_w)
            new_h = int(height/n)
            new_w = int(width/n)
            img = img.resize((new_w, new_h))
            img.save(path+'/'+file)
            print(file)


if __name__ == '__main__':
    resize_image('D:/play/pystudy/0005/test', 1136, 640)