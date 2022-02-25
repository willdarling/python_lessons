# Let's use our knowledge about math to help us create some simple functions

# Example function
def half(x: int) -> float:
    y = x/2
    return y

# Return the result of tripling x
def triple(x: int) -> int:
    return x*3

# Return a fourth of x
def quarter(x: int) -> float:
    return x/4

# Add these two numbers then multiply by 5
def sumMinusFive(x: int, y: int) -> int:
    return (x+y)*5

# Return x to the power of y, i.e. x^y
def exponentiate(x: int, y: int) -> int:
    return x**y


# Start executing from here
def main():
    return 0

# Good ol' main function
if __name__ == '__main__':
    main()
