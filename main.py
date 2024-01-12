from src import ButterflyCurve, Circle, Hypotrochoid, LissajousCurve, SierpinskiTriangle


def main():
    butterfly_curve = ButterflyCurve(n_points=1000)
    butterfly_curve.plot(filename='butterfly_curve.png')

    circle = Circle(n_points=250, radius=3)
    circle.plot(filename='circle.png')

    hypotrochoid = Hypotrochoid(n_points=800, R=3, r=.5, d=3)
    hypotrochoid.plot(filename='hypotrochoid.png')

    lissajous_curve = LissajousCurve(n_points=1000, a=3, b=2, delta=3.14)
    lissajous_curve.plot(filename='lissajous_curve.png')

    sierpinski_triangle = SierpinskiTriangle(1500, corners=[(0, 0), (2, 0), (1, 1)])
    sierpinski_triangle.plot(filename='sierpinski_triangle.png')


if __name__ == "__main__":
    main()
