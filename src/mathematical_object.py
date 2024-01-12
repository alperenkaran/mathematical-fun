import numpy as np
import matplotlib.pyplot as plt


class MathematicalObject(np.ndarray):
    def __new__(cls, n_points, **kwargs):
        points = cls._generate_points(n_points, **kwargs)
        obj = np.asarray(points).view(cls)
        return obj

    @staticmethod
    def _generate_points(n_points, **kwargs):
        raise NotImplementedError('Subclasses must implement _generate_points method')

    def plot(self, save=True, filename=None, **kwargs):
        plt.figure(figsize=kwargs.get('figsize', (8, 8)))
        plt.scatter(self[:, 0], self[:, 1], s=5)

        if save:
            plt.savefig(f'plots/{filename}')
        else:
            plt.show()
