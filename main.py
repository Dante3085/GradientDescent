
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
def func(x):
    return (pow(x, 2) * math.cos(x) - x) / (10)

# gradient(f(x)) = ()^T

gd = GradientDescent(func=func, gradient=[gradient_part_1],
                     startValue=[10], stepSize=0.5)

print(str(gd.gradient_descent()))