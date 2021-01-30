# What is the probability of rolling two six-sided dice and getting a value greater than 7?
def two_dice(sides, num):
    n = 0
    m = 0
    for i in range(1, sides+1):
        for j in range(1, sides+1):
            if i+j > num:
                n += 1
                m = i*j
    return "The probability of two {}-sided dice rolling a value greater than {} is {}/{}".format(sides, num, n, m)


# What is the probability of rolling three six-sided dice and getting a value greater than 7?
def three_dice(sides, num):
    n = 0
    m = 0
    for i in range(1, sides+1):
        for j in range(1, sides+1):
            for k in range(1, sides+1):
                if i+j+k > num:
                    n += 1
                    m = i*j*k
    return "The probability of three {}-sided dice rolling a value greater than {} is {}/{}".format(sides, num, n, m)


# You have to pay $30 if Red Sox win and your friend only pays $5 if they win, what's the assigned probability?
def odds_prob(a_lot, a_little):
    return "The assigned probability is {}/{}".format(int(a_lot / a_little), int(a_lot / a_little + 1))


if __name__ == "__main__":
    two = two_dice(6, 7)
    three = three_dice(6, 7)
    four = odds_prob(30, 5)
