from .mathematical_object import MathematicalObject

import numpy as np


class LissajousCurve(MathematicalObject):

    @staticmethod
    def _generate_points(n_points, a=1, b=1, delta=0):
        t = np.linspace(0, 2 * np.pi, n_points)
        x = np.sin(a * t + delta)
        y = np.sin(b * t)

        points = np.column_stack((x, y))
        return points
