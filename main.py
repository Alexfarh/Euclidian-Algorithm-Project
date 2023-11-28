# Use Recursion To AutoMate Euclid's Algorithm
def euclid(x: int, y: int) -> int:
    if x > y:
        remainder = x % y
        gcd = y
    else:
        remainder = y % x
        gcd = x
    if remainder != 0:
        gcd = euclid(gcd, remainder)
    return gcd


print(euclid(615, 810))
# 15
