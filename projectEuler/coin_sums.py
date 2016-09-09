"""
Find the number of ways £2 (200p) can be made using any number of coins

Coins:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)

"""

if __name__ == "__main__":
    num_ways = 1 # 1 way with £2 coin

    for one_pound in range(0, 201, 100):
        for fifty_pence in range(0, 201, 50):
            for twenty_pence in range(0, 201, 20):
                for ten_pence in range(0, 201, 10):
                    for five_pence in range(0, 201, 5):
                        for two_pence in range(0, 201, 2):
                            for one_pence in range(0, 201, 1):
                                total = 0
                                total += (one_pound + fifty_pence + 
                                          twenty_pence + ten_pence + five_pence + 
                                          two_pence + one_pence)

                                if total > 200:
                                    break

                                if total == 200:
                                    num_ways += 1

    print(num_ways)
