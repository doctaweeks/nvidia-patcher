#!/usr/bin/env python3

import platform
import mmap
import sys

release = platform.release()
orig = '/lib/modules/%s/video/nvidia.ko' % release
with open(orig, mode='a+') as f:
    with mmap.mmap(f.fileno(), 0) as s:
        idx = s.find(b'KVMKVMKVM')
        if idx == -1:
            idx = s.find(b'AAAAAAAAA')
            if idx == -1:
                print('Error: did not find signature', file=sys.stderr)
                sys.exit(1)
            else:
                print('Already patched', file=sys.stderr)
                sys.exit(0)
        s.seek(idx)
        s.write(b'AAAAAAAAA')
        s.flush()
