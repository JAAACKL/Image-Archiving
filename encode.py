import os, sys, base64, math
import numpy as np
import zlib
from PIL import Image

def diff(old, new):
    d = [0] * len(old)
    for i in range(len(old)):
        d[i] = new[i] - old[i]
    return d

def rle_encode(message):
    encoded_string = []
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
            '''
            if the character at the current index is the same as the character at the next index. If the characters are the same, the count is incremented to 1
            '''
            if all(message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
            '''
            the count and the character is concatenated to the encoded string
            '''
        encoded_string.append(count)
        encoded_string.append(ch)
        i = j + 1
    return encoded_string

def rle_decode(message):
    decoded_message = []
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while (i <= len(message) - 1):
        run_count = int(message[i])
        run_word = message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message

# script

for infile in sys.argv[1:]:
    
    #if not infile.startswith("compressed_"):
    """
        with open(infile, "rb") as image2string:
            # base64
            converted_string = base64.b64encode(image2string.read())
            c_file = "compressed_" + os.path.splitext(infile)[0] + ".bin"
            f = open(c_file, "wb")
            f.write(converted_string)
            f.close()
            print(os.path.getsize(infile) / 1000)
            print(os.path.getsize(c_file) / 1000)
        
        with Image.open(infile) as im:
            # delta
            data = Image.Image.getdata(im)
            deltas = []
            last = [0] * len(data[0])
            for pixel in data:
                deltas.append(diff(last, pixel))
                last = pixel
            
            converted_string = base64.b64encode(bytes(list(numpy.concatenate(deltas).flat)))
            print(converted_string)
    """
    print(infile)
    with open(infile, "rb") as im:
        compressed_data = zlib.compress(im.read(), level=9)
        c_file = "compressed_" + os.path.splitext(infile)[0] + ".bin"
        f = open(c_file, "wb")
        f.write(compressed_data)
        f.close()
        print(os.path.getsize(infile) / 1000)
        print(os.path.getsize(c_file) / 1000)
