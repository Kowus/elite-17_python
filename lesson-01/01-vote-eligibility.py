# Write an algorithm to determine 
# if an individual is eligible to vote
# given that voting age is 18

vote_age = 18

individual = int(input("What is your age? "))

if vote_age < individual:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote. I'll call the cops!!!")