#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

if __name__ == '__main__':
    projDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir2rm = os.path.join(projDir, 'radioApp', 'static', 'images', 'full')
    dir2copy = os.path.join(projDir, 'radioUrls', 'radioUrls', 'images', 'full')
    try:
        shutil.rmtree(dir2rm)
    except OSError:
        pass
    
    try:
        shutil.copytree(dir2copy, dir2rm)
    except OSError:
        pass