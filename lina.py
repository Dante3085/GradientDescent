
"""Linear Algebra utilities."""

def vector_distance(v1, v2):
    return abs(vector_length(v1) - vector_length(v2))

def scalar_product(a, b):
    returnValue = 0
    for i in range(0, len(a)):
        returnValue += a[i] * b[i]
    return returnValue

def vector_sub(a, b):
    result = []
    for i in range(0, len(a)):
        result.append(a[i] - b[i])
    return result

def vector_length(v):
    length = 0
    for e in v:
        length += pow(e, 2)
    length = pow(length, 0.5)
    return length

def vector_equals(a, b):
    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True
