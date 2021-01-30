# What is the probability of rolling two six-sided dice and getting a value greater than 7?
sides <- c(1:6)
count1 <- 0
for(roll1 in sides){
  for(roll2 in sides){
    count1 <- count1 + ifelse(roll1+roll2 > 7, 1, 0)
  }
}

# What is the probability of rolling three six-sided dice and getting a value greater than 7?
count2 <- 0
for(roll1 in sides){
  for(roll2 in sides){
    for(roll3 in sides){
      count2 <- count2 + ifelse(roll1+roll2+roll3 > 7, 1, 0)
    }
  }
}

# You have to pay $30 if Red Sox win and your friend only pays $5 if they win, what's the assigned probability?
bet1 <- 30
bet2 <- 5
assigned.prob <- ifelse(bet1 > bet2, (bet1 / bet2) / ((bet1 / bet2) + 1), (bet2 / bet1) / ((bet2 / bet1) + 1))
