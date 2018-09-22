# -*- coding: utf-8 -*-

#  @params
#        p =
#        q =
#        r =
#        s =
#        sigma = isovalues on the grid
#
#        p = (px, py, pz)


def LinearInterpolation (p,q,r,s, sigma):
    sigma = (sigma - s)/(r - s)
    (px, py) = p
    (qx, qy) = q
