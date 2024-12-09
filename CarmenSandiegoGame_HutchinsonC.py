# Final Project
# Casey Hutchinson
# ITEC 3100
# Due by 12/3/2024

import random

# Step 4) My welcome message greets the user to my mini game, and displays the 3 highest scores. 
# 4.1) It displays when the program starts and again when the game is over
def welcome_message():
    print("Welcome to my 'Where in the World is Carmen Sandiego' game!")
    print("------------------------------------------------------------")
    print("Current High Scores: ")
    show_high_scores()
    print("--------------------------------------------------------")

    # 4.2) The menu gives the user 2 options: start a new game or exit
    while True:
        print("Menu")
        print("1. Play a new game and help find Carmen Sandiego.")
        print("2. Exit, and let Carmen Sandiego escape.")
        choice = input("Please enter a 1 or 2 to make your selection from the options above: ")
        print("\n")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Have a great day.")
            exit()
        else:
            print("Invalid input. Please enter a 1 or 2.")

def play_game():
    print("Thanks for choosing to help me find Carmen Sandiego.")
    player_name = input("First, please tell me your name: ")                  # Step 5.1) variable to store the players name
    print("\n")

    # Basic dialogue to set up the game for the user
    print(f"Thank you Agent {player_name}. Lets begin.")
    print("\n")
    print("___________________________________________________________")
    print("***This is an urgent communinque. Please do not ignore***")
    print(f"Dear agent {player_name},")
    print("Carmen Sandiego has stolen Duke’s helmet, and you need to help track her down using clues about possible destinations she has absconded to with it.")  
    print("You have five days to catch up with her before she gets away.")
    print("***END TRANSMISSION 830.539876***")
    print("\n")

    # Step 1) List of tuples that stores my 15 cities/countries + facts. I decided to use sport related facts for my project
    locations_facts = [("London, England", "Home of the best football (soccer) club in the world. During the 2024/25 football season, they have the opportunity to become the first club to win every major continental honour in their region."),
                       ("Buenos Aires, Argentina", "This city is the capital city of the country that broke the United State's 3-tournament streak of men's basketball gold medals at the Olympics in 2004."),
                       ("Rio de Janeiro, Brazil", "This region of the world has many popular pastimes, but none moreso than football (soccer). This city in particular is home to the youngest player to ever win the award for best player in the world."),
                       ("Cairo, Egypt", "While football (soccer) is the most popular sport in this city and country, squash is the sport where its citizens excel. This city is the location where the men and women representing their country play most of their games. The men currently have 7 of the top 10 ranked players in the world, and the women have 3."),
                       ("Paris, France", "Rugby and football (soccer) remain the most popular sports in this country, but this country is host to the most prestigious cycling competition in the world. The finish line for this event is always located in this city."),
                       ("Athens, Greece", "This city served as the host for the inaugural Olympic games in 1896."),
                       ("Reykjavik, Iceland", "This city is the birthplace of the football (soccer) player considered to be the country's greatest ever athlete. In 2016, he and his country qualified for their first ever major international competition. They defeated an international giant in their last 16 matchup. It is considered one of the biggest upsets in football history."),
                       ("Rome, Italy", "Today, the most popular sports in this country are football (soccer), rugby, and tennis. In previous centuries, the city held 'sporting events' in an arena that is considered one of the most recognizable landmarks in the world."),
                       ("Tokyo, Japan", "Unlike most countries, the most popular sport in this country is a form of wrestling. This particular city annually hosts 3 of the largest tournaments in the world for this form of wrestling."),
                       ("Mexico City, Mexico", "This city is home to what is considered the most famous and iconic stadiums in the world and sits over a mile above sea level. In the world of football (soccer), the stadium is known for having seen the 'Game of the century' and the 'Goal of the century'"),
                       ("Oslo, Norway", "This city has been chosen to host the World Ski Championships 4 times, and is arguably the most popular skiing location in the world. In fact, skiing is the most popular recreational activity in the country."),
                       ("San Marino, San Marino", "Football (soccer) is the most popular sport in this country, and this particular city is home to three professional clubs. Despite the sports popularity, the national team is the lowest ranked-ranked FIFA affiliated national team in the world."),
                       ("Moscow, Russia", "Ice Hockey is the most popular winter sport in this country, and this particular city is the home of the national team. The national team is considered part of the 'Big 6' on the national stage, and have the second most medals in IIHF World Championship history."),
                       ("Istanbul, Turkey", "This city is home to one of the oldest and most recognizable football (soccer) clubs in the world. It was established in 1903, however, it was originally founded as a gymnastics club."),
                       ("New York, United States", "If you live in this country and love sports, then this city is for you. This city is home to 11 professional sports teams across five major sports.")]
    
    # Here is where I set up my rules for the game, how to answer the questions or exit the program, and how I decided to break down the scoring.
    print("____________________________________________________________________________________________________________________________________________________________________")
    print("There isn't a lot of time to catch Carmen Sandiego, but you'll need to do your best.")
    print("You will be given a fact about the City/Country she is currently sighted in, but nothing more.")
    print("You will then need to guess which City/Country she's in based on the options given to you.")
    print("Your answer choices will be 1-5 for each question, but it will be a different fact everytime.")
    print("Each incorrect guess corresponds to 1 day. So for every incorrect guess, you lose a day to catch her.")
    print("You'll be allowed 5 incorrent guesses. However, you lose a day to catch her for each incorrect guess. After 5 incorrect guesses, she escapes...")
    print("If you get 5 correct guesses before you get 5 incorrect, then you will have caught Carmen Sandiego and won the game!")
    print("Each correct guess is worth 10 points. Each incorrect guess takes away 5 points.")
    print("If you get 5 correct answers in a row, the best score you can get is a 50. If you get 5 incorrect answers in a row... your score would be -25. Don't let her escape!")
    print("If at any time you wish to exit the game, simply type 'exit' as your answer choice.")
    print("____________________________________________________________________________________________________________________________________________________________________")
    print("\n")


    correct = 0                     # Step 3) this counter is used to count the number of correct answers by the user
    days = 1                        # Step 5.3.5) counter used when showing where Carmen was on a given day. This doubles as a tracker for incorrect guesses
    sentinel = "exit"               # value entered by the user to exit the game
    total_points = 0                # counter that I used to total up the amount of points scored by the user
         
    incorrect_locations = []        # Step 2 and 5.3.5) this is used to store incorrect guesses so they can be counted
    current_guesses = []            # Step 5.3.4) this stores the users guesses about Carmens location until an incorrect answer is given and is then reset (below)
    correct_guesses = set()         # a set to add the city for correct guesses so that they are not used again in that loop

    # Step 5.2) Main loop of the game. Keeps the game running until one of the conditions is met (detailed below)
    while correct < 5:
        # This list becomes more pertinent as the user plays the game and locations get stored in the correct_guesses set, but this list contains areas that have NOT already been guessed correctly by the user
        remaining_locations = [location for location in locations_facts if location[0] not in correct_guesses]

        # Step 5.3
        # Randomly selects a city/country and its corresponding fact.
        carmen_location = random.choice(remaining_locations)
        city, fact = carmen_location

        # Initializing the location_choices list - starting with the randomly selected location from above. Used a while loop to give the user 5 options
        location_choices = [carmen_location]
        while len(location_choices) < 5:
            # Steps 5.3.1, 5.3.2, and 5.3.3
            # This variable randomly selects a location from the remaining_locations list and checked against the location_choices list to avoid choosing the correct location again or duplicate locations from the remaining list.
            # Once the conditions are satisfied it shuffles the locations list to a random order before display. This helps prevent the correct answer being in the top spot each time.
            other_choices = random.choice(remaining_locations)
            if other_choices [0] != city and other_choices not in location_choices:
                location_choices.append(other_choices)
        random.shuffle(location_choices)
    
        # Displays the fact from the randomly selected location above
        print("The fact about the city Carmen Sandiego is currently sighted in is:")
        print(f"{fact}")
        print("\n")

        # This prints the location options for the user by accessing the location via index of the tuple
        for idx, option in enumerate(location_choices, start=1):
            print(f"{idx}. {option[0]}")

        # The user inputs their guess based on the options given
        try:
            guess = input("Based on the fact above, where is Carmen Sandiego? ")
            print("\n")
        except ValueError:
            print("Invalid input. Please enter a selection from the choices above.")
            print("\n")

        # Step 5.2.1) if the user wants to exit the program they can enter the sentinel value given in the directions above
        if guess == sentinel:
            print("Thank you for playing the game. We'll catch Carmen Sandiego next time.")
            print("\n")
            break

        
        try:
            # Even though I displayed the options to the user starting at 1, I need to convert to zero-index to check them against my list. This guess_index variable does that
            guess_index = int(guess) - 1

            # Here is the check to see if the user guess is correct or incorrect
            if location_choices[guess_index][0] == city:
                correct += 1                                                                # If the user is correct, I add 1 to the correct counter variable above
                total_points += 10                                                          # I also add 10 points to the total_points variable above
                correct_guesses.add(city)                                                   # I add the location to the correct_guesses set
                current_guesses.append(city)                                                # I add the location to the current guesses list for tracking

                # Prints a well done message for correct guesses and tells the users the number of correct guesses they've accumulated after updating the counter
                print(f"Well done Agent {player_name}. That's correct. Total correct guesses so far: {correct}.")
                print("\n")
            else:
                incorrect_locations.append(location_choices[guess_index][0])                # If the user is incorrect, I add the location to the incorrect_locations list so it can be counted           
                total_points -= 5                                                           # I also subtract 5 points from the total_points variable above
                current_day = 5 - days                                                      # Variable to subtract the current day counter from 5. I use this new variable to let the user know how many "days" they have left to find Carmen

                # Prints an incorrect message, then uses the day counter to show the user the locations Carmen visited on that day, before telling them the days remaining
                print(f"Sorry Agent {player_name}, that's incorrect. Total incorrect guesses so far: {days}")
                print(f"On day {days}, Carmen has been to: {'/ '.join(current_guesses)}")
                print(f"You now only have {current_day} incorrect guesses remaining.")
                print("\n")

                # Here I reset the current_guesses list after an incorrect answer, and add one to the day counter
                current_guesses = []
                days += 1
        except (ValueError, IndexError):
            print("Invalid input. Please enter a selection from the choices above.")
            print("\n")

        # Step 5.2.3) This is where the game will stop based on certain parameters. If they get 5 correct guesses, the user is congratulated. 
        # The new_high_scores function takes the users name and point total to add to a txt file and compare them to other high scores
        if correct == 5:
            # Step 5.4
            print(f"Good work Agent {player_name}! That's 5 correct guesses. You've caught Carmen Sandiego and found Duke's stolen helmet!")
            print(f"Agent {player_name}, you've finished the game with a score of {total_points}.")
            new_high_scores(player_name, total_points)
            print("\n")
            break
        # Step 5.2.2) If the user gets 5 incorrect guesses, they are informed that Carmen has escaped. The users name and point total is run through the same new_high_scores function to compare them to other high scores
        elif len(incorrect_locations) == 5:
            # Step 5.4
            print(f"Sorry Agent {player_name}, but that's 5 incorrect guesses. Carmen Sandiego has escaped with Duke's helmet...")
            print(f"Agent {player_name}, you've finished the game with a score {total_points}...")
            new_high_scores(player_name, total_points)
            break

