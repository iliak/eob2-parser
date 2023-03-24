# eye-of-the-beholder-2 resource parser
Eye of The Beholder 2 file format extractor

 - Put EOB2 original game data in data/ 
 - create a virtual environment (Python 3.10)
 - run "pip install -r requirements.txt"
 - run "python extract.py"
 - look in build/ ;)




Westwood CPS format : https://moddingwiki.shikadi.net/wiki/Westwood_CPS_Format

## ADL
The .adl files contains the sounds

## CPS
The .cps files contains images. Usually are 320x200 pixel in size, 256 colors for PC version, 32 colors for Amiga version.
The images can be compressed with different compression method. They may or may not contain a palette. 
The palette in case that it exist is placed just after the header. 
The image data is placed after the header and the palette.

## DAT
The .dat files contains the decoration rectangle data files (.dat) that are bundled with each decoration image file.

## DCR

## DEC
The .dec files contains decoration rectangle data files. See .dat.

## EGA
The .ega files contains 

## PAL
The .pal files contains external colors palette of a VGA picture (CPS/CMP/VCN fomats)

## VCN
The .vcn files contains graphics for the walls including the background. 
All walls graphics and the background is made up of 8x8 blocks. 
The .vcn file contains the data for these blocks, not how to put them together. 
The description how to put these 8x8 blocks into correct walls is defined in the .vmp files.


## VMP
The .vmp files contains information about how to put together the 8x8 blocks defined in the corresponding vcn files, into proper walls (including the background).

