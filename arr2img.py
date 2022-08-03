#!/usr/bin/env python3

import numpy as np
import pyarts
from PIL import Image


def cloudfield():
    cf = pyarts.xml.load('export/cloudbox_field.xml')
    print(cf.shape)
    m = cf[:, 10, 0, 0, :, :, 0]
    m = np.moveaxis(m, 0, -1)
    return m


def main():
    cf = cloudfield()
    cf = cf / np.max(cf)
    print(cf.min())
    print(cf.max())
    m = cf / np.percentile(cf, 98)
    m[m > 1] = 1
    m = (m * 255).astype(np.uint8)
    Image.fromarray(m).save('pano.png')


if __name__ == "__main__":
    main()
