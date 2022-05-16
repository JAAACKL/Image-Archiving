import os, sys
from PIL import Image
import numpy as np
import zlib

infile = sys.argv[1]
compressed_image = 'compressed_' + os.path.splitext(infile)[0] + '.webp'
archive = os.path.splitext(infile)[0] + '.bin'

#try:
print('Encoding ' + infile)
print('Original Image Size: ', os.path.getsize(infile) / 1000)
with Image.open(infile) as im:
    try:
        im.save(compressed_image,optimize=True,lossless=True,format="WEBP")
    except:
        if os.name == 'posix':
            os.system('cp ' + infile + ' ' + compressed_image)
        else:
            os.system('copy ' + infile + ' ' + compressed_image)
    print('WebP Conversion Size: ', os.path.getsize(compressed_image) / 1000)
    smaller_file = compressed_image
    if os.path.getsize(compressed_image) >= os.path.getsize(infile):
        smaller_file = infile
    with open(smaller_file, "rb") as cim:
        compressed_data = zlib.compress(cim.read(), level=9)
        f = open(archive, "wb")
        f.write(compressed_data)
        f.close()
        os.remove(compressed_image)
        print('Compressed Archive Size: ', os.path.getsize(archive) / 1000)
        print('compression ratio = ', os.path.getsize(archive) / os.path.getsize(infile))
    with open(archive, "rb") as archived_bytes:
        print('Decoding ' + archive)
        original_data = zlib.decompress(archived_bytes.read())
        f = open(compressed_image, "wb")
        f.write(original_data)
        f.close()
    with Image.open(compressed_image) as retrieved_im:
        #retrieved_im.show()
        os.remove(compressed_image)
#except Exception as e:
    #print(e)