def powerof(x, y):
    if y <= 0:
        return 1

    return powerof(x, y-1) * x


print(powerof(4, 4))
