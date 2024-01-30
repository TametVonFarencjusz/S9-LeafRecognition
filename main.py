import os
from PIL import Image

def PNGToJPG():
    data_dir = 'Data'
    data_dir_out = 'Data2'

    for dataname in os.listdir(data_dir):
        f = os.path.join(data_dir, dataname)
        # checking if it is a file
        # print(f)

        # od = os.path.join(data_dir_out, dataname)
        # try:
        #     os.mkdir(od)
        # except:
        #     pass

        for leafname in os.listdir(f):
            l = os.path.join(f, leafname)
            # checking if it is a file
            # print(l)

            od = os.path.join(data_dir_out, dataname, leafname)
            try:
                os.makedirs(od)
            except:
                pass

            for img in os.listdir(l):
                i = os.path.join(l, img)
                # checking if it is a file
                # print(i)

                oi = os.path.join(od, img[:-3] + "jpg")
                print(oi)

                png = Image.open(i).convert('RGBA')
                background = Image.new('RGBA', png.size, (255,255,255))
                alpha_composite = Image.alpha_composite(background, png)
                alpha_composite_2 = alpha_composite.convert('RGB')
                alpha_composite_2.save(oi, 'JPEG', quality=80)
                # new_image = image.resize((500, 500))

def SizeDown(down = 2):
    data_dir = 'Data2'
    data_dir_out = 'Data2_Small_'+str(down)

    for dataname in os.listdir(data_dir):
        f = os.path.join(data_dir, dataname)
        for leafname in os.listdir(f):
            l = os.path.join(f, leafname)
            od = os.path.join(data_dir_out, dataname, leafname)
            try:
                os.makedirs(od)
            except:
                pass
            for img in os.listdir(l):
                i = os.path.join(l, img)
                # checking if it is a file
                # print(i)

                oi = os.path.join(od, img[:-3] + "jpg")
                print(oi)

                big = Image.open(i)
                new_size = (int(big.size[0]/down), int(big.size[1]/down))
                small = big.resize(new_size)
                small.save(oi, 'JPEG', quality=80)


if __name__ == '__main__':
    #PNGToJPG()
    SizeDown(16)
