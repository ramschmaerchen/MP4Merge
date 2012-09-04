========
MP4Merge
========

This is a simple tool written in Python. It's goal is to merge MP4 videos into one file recursively separated by folder name.
::
 $ ls -R ~/Movies
 a

 ./a:
 a Pt1.mp4	a Pt2.mp4

Will generate a MP4 file: ~/Movies/a/a.mp4

Project Structure
-----------------

 * mp4merge.py : Main program executable

Dev Guide
---------

 * git clone https://github.com/nap/MP4Merge.git
 * Build from source MP4Box http://gpac.sourceforge.net/
 * Or use brew install MP4Box

Dependencies
------------

 #. MP4Box

Author
------

 * jean.bernard.ratte@unary.ca
