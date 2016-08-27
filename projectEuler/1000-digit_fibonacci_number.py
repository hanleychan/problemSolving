"""
Find the index of the first item in the Fibonacci sequence to contain 1000 digits
"""

if __name__ == "__main__":
    fibonacci = [1,1]

    # keep calculating the next fibonacci # n the sequence starting from the 3rd number
    index = 3
    while True:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        if len(str(fibonacci[-1])) >= 1000:
            break
        index += 1

    print(index)
