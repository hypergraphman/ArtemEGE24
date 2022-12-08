for a in range(1, 1000):
    if all(((x & 28 != 0) or (x & 45 != 0)) <= ((x & 48 == 0) <= (x & a != 0)) for x in range(1, 1000)):
        print(a)
        break