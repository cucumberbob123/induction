def calculateMinibusNeeded(m, s, p):
    if m * s >= p:
        return 0
    else:
        seatsNeeded = p - m * s
        if seatsNeeded % s == 0:
            return seatsNeeded // s
        return (seatsNeeded // s) + 1
