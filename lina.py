
"""Linear Algebra utilities. A vector is represented as a list of elements (e.g. [1, 2, 3])."""

def vector_distance(v1, v2):
    """
    Returns the distance between the given vectors v1 and v2, which is the absolute difference between their
    lengths.
    """

    return abs(vector_length(v1) - vector_length(v2))

def scalar_product(a, b):
    """Returns the scalar product of the vectors a and b, which is a1 * b1 + a2 * b2 + ... + an * bn."""

    returnValue = 0
    for i in range(0, len(a)):
        returnValue += a[i] * b[i]
    return returnValue

def vector_sub(a, b):
    """Returns the vector which is the result of subtracting the given vectors a and b."""

    result = []
    for i in range(0, len(a)):
        result.append(a[i] - b[i])
    return result

def vector_length(v):
    """Returns the length of the given vector v, which is the square root of v1^2 + v2^2 + ... + vn^2."""

    length = 0
    for e in v:
        length += pow(e, 2)
    length = pow(length, 0.5)
    return length

def vector_equals(a, b):
    """Returns True if all the elements of a are identical to all the elements b. Otherwise False."""

    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True
