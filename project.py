import random
import sys


ball = ["It is certain", "It is decidedly so", "Without a doubt", "Yes Definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", " Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
question = input("What question are you seeking to be answered by the mighty 8 ball god?")
print(question)
print(random.choice(ball))
