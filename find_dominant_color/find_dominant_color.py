from __future__ import print_function
import binascii
from PIL import Image
import numpy as np
import scipy.cluster
from scipy.spatial import KDTree
from webcolors import hex_to_rgb
import webcolors
css3_hex_to_names = webcolors.CSS3_HEX_TO_NAMES

def convert_rgb_to_names(rgb_tuple):
    """
        A dictionary of all the hex and their respective names in css3

        Args:
            rgb_tuple (tuple): RGB values

        Returns:
            string: Returns the dominant color
    """
    #
    css3_db = css3_hex_to_names
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'{names[index]}'

NUM_CLUSTERS = 5

print('[INFO]: Reading image ...')
im = Image.open('test_image.jpg')     # Reading the input image
im = im.resize((150, 150))      # optional, to reduce time
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

print('[INFO]: Finding clusters')
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print('[INFO]: Cluster centres:\n', codes)

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max]
colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
print('[INFO]: Most frequent is %s (RGB values) Color code:(#%s)' % (peak, colour))
peak=tuple(peak)
print(f'[INFO]: Dominant color = {convert_rgb_to_names(peak)}')