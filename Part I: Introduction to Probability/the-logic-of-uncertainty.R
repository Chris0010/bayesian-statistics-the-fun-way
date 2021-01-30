# What is the probability of rolling 20 three times in a row on a 20-sided die?
sides <- 20
times <- 3
event.prob <- (1/sides)^times

# Weather report says there's a 10% chance of rain and you forget your umbrella 50%.
# What is the chance you get caught in the rain without your umbrella?
rain.prob <- 0.1
umb.prob <- 0.5
rain.no.umb <- rain.prob*umb.prob

# Raw eggs have a 1/20000 chance of having salmonella.
# If you eat two raw eggs, what is the probability you ate an egg with salmonella?
times <- 2
prob <- 1/20000
salm.prob <- (prob*times)-prob^times

# What is the probability of getting two heads in two coin tosses or
# rolling three sixes in three 6-sided dice rolls?
coin.prob <- 1/2
dice.prob <- 1/6
rolls <- 3
flips <- 2
heads.sixes <- coin.prob^flips+dice.prob^rolls-coin.prob^flips*dice.prob^rolls
