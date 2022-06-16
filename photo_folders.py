import os
from PIL import Image
i = 0
for dirpath, _, filenames in os.walk('C:\\'):
    num_files = len(filenames)
    num_photo_files = 0
    for filename in filenames:
        _, ext = os.path.splitext(filename)
        if ext.lower() == '.jpeg' or ext.lower() == '.jpg' or ext.lower == '.png':
            try:
                im = Image.open(dirpath + '\\' + filename)
                if im.size[0] > 500 and im.size[1] > 500:
                    num_photo_files += 1
            except:
                pass
    if num_files and num_photo_files / num_files > 0.5:
        print(dirpath)
