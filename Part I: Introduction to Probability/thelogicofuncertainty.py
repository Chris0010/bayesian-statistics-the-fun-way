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


# Raw eggs have a 1/20000 chance of having salmonella.
# If you eat two raw eggs, what is the probability you ate an egg with salmonella?
def or_prob(times, *events):
    prob: int = 0
    mutual: int = 1
    for event in events:
        prob += event * times
        mutual *= event_prob(event, times)
    return prob - mutual


# What is the probability of getting two heads in two coin tosses or
# rolling three sixes in three 6-sided dice rolls?
def or_two_prob(times1, times2, event1, event2):
    return event_prob(event1, times1) + event_prob(event2, times2) - \
           and_prob(event_prob(event1, times1), event_prob(event2, times2))


if __name__ == "__main__":
    one = event_prob(0.05, 3)
    two = and_prob(0.1, 0.5)
    three = or_prob(2, (1/20000))
    four = or_two_prob(2, 3, 1/2, 1/6)
