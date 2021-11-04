
from Optimization import GradientDescent
import math

# # f(x) = x^2
# def x_squared(x):
#     return x * x
#
# # f'(x) = 2*x
# def two_x(x):
#     return 2*x
#
# # f(x) = x^2 + y^2 - x*y + 9*x - 6*y + 2
# def func(x, y):
#     return x*x + y*y - x*y + 9*x - 6*y + 2
#
# def gradient_part_1(arg):
#     return 2*arg[0] - arg[1] + 9
#
# def gradient_part_2(arg):
#     return 2*arg[1] - arg[0] - 6

# # f(x) = x^2 - 4x
# def func(x):
#     return x*x - 4*x
#
# # gradient(f(x)) = (2x-4)^T
# def gradient_part_1(arg):
#     return 2*arg[0] - 4

# f(x) = (x^2 * cos(x) - x) / (10)
# def func(x):
#     return (pow(x, 2) * math.cos(x) - x) / (10)

# gradient(f(x)) = ()^T

# TODO: Symbole aus func Argument extrahieren und funcArgs Argument entfernen.
# TODO: Nach numpy array umstellen, um Vektorberechnungen zu vereinfachen.
# TODO: Vektor utilities in separates Modul verlagern.
# TODO: Auch Maxima. Falls Funktion kein Minimum und nur Maximum hat, explodieren die Zahlen aktuell einfach.
#       Lösung wäre das Vorzeichen von n*(Gradient(currentValue)) für Minima(-) und Maxima(+)
#       dynamisch anzupassen. Dann heiß das ganze aber nicht mehr Gradient "Descent", sondern
#       Gradient "Climb" (Climb/Klettern: Man sowohl aufsteigend als auch absteigend klettern.)
# gd = GradientDescent(func="x**2 + y**2 - x*y + 9*x - 6*y + 2", funcArgs=["x", "y"],
#                      startValue=[0, 0], stepSize=.5, precision=-1)

gd = GradientDescent(func="-2*a**2 + 48*a", funcArgs=["a"], startValue=[33],
                     stepSize=.1, precision=-1)

print(str(gd.gradient_descent()))