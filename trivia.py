import random

#2D Arrays containing Questions and Answers
MATH_QA = [["What is the square root of 49?", "7"], ["What is 10 x 15?", "150"],
["Given that a^2 + 4^2 = 52, what is the value of a?", "6"],
["Combine the following terms: 12a + 26b -4b – 16a", "-4a + 22b"],
["What is |-26|?", "26"],
["What is the radius of a circle that has a circumference of 3.14 meters?", "0.5 meter"],
["Simplify the following: (4 – 5) – (13 – 18 + 2)", "2"],
["What is the least common multiple of 2 and 4?", "4"]]

SCI_QA =[["What is the atomic number of carbon?", "6"],
["What temperature in celsius is equal to absolute 0?", "273 celsius"],
["What keeps the planets orbiting around the sun?", "gravity"],
["What planet is farthest away from the sun?", "Neptune"],
["What is the largest organ in the human body?", "the skin"],
["What is the largest bone in the human body?", "the femur"],
["What is the smallest unit of matter?", "atom"],
["What are the 4 states of matter?", "solid, liquid, gas, plasma"]]

HIST_QA = [["When was the Declaration of Independence signed?", "August 2, 1776"],
["When did the Revolutionary War end?", "September 3, 1783"],
["When was the first U.S. dollar printed?", "1862"],
["Who was the Confederate president during the Civil War?", "Jefferson Davis"],
["Who was the first United States president to appear on television?", "Franklin D. Roosevelt"],
["Which branch of the military did President John F. Kennedy serve in?", "United States Navy"],
["What year did Apple Computer introduce the first iPod?", "2001"],
["Who was the first Black president?", "Barack Obama"]]

GEO_QA = [["What is the smallest country in the world?", "Vatican City"],
["True or False: there are no deserts in Europe.", "true"],
["How many countries are inside the United Kingdom?", "4"],
["What country has the abbreviation CH?", "Switzerland"],
["Where is the historical city of Timbuktu located?", "Mali"],
["What is the largest state in the US, by area?", "Alaska"],
["What would you call someone from Sudan?", "Sudanese"],
["What is the state capital of New York?", "Albany"]]

SPORTS_QA = [["Which soccer club has the most UFEA Champions League trophies?", "Real Madrid CF"],
["Which soccer player has the greatest number of player of the year awards?", "Lionel Messi"],
["Who is the undefeated and undisputed champion of the UFC lightweight divison?", "Khabib Nurmagomedov"],
["How many wins did Muhammad Ali have as an amateur boxer?", "100"],
["Of his first 19 professional bouts, how many did Muhammad Ali win by KO?", "15"],
["What college did Michael Jordan attend?", "University of North Carolina"],
["Who is the only player to score 100 points in a single basketball game?", "Wilt Chamberlain"],
["What player has the most super bowl rings in NFL history?", "Tom Brady"]]

#Points variable keeps track of score
POINTS = 0

#These functions select questions
def math_question():
    random.shuffle(MATH_QA)

    answer = MATH_QA[0][1]
    question = MATH_QA[0][0]

    your_answer = input("Question: " + question + " \n")

    if your_answer == answer:
        print("Correct! \n")

        global POINTS
        POINTS += 1
    else:
        print("Sorry... that is not correct. \n")

    MATH_QA.pop(0)

def sci_question():
    random.shuffle(SCI_QA)

    answer = SCI_QA[0][1]
    question = SCI_QA[0][0]

    your_answer = input("Question: " + question + " \n")

    if your_answer == answer:
        print("Correct! \n")

        global POINTS
        POINTS += 1
    else:
        print("Sorry... that is not correct. \n")

    SCI_QA.pop(0)

def hist_question():
    random.shuffle(HIST_QA)

    answer = HIST_QA[0][1]
    question = HIST_QA[0][0]

    your_answer = input("Question: " + question + " \n")

    if your_answer == answer:
        print("Correct! \n")

        global POINTS
        POINTS += 1
    else:
        print("Sorry... that is not correct. \n")

    HIST_QA.pop(0)

def geo_question():
    random.shuffle(GEO_QA)

    answer = GEO_QA[0][1]
    question = GEO_QA[0][0]

    your_answer = input("Question: " + question + " \n")

    if your_answer == answer:
        print("Correct! \n")

        global POINTS
        POINTS += 1
    else:
        print("Sorry... that is not correct. \n")

    GEO_QA.pop(0)

def sports_question():
    random.shuffle(SPORTS_QA)

    answer = SPORTS_QA[0][1]
    question = SPORTS_QA[0][0]

    your_answer = input("Question: " + question + " \n")

    if your_answer == answer:
        print("Correct! \n")

        global POINTS
        POINTS += 1
    else:
        print("Sorry... that is not correct. \n")

    SPORTS_QA.pop(0)

if __name__ == '__main__':
    number_of_questions = 0

    print("\nWelcome to Trivia.py! \n\n")
    print("Rules \n")
    print("There will be 25 questions, and each question will be worth 1 point. Answers ARE case sensitive \n")
    print("In order to win, you must get at least 15 out of the 25 questions correct! \n\n")
    print("Good luck! \n\n")

    while number_of_questions < 25:
        question_type = random.randint(0, 4)

        if question_type == 0:
            math_question()
        elif question_type == 1:
            sci_question()
        elif question_type == 2:
            hist_question()
        elif question_type == 3:
            geo_question()
        elif question_type == 4:
            sports_question()

        number_of_questions += 1

    print("Your score is: " + str(POINTS) + "/25 \n")

    if POINTS > 14:
        print("GAME OVER... YOU. HAVE. WON! \n\n")
    else:
        print("GAME OVER... YOU. HAVE. LOST...\n\n")
