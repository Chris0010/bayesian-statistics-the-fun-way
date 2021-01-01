# What is the probability of rolling 20 three times in a row on a 20-sided die?
def event_prob(prob_one_event, event_occurs):
    return prob_one_event ** event_occurs


# Weather report says there's a 10% chance of rain and you forget your umbrella 50%.
# What is the chance you get caught in the rain without your umbrella?
def and_prob(*events):
    prob = 1
    for event in events:
        prob *= event
    return prob


# Raw eggs have a 1/20000 chance of having or_prob.
# If you eat two raw eggs, what is the probability you ate an egg with or_prob?
def or_prob(times, *events):
    prob: int = 0
    mutual: int = 1
    for event in events:
        prob += event * times
    for event in events:
        mutual *= event ** times
    return prob - mutual


# What is the probability of getting two heads in two coin tosses or
# rolling three sixes in three 6-sided dice rolls?
def coinordice(coin_times, dice_sides, dice_times):
    return ((1/2) ** coin_times) + event_prob(dice_sides, dice_times)


if __name__ == "__main__":
    one = event_prob(0.05, 3)
    two = and_prob(0.1, 0.5)
    three = or_prob(2, (1/20000))
