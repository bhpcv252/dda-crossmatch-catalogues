import numpy as np
import math

def hms2dec(h,  m, s):
    return 15*(h + m/60 + s/(60*60))

def dms2dec(d, m, s):
    return math.copysign(1, d) * (abs(d) + m/60 + s/(60*60))

def import_bss():
    bss_cat = np.loadtxt('bss.dat', usecols=range(1,7))
    data = []
    for i in range(len(bss_cat)):
        data.append((i+1, hms2dec(bss_cat[i][0], bss_cat[i][1], bss_cat[i][2]), dms2dec(bss_cat[i][3], bss_cat[i][4], bss_cat[i][5]) ))
    return data

def import_super():
    super_cat = np.loadtxt('super.csv', delimiter=',' , skiprows=1, usecols=[0, 1])
    data = []
    for i in range(len(super_cat)):
        data.append((i+1, super_cat[i][0], super_cat[i][1]))
    return data

def angular_dist(r1,d1,r2s,d2s):
    a = np.sin(np.absolute(d1 - d2s) / 2) ** 2
    b = np.cos(d1) * np.cos(d2s) * np.sin(np.absolute(r1 - r2s) / 2) ** 2
    d = 2 * np.arcsin(np.sqrt(a + b))
    return d #in radians


def crossmatch(bss_cat, super_cat, max_dist):
    bss_cat_rad = np.radians(bss_cat)
    super_cat_rad = np.radians(super_cat)
    matches = []
    no_matches = []
    for i in range(len(bss_cat_rad)):
        bss_row_id = i
        super_row_id = -1
        dists = angular_dist(bss_cat_rad[i][0], bss_cat_rad[i][1], super_cat_rad[:, 0], super_cat_rad[:, 1])
        closest_dist = np.degrees(np.min(dists))
        if closest_dist <= max_dist:
            super_row_id = np.argmin(dists)
            matches.append((bss_row_id, super_row_id, closest_dist))
        else:
            no_matches.append(bss_row_id)
    return (matches, no_matches)


if __name__ == '__main__':
    bss_cat = import_bss()
    super_cat = import_super()

    max_dist = 40/3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(matches[:3])
    print(no_matches[:3])
    print(len(matches), "matched and", len(no_matches), "didn't match.")

    max_dist = 5/3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(matches[:3])
    print(no_matches[:3])
    print(len(matches), "matched and", len(no_matches), "didn't match.")
