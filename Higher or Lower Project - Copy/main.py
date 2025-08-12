import art
import game_data
import random

#Game logo
print(art.logo)

# The user will have a score
user_score = 0
option_a_number = 0
option_b_number = 0

#This function only randomizes option a
def randomize_option_a(the_option_a):
    random_number_a = random.randint(1, 49)

    the_option_a = game_data.data[random_number_a]

    return the_option_a

#This function only randomizes option b
def randomize_option_b(the_option_b):
    random_number_b = random.randint(1, 49)

    the_option_b = game_data.data[random_number_b]

    return the_option_b

# This function randomizes both options
def randomize_options():
    # The user will be given two options to pick whether option A has more followers
    # than option B. The options will be randomized.
    random_number_a = random.randint(1, 49)
    random_number_b = random.randint(1, 49)

    option_a = game_data.data[random_number_a]
    option_b = game_data.data[random_number_b]

    return option_a, option_b

# This function just gives the player info about option A and B
def compare_a_and_b_description(the_option_a, the_option_b):
    print(f"Compare A: {the_option_a["name"]}, a {the_option_a["description"]}, from {the_option_a["country"]}")
    print(art.vs)
    print(f"Against B: {the_option_b["name"]}, a {the_option_b["description"]}, from {the_option_b["country"]}")

# This function calculates the amount of followers and compares both options to see which has the most followers
def compare_a_and_b_calculation(the_option_a, the_option_b, the_user_score):
    while True:
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        if the_option_a["follower_count"] > the_option_b["follower_count"]:
            if user_input == "A":
                the_user_score += 1
                print("\n" * 10)
                print(art.logo)
                print(f"You're right! Current score {the_user_score}")
                the_option_b = randomize_option_b(the_option_b)
                compare_a_and_b_description(the_option_a, the_option_b)
            else:
                print("\n" * 10)
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {the_user_score}")
                break
        else:
            if user_input == "A":
                print("\n" * 10)
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {the_user_score}")
                break
            else:
                the_user_score += 1
                print("\n" * 10)
                print(art.logo)
                print(f"You're right! Current score {the_user_score}")
                the_option_a = the_option_b
                the_option_b = randomize_option_b(the_option_b)

                compare_a_and_b_description(the_option_a, the_option_b)


# If option A has more followers than option B, then it is the right pick, otherwise
# it is option B

# If the user gets it wrong then it is Game Over and the game demonstrates final score
rand_number = randomize_options()

instagram_user_a = rand_number[0]
instagram_user_b = rand_number[1]

compare_a_and_b_description(the_option_a=instagram_user_a, the_option_b=instagram_user_b)
compare_a_and_b_calculation(the_option_a=instagram_user_a, the_option_b=instagram_user_b, the_user_score=user_score)