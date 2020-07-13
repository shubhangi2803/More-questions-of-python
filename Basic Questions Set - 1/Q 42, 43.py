# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# 43. Write a Python program to get OS name, platform and release information.

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)

import platform
import os
print(os.name)
print(platform.system())
print(platform.release())
