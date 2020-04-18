class PointsCalculationPolicy:

    def __init__(self):
        pass


def type_check(obj):
    if type(obj) is not PointsCalculationPolicy:
        raise TypeError
