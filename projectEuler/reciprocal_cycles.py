"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its
decimal fraction part
"""

if __name__ == "__main__":
    longest_recurring_n = 0
    max_recurring_length = 0

    for i in range(1, 1000):
        remainders = []
        remainder = 1 % i;
        remainders.append(remainder)

        while remainder != 0:
            remainder = (remainder * 10) % i

            # no recurring cycle
            if remainder == 0:
                break

            recurring_length = 0

            # recurring cycle found
            if remainder in remainders:
                recurring_length = len(remainders[remainders.index(remainder):])
                if recurring_length > max_recurring_length:
                    max_recurring_length = recurring_length
                    longest_recurring_n = i

                break

            remainders.append(remainder)

    print(longest_recurring_n)
