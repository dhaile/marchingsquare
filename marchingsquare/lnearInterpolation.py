# -*- coding: utf-8 -*-

#  @params
#        p =
#        q =
#        r =
#        s =
#        sigma = isovalues on the grid
#
#        p = (px, py, pz)


class LinearInterpolation:

    def interpolate(self, p, q, sp, sq, sigma):
        (px, py, pz) = p
        (qx, qy,) = q
        alpha = (sigma - sp) / (sq - sp)
        rx = (1 - alpha) * px + alpha * qx
        ry = (1 - alpha) * qy + alpha * qy
        r = (rx, ry)
        return r
