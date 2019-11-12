import sys
import struct

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

SECTION_ASCII = 1
SECTION_UTF8 = 2
SECTION_WORDS = 3
SECTION_DWORDS = 4
SECTION_DOUBLES = 5
SECTION_COORD = 6
SECTION_REFERENCE = 7
SECTION_PNG = 8
SECTION_GIF87 = 9
SECTION_GIF89 = 10


if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

magic, version = struct.unpack("<LL", data[0:8])
timestamp, author = struct.unpack("<L8s", data[8:20])
(section,) = struct.unpack("<L", data[20:24])


if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % str(author))
print("SECTIONS: %d" % int(section))

print("-------  BODY  -------")
offset = 24
i = 0


while i < int(section):

    stype, slen = struct.unpack("<LL", data[offset:offset+8])
    slen = int(slen)

    if stype == SECTION_ASCII:
        (output,) = struct.unpack(("<%ds" % slen), data[offset + 8: (offset + 8 + slen)])
        print("ASCII OUTPUT: %s" % (output))
        
    elif stype == SECTION_UTF8:
        (output,) = struct.unpack(("<%ds" % slen), data[offset + 8: (offset + 8 + slen)])
        output = output.decode('utf-8')
        print("UTF-8 OUTPUT: %s" % (output))
        
    elif stype == SECTION_WORDS:
        words = int(slen/4)
        (output,) = struct.unpack(("<%s" % ('L' * words)), data[offset + 8: (offset + 8 + slen)])
        print("WORDS OUTPUT: %s" % (output))
        
    elif stype == SECTION_DWORDS:
        dwords = int(slen/8)
        (output,) = struct.unpack(("<%s" % ('L' * dwords)), data[offset + 8: (offset + 8 + slen)])
        print("DWORDS OUTPUT: %s" % (output))

    elif stype == SECTION_DOUBLES:
        doubles = int(slen/8)
        (output,) = struct.unpack(("<%s" % ('L' * doubles)), data[offset + 8: (offset + 8 + slen)])
        print("DOUBLES OUTPUT: %s" % (output))

    elif stype == SECTION_COORD:
        output = struct.unpack("<dd", data[offset + 8: (offset + 8 + slen)])
       	print("COORDS OUTPUT: %s" % str(output))

    elif stype == SECTION_REFERENCE:
        output = struct.unpack("<L", data[offset + 8: (offset + 8 + slen)])
        print("REFRENCE OUTPUT: %d" % output[0])
            
    elif stype == SECTION_PNG:
        output = struct.unpack(("<%s" % ('B' * slen)), data[offset + 8: (offset + 8 + slen)])
        im_data = [137, 80, 78, 71, 13, 10, 26, 10] + list(output)
        file = open("png_data.png", "wb")
        file.write(bytearray(im_data))
        print("PNG CREATED")
        
    elif stype == SECTION_GIF87:
        output = struct.unpack(("<%s" % ('B' * slen)), data[offset + 8: (offset + 8 + slen)])
        im_data = [47, 49, 46, 38, 37, 61] + list(output)
        file = open("gif87_data.gif", "wb")
        file.write(bytearray(im_data))
        print("GIF87 CREATED")
        
    elif stype == SECTION_GIF89:
        output = struct.unpack(("<%s" % ('B' * slen)), data[offset + 8: (offset + 8 + slen)])
        im_data = [47, 49, 46, 38, 39, 61] + list(output)
        file = open("gif89_data.gif", "wb")
        file.write(bytearray(im_data))
        print("GIF89 CREATED")

    offset = offset + slen + 8
    i = i + 1