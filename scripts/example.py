import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from mach1py import mach1file

obj = mach1file("./tests/test_correct.txt")
