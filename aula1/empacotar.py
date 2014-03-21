#!/usr/bin/env python
# coding: utf-8

import sys, shutil

if len(sys.argv) < 3:
    print 'leia o manual prático'
    sys.exit(1)

shutil.make_archive(sys.argv[1], 'bztar', sys.argv[2])


