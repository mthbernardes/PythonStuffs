from StringIO import StringIO
from macholib import macho_dump
import sys
import os

fp = StringIO()
macho_dump.print_file(fp, sys.argv[1])
lines = fp.getvalue().splitlines()

print lines

raw_input()
os.system('file '+sys.argv[1])

raw_input()
os.system('strings '+sys.argv[1])
