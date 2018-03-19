import fnmatch
import os
from spectral import *
import spectral.io.envi as envi

#spectral images will be the library to convert .hdr to .jpg
#a/ is the directory of the hdr file is and saves the .jpg file in the location of the code

for file in os.listdir('a/'):
        if fnmatch.fnmatch('a/'+ file, '*.hdr'):
            print ('a/'+file)
            img = open_image('a/'+file)
            save_rgb(file+'.jpg', img, [29, 19, 9])
