
from sympy import *
import numpy

class GradientDescent:
    def __init__(self, func, funcArgs, startValue, stepSize, precision=0.01):
        """
        Prepares the necessary prerequisites for running the Gradient Descent algorithm on the given function 'func' by
        calling GradientDescent.gradient_descent().

        :param func: A string that contains the symbolic representation of the function Gradient Descent will be run on.
        :param funcArgs: A list with the names of the arguments/parameters of 'func'.
        :param startValue: A list of values, one for each argument of 'func' that determines where Gradient Descent
                           will start.
        :param stepSize: A float that describes how far each step in Gradient Descent goes.
        :param precision: If the value in the current step of Gradient Descent and the value in the previous step are
                          apart by less than this float, the process will stop and return the current value.
                          This parameter is useful to put an upper bound on the amount of steps the Gradient Descent
                          process will do, because it can sometimes take a long time until it naturally terminates
                          (i.e. no change in values between steps).
                          Set this to -1 if you want to run Gradient Descent until there is no change anymore between
                          steps.
        """

        self.gradient = self.__calc_gradient(func, funcArgs)
        self.startValue = startValue
        self.stepSize = stepSize
        self.precision = precision

    def __calc_gradient(self, func, funcArgs):
        argSymbols = []
        for argName in funcArgs:
            argSymbols.append(Symbol(argName))

        f = parse_expr(func)
        gradient = []
        for argSymbol in argSymbols:
            gradient.append(lambdify(argSymbols, diff(f, argSymbol)))

        return gradient

    def gradient_descent(self):
        previousValue = None
        currentValue = self.startValue

        if self.precision == -1:
            while previousValue is None or previousValue != currentValue:
                previousValue = currentValue
                currentValue = self.__descent(currentValue)
                self.stepSize = self.__update_stepSize(self.stepSize, currentValue, previousValue)
                print("currentValue: " + str(currentValue) + ", stepSize: " + str(self.stepSize))
        else:
            while previousValue is None or self.vector_distance(previousValue, currentValue) > self.precision:
                previousValue = currentValue
                currentValue = self.__descent(currentValue)
                self.stepSize = self.__update_stepSize(self.stepSize, currentValue, previousValue)
                print("currentValue: " + str(currentValue) + ", stepSize: " + str(self.stepSize))

        return currentValue

    # Da Funktionen mit mehreren Variablen erlaubt sind, muss standardmäßig mit Vektoren gerechnet werden.
    def __descent(self, currentValue):
        returnValue = []
        for i in range(0, len(currentValue)):
            returnValue.append(currentValue[i] - self.stepSize * self.gradient[i](*currentValue))
        return returnValue

    def __update_stepSize(self, currentStepSize, currentValue, previousValue):

        # The calculations below will not work if currentValue is the same as previousValue.
        # So we just return the currentStepSize.
        if self.vector_equals(currentValue, previousValue):
            return currentStepSize

        v = self.vector_sub(self.gradient_at(currentValue), self.gradient_at(previousValue))
        denominator = (pow(self.vector_length(v), 2))

        v2 = self.vector_sub(currentValue, previousValue)

        return (abs(self.scalar_product(v, v2))) / denominator

    def gradient_at(self, arg):
        returnValue = []
        for i in range(0, len(arg)):
            returnValue.append(self.gradient[i](*arg))
        return returnValue

    def vector_distance(self, v1, v2):
        return abs(self.vector_length(v1) - self.vector_length(v2))

    def scalar_product(self, a, b):
        returnValue = 0
        for i in range(0, len(a)):
            returnValue += a[i] * b[i]
        return returnValue

    def vector_sub(self, a, b):
        result = []
        for i in range(0, len(a)):
            result.append(a[i] - b[i])
        return result

    def vector_length(self, v):
        length = 0
        for e in v:
            length += pow(e, 2)
        length = pow(length, 0.5)
        return length

    def vector_equals(self, a, b):
        for i in range(0, len(a)):
            if a[i] != b[i]:
                return False
        return True