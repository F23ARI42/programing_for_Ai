import random


def game():
    data = [
        {"name": "Neymar", "description": "Footballer", "followers": 210},
        {"name": "Khloé Kardashian", "description": "Reality TV personality", "followers": 310},
        {"name": "Real Madrid CF", "description": "Football club", "followers": 130},
        {"name": "9GAG", "description": "Social media platform", "followers": 60},
        {"name": "Cristiano Ronaldo", "description": "Footballer", "followers": 600},
        {"name": "Instagram", "description": "Social media platform", "followers": 650},
        {"name": "YouTube", "description": "Video platform", "followers": 450},
        {"name": "National Geographic", "description": "Magazine", "followers": 280},
    ]

    score = 0

    while True:
        option_A, option_B = random.sample(data,2)

        print(f"{option_A['name']} ({option_A['description']})")
        print("vs")
        print(f"{option_B['name']} ({option_B['description']})")
        user = input("Who has more followers? (A/B): ").upper()
        correct_choice = "A" if option_A["followers"] > option_B["followers"] else "B"
        if user == correct_choice:
            score += 1
            print(f"Correct! Your score is {score}.")
        else:
            print(f"Wrong choice! Final score: {score}")
            break
game()
