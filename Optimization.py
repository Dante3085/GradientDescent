
class GradientDescent:
    def __init__(self, func, gradient, startValue, stepSize):
        self.func = func
        self.gradient = gradient # calc_gradient(func)
        self.startValue = startValue
        self.stepSize = stepSize

    def __calc_gradient(self, func):
        pass

    def gradient_descent(self):
        previousValue = None
        currentValue = self.startValue

        # Do gradient descent as long as there is change.
        while previousValue is None or self.vector_distance(previousValue, currentValue) > 0.01:
            previousValue = currentValue
            currentValue = self.__descent(currentValue)

        return currentValue

    # Da Funktionen mit mehreren Variablen erlaubt sind, muss standardmäßig mit Vektoren gerechnet werden.
    def __descent(self, currentValue):
        returnValue = []
        for i in range(0, len(currentValue)):
            returnValue.append(currentValue[i] - self.stepSize * self.gradient[i](currentValue))
        return returnValue

    def vector_distance(self, v1, v2):
        return abs(self.vector_length(v1) - self.vector_length(v2))

    def vector_length(self, v):
        length = 0
        for e in v:
            length += pow(e, 2)
        length = pow(length, 0.5)
        return length