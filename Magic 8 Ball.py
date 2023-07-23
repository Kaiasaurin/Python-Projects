import random
import time

def magic_8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    question = input("Ask a question: ")
    time.sleep(1)

    print("Shaking the Magic 8 Ball...")
    time.sleep(1)
    print("Thinking of an answer...")
    time.sleep(2)

    answer = random.choice(responses)

    print("Magic 8 Ball says:", answer)

magic_8_ball()
