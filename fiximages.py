import sys
import os
import imghdr
from PIL import Image

def imagerenametree(src, symlinks=False):
    names = os.listdir(src)
    
    for name in names:
        srcname = os.path.join(src, name)
        if os.path.isdir(srcname):
            imagerenametree(srcname, symlinks)
        else:
            filetype = imghdr.what(srcname)
            # check extension, rename if missing
            if None != filetype:
                    filename, file_extension = os.path.splitext(srcname)
                    if "" == file_extension:
                         print ("Rename file from %s to %s.%s" % (srcname, filename, filetype))
                         os.rename(srcname, filename + '.' + filetype)
                    else:
                         print ("File %s already has correct extension of %s." % (srcname, file_extension))
            else:
                    print ("File %s is not an image" % srcname )



if 2 != len(sys.argv):
    print ("Invalid number of arguments")
else:
    imagerenametree(sys.argv[1], symlinks=False)
