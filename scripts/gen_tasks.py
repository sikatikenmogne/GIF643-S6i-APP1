#!/usr/bin/env python3

import glob, os, sys

dirname = "./"
if len(sys.argv) >= 2:
    dirname = sys.argv[1]

width = 480
if len(sys.argv) >= 3:
    out_dirname = sys.argv[2]

if len(sys.argv) >= 4:
    width = int(sys.argv[3])

os.chdir(dirname)
files = glob.glob("*.svg")

for f in files:
    basename    = os.path.splitext(f)[0]
    pngname     = basename + ".png"
    print("%s;%s;%s"%(
        os.path.join(dirname, f),
        os.path.join(out_dirname, pngname),
        width))
