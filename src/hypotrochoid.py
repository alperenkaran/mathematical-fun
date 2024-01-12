from .mathematical_object import MathematicalObject

import numpy as np


class Hypotrochoid(MathematicalObject):
    @staticmethod
    def _generate_points(n_points, R=3, r=1, d=1):
        theta_values = np.linspace(0, 2 * np.pi, n_points)
        x_values = (R - r) * np.cos(theta_values) + d * np.cos((R - r) / r * theta_values)
        y_values = (R - r) * np.sin(theta_values) - d * np.sin((R - r) / r * theta_values)

        points = np.column_stack((x_values, y_values))
        return points
