"""
The following iterative sequence is defined for the set of positive integers:
        n -> n/2 (n is even)
        n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Find the starting number under one million that produces the longest chain
"""

def next_number(n):
    """ Returns the next number in the collatz sequence """
    if n % 2 == 0: # even
        return int(n/2)
    else:
        return (3*n)+1

if __name__ == "__main__":
    longest_chain_number = 1
    longest_chain_length = 1

    for i in range(2, 1000000):
        chain_length = 1 # chain begins with number itself

        current_value_in_chain = i
        while current_value_in_chain != 1:
            current_value_in_chain = next_number(current_value_in_chain)
            chain_length += 1
        else:
            if chain_length > longest_chain_length:
                longest_chain_length = chain_length
                longest_chain_number = i


    print(longest_chain_number)

