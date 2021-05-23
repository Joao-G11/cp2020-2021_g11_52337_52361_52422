# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import random

if (len(sys.argv) != 3 or len(sys.argv) != 4) : 
    print("invalid number of arguments please use: python <filename> <number particles> <max_position> <max_energy>");
    print("optional - if you want tendencies use te same command as above with extra parameter <mode> with 0 < mode < maxposition or max energy")
    sys.exit(-1);
    



nParticles  = int(sys.argv[1])
maxPosition = int(sys.argv[2])
max_energy  = int(sys.argv[3])

if(len(sys.argv) == 3):

    for i in range (nParticles):
        position = random.randint(1, maxPosition)
        energy = random.randint(1, max_energy)
        print('%d %d' % (position, energy))
            
else:
    
    mode = int(sys.argv[4])
    for i in range (nParticles):
        position = int(random.triangular(1, maxPosition, mode))
        energy = int(random.triangular(1, max_energy, mode))
        print('%d %d' % (position, energy))


# To save in file this program > output filename

