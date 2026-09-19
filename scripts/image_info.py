"""Print dimensions and size of the extracted JPEGs by reading their SOF markers."""

import glob
import os
import struct


def size_of(path: str) -> tuple[int, int]:
    data = open(path, "rb").read()
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[i + 5 : i + 9])
            return width, height
        i += 2 + struct.unpack(">H", data[i + 2 : i + 4])[0]
    raise ValueError(f"no SOF marker in {path}")


for path in sorted(glob.glob("src/assets/images/*.jpg")):
    width, height = size_of(path)
    kb = os.path.getsize(path) // 1024
    print(f"{os.path.basename(path):16} {width}x{height}  {kb} KB")
