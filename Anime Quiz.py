#Python Anime Quiz
from tokenize import endpats

quests = ("In Naruto, what is the name of the nine-tailed fox sealed inside Naruto Uzumaki?",
          "In Death Note, what item must someone have in order to use the Death Note effectively?",
          "Which anime features a boy who turns into a giant humanoid monster?",
          "In My Hero Academia, what is the name of All Might’s ultimate move?",
          "In One Piece, what is the name of the sea where the Grand Line begins?")
opts = (("A. Kurama","B. Shukaku","C. Kyuubi","D. Hachibi"),
        ("A. A red pen","B. A piece of the Death Note","C. The person's real name and face","D. A Shinigami's permission"),
        ("A. Fullmetal Alchemist","B. Bleach","C. Attack on Titan","D. One Piece"),
        ("A. Smash Breaker","B. Texas Smash","C. United States of Smash","D. Detroit Plus Ultra"),
        ("A. Calm Belt","B. East Blue","C. West Blue","D. Reverse Mountain"))
ans = ("A","C","C","C","D")
guesses = []
score = 0
quests_num = 0


for question in quests:
    print("-----------------------------------------------------------------")
    print(question)
    for option in opts[quests_num]:
        print(option)

    guess = input("Choose the correct answer (A-B-C-D): ").upper()
    guesses.append(guess)
    if guess == ans[quests_num]:
        score += 1
        print("Correct answer")
    else:
        print("Incorrect answer")
        print(f"{ans[quests_num]} is the correct answer")
    quests_num += 1


print()
print("---------------------------Results-------------------------------")
print()

print("answer: ",end="")
for answer in ans:
    print(answer, end=" ")
print()

print("guess: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(quests) * 100)
print(f"Your score is: {score}%")
