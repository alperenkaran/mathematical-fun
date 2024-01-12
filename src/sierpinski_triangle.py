from .mathematical_object import MathematicalObject

from numbers import Number
import numpy as np


class SierpinskiTriangle(MathematicalObject):

    @staticmethod
    def _validate_corners(corners):
        """
        Checks if corners is of the wanted format.
        """
        if not (isinstance(corners, list)) or (len(corners) != 3):
            raise ValueError('Corners must be a list of three tuples.')

        for corner in corners:
            if (
                    (not isinstance(corner, tuple))
                    or (len(corner) != 2)
                    or (not isinstance(corner[0], Number))
                    or (not isinstance(corner[0], Number))
            ):
                raise ValueError('Each corner should be a tuple of two numbers.')

        (x1, y1), (x2, y2), (x3, y3) = corners
        (u1, v1), (u2, v2) = (x2 - x1, y2 - y1), (x3 - x1, y3 - y1)

        if u1 * v2 - u2 * v1 == 0:
            raise ValueError('The corners should not be linear.')

    @classmethod
    def _generate_points(cls, n_points, corners=None):
        corners = corners or [(0, 0), (1, 0), (0, 1)]
        cls._validate_corners(corners)
        points = np.zeros((n_points, 2))
        point = np.array(corners[0])

        for i in range(n_points):
            corner = corners[np.random.randint(3)]
            point = 0.5 * (point + corner)
            points[i] = point

        return points
