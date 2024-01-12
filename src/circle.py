from .mathematical_object import MathematicalObject

import numpy as np


class Circle(MathematicalObject):
    @staticmethod
    def _generate_points(n_points, radius=1):
        theta_values = np.random.random(size=n_points) * 2 * np.pi
        x_values = radius * np.cos(theta_values)
        y_values = radius * np.sin(theta_values)

        points = np.column_stack((x_values, y_values))
        return points
