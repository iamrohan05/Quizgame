score = 0
print("Let's start our soccer quiz game 🎮🎮")

playing = input("Do you want to play this game? Yes/No: ")
if playing.lower() == "no":
    print("Exiting the game")
    quit()
else:
    print("Welcome to the game!!")

# Question 1
answer = input("1. Who boasts the most G/A in soccer history? ")
if answer.lower() == "messi":
    print("Correct answer. You get one point.")
    score += 1
else:
    print("Incorrect answer. Now onto the next question.")

# Question 2
answer = input("2. Which country has won the most FIFA World Cups? ")
if answer.lower() == "brazil":
    print("Correct answer. You get one point.")
    score += 1
else:
    print("Incorrect answer. Next question.")

# Question 3
answer = input("3. Who is known as 'CR7'? ")
if answer.lower() == "ronaldo" or answer.lower() == "cristiano ronaldo":
    print("Correct answer. You get one point.")
    score += 1
else:
    print("Incorrect answer. Let's move on.")

# Question 4
answer = input("4. What is the full name of FIFA? ")
if answer.lower() == "federation internationale de football association":
    print("Correct answer. You get one point.")
    score += 1
else:
    print("Incorrect. Let's go to the next.")

# Question 5
answer = input("5. Which club has won the most UEFA Champions League titles? ")
if answer.lower() == "real madrid":
    print("Correct answer. You get one point.")
    score += 1
else:
    print("Incorrect answer. Moving on.")

# Question 6
answer = input("6. Who won the Ballon d'Or in 2023? ")
if answer.lower() == "messi" or answer.lower() == "lionel messi":
    print("Correct again!")
    score += 1
else:
    print("Nope. Next question.")

# Question 7
answer = input("7. What is the name of the soccer stadium in Barcelona? ")
if answer.lower() == "camp nou":
    print("Correct!")
    score += 1
else:
    print("Incorrect. Moving on.")

# Question 8
answer = input("8. Who is England’s all-time top goal scorer? ")
if answer.lower() == "harry kane":
    print("Correct answer. You get one point.")
    score += 1
else:
    print("Wrong. Let's go to the next.")

# Question 9
answer = input("9. In which year did France win their second World Cup? ")
if answer == "2018":
    print("Correct answer.")
    score += 1
else:
    print("Incorrect. Almost done!")

# Question 10
answer = input("10. Which African country made it to the World Cup semi-finals in 2022? ")
if answer.lower() == "morocco":
    print("Correct! Final point earned.")
    score += 1
else:
    print("Incorrect, but good try!")

# Final score
print("Your final score is:", score, "/10")
print("Thanks for playing! ⚽🎉")


