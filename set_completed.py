#!/usr/bin/python2

"""
Author: beredim
"""

import bencode
import sys
from os import path

if len(sys.argv) < 2:
    print "First argument: Resume File"
    sys.exit(0)

resume_file = open(sys.argv[1])
decoded_data = bencode.bdecode(resume_file.read())
resume_file.close()

decoded_data['progress']["blocks"]="all"
decoded_data['progress']["have"]="all"

f = open(sys.argv[1],"w")
f.write(bencode.bencode(decoded_data))
f.close()
