from .mathematical_object import MathematicalObject

import numpy as np


class ButterflyCurve(MathematicalObject):

    @staticmethod
    def _generate_points(n_points):
        theta_values = np.linspace(0, 24 * np.pi, n_points)
        r_values = np.exp(np.sin(theta_values)) - 2 * np.cos(4 * theta_values) + np.sin(theta_values / 12) ** 5

        x_values = r_values * np.cos(theta_values)
        y_values = r_values * np.sin(theta_values)

        points = np.column_stack((x_values, y_values))
        return points

