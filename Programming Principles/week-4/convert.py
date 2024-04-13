MM_IN_INCH = 25.4
MM_IN_FOOT = 304.8
MM_IN_YARD = 914.4
MM_IN_MILE = 1609344


def cm2inches(cm):
    return cm * 0.393


def m2feet(m):
    return m * 3.281


def m2feetAdd(m1, m2):
    return (m1 * 3.281) + (m2 * 3.281)


def m2yards(m):
    return m * 1.094


def km2miles(km):
    return km * 0.621
