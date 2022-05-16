import os, sys
from PIL import Image
import zlib

for infile in sys.argv[1:]:
    archive = infile + '.bin'
    retrieved = infile + '.webp'
    with open(archive, "rb") as archived_bytes:
        print('Decoding ' + archive)
        original_data = zlib.decompress(archived_bytes.read())
        f = open(retrieved, "wb")
        f.write(original_data)
        f.close()
    with Image.open(retrieved) as retrieved_im:
        retrieved_im.show()
        os.remove(retrieved)