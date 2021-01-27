count1 <- 0
for(roll1 in c(1:6)){
  for(roll2 in c(1:6)){
    count1 <- count1 + ifelse(roll1+roll2 > 7, 1, 0)
  }
}

count2 <- 0
for(roll1 in c(1:6)){
  for(roll2 in c(1:6)){
    for(roll3 in c(1:6)){
      count2 <- count2 + ifelse(roll1+roll2+roll3 > 7, 1, 0)
    }
  }
}