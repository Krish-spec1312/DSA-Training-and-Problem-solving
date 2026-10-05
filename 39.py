def power(base,exponent):
    if exponent == 0:
        return 1
    return base * power(base,exponent-1)
print(power(2,4))
print(power(9,56))
