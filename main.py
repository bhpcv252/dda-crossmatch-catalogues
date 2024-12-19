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

def angular_dist(ra1, dec1, ra2, dec2):
    r1 = np.radians(ra1)
    d1 = np.radians(dec1)
    r2 = np.radians(ra2)
    d2 = np.radians(dec2)

    a = np.sin(abs(d1 - d2)/2)**2
    b = np.cos(d1)*np.cos(d2)*np.sin(abs(r1-r2)/2)**2
    d = 2 * np.arcsin(np.sqrt(a + b))
    return np.degrees(d)

def crossmatch(bss_cat, super_cat, max_dist):
    matches = []
    no_matches = []
    for bcr in bss_cat:
        closest_dist = float('inf')
        bss_row_id = bcr[0]
        super_row_id = 0
        for scr in super_cat:
            dist = angular_dist(bcr[1], bcr[2], scr[1], scr[2])
            if dist < closest_dist and dist < max_dist:
                closest_dist = dist
                super_row_id = scr[0]
        
        if super_row_id > 0:
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
