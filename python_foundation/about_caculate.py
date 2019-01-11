#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TOTAL:（(x -111)*0.4+38）/195
SOA：((y-29-18)*0.6+29)/135
MOBILE：((y-27-2)*0.6+27)/69
DATA：((y-17-18)*0.6+17)/74
"""

# c = 378
c = 378
d = 107
m = 98

total = c + d + m

tt = (total - 111) * 0.4 + 38
cc = (c - 29 - 18) * 0.6 + 29
dd = (d - 17 - 18) * 0.6 + 17
mm = (m - 27 - 2) * 0.6 + 27

gx_c = c - cc
gx_d = d - dd
gx_m = m - mm


print("Total=", total)
print("tt=", tt)
print("cc=", cc, "dd=", dd, "mm=", mm)
print("gx_c=", gx_c, "gx_d=", gx_d, "gx_m=", gx_m)
print("gx_c=", gx_c/tt, "gx_d=", gx_d/tt, "gx_m=", gx_m/tt)

print("T：", ((total - 111) * 0.4 + 38) / 195)
print("C：", ((c - 29 - 18) * 0.6 + 29) / 135)
print("D：", ((d - 17 - 18) * 0.6 + 17) / 74)
print("M：", ((m - 27 - 2) * 0.6 + 27) / 69)

