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

License Terms
-------------
 
::
 Copyright (C) 2012 Jean-Bernard Ratté (http://unary.ca:8080)

 Permission is hereby granted, free of charge, to any person obtaining a copy 
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
 copies of the Software, and to permit persons to whom the Software is 
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
 SOFTWARE.
