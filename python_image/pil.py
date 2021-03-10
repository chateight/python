from PIL import Image
import glob, os, time


def conv(files):
    for f in files:
        ftitle, fext = os.path.splitext(os.path.basename(f))
        imr = Image.open(f)
        im_thumb =  (200, 200)
        imr.thumbnail(im_thumb)
#    imr = imr.rotate(90, expand=True)
#    imr = imr.resize([x // 4 for x in imr.size]).resize(imr.size)
        

        imr.save(os.path.join(dst_dir, ftitle + '_thumb' + fext), 'jpeg')

src_dir = 'img'
dst_dir = 'imgs'

files = glob.glob(os.path.join(src_dir, '*.jpeg'))
if files:
    files
else:
    files = glob.glob(os.path.join(src_dir, '*.jpg'))

t1 = time.time()
conv(files)
print('{:.2f}'.format(time.time() - t1))