# This function takes the HighScores.txt file and stores it the data in a list called scores that will eventually be called in the next function
def high_scores():
    try: 
        with open("HighScore.txt", "r") as file:
            scores = []
            for line in file:
                name, score = line.split(", ")
                scores.append((name, int(score)))
            return scores
    except FileNotFoundError:
        return []
    
# Step 5.5) Here we take the player_name and total_points variable from the play_game function and pass them through this function    
def new_high_scores(name, new_score):
    scores = high_scores()                                      # returns a list of tuples from the high_scores function
    scores.append((name, new_score))                            # adds the players name and updated score to the list
    scores.sort(key=lambda x: x[1], reverse=True)               # this takes the scores, which is the second element of the tuples, and sorts them in descending order
    top_three = scores[:3]                                      # slicing method takes only the top 3 scores from the scores list

    # This overwrites the previous version of the file with the new top three high scores
    with open("HighScore.txt", "w") as file:
        for score in top_three:
            file.write(f"{score[0]}, {score[1]}\n")

# This is used in the welcome function to display the current top 3 scores to the user
def show_high_scores():
    scores = high_scores()
    for idx, (name, score) in enumerate(scores, start=1):
        print(f"{idx}. {name}: {score} points")


def main():
    welcome_message()

if __name__ == "__main__":
    main()