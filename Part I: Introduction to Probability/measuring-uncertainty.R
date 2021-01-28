sides <- c(1:6)
count1 <- 0
for(roll1 in sides){
  for(roll2 in sides){
    count1 <- count1 + ifelse(roll1+roll2 > 7, 1, 0)
  }
}

count2 <- 0
for(roll1 in sides){
  for(roll2 in sides){
    for(roll3 in sides){
      count2 <- count2 + ifelse(roll1+roll2+roll3 > 7, 1, 0)
    }
  }
}

bet1 <- 30
bet2 <- 5
assigned_prob <- ifelse(bet1 > bet2, (bet1 / bet2) / ((bet1 / bet2) + 1), (bet2 / bet1) / ((bet2 / bet1) + 1))
