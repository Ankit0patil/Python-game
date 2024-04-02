"""# Python quiz game with difficulty levels

class QuizLevel:
    def __init__(self, questions, options, answers):
        self.questions = questions
        self.options = options
        self.answers = answers

easy_questions = (
    "What is the square root of 144?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are there in the human body?: ",
    "Who is known as the father or modern physics ?: ",
    "How many continents are there on Earth?: ",
    "Who painted the Mona Lisa?:"
)
easy_options = (
    ("A. 12", "B. 14", "C. 16", "D. 18"),
    ("A. Whale", "B. Anaconda", "C. Duck", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 300", "D. 209"),
    ("A. Thomas Edison", "B. Albeit Einstein", "C. Nikola Tesla", "D. Isac Newton"),
    ("A. 9", "B. 6", "C. 8", "D. 7"),
    ("A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Michelangelo")
)
easy_answers = ("A", "D", "A", "A", "B", "D", "A")

medium_questions = (
    "Which planet in the solar system is the hottest?: ",
    "What is the chemical symbol for gold?: ",
    "What is the capital of Australia?: ",
    "What is the largest ocean on Earth?: ",
    "Who was the second person to step on moon ?: ",
    "Which is the only metal that is liquid at room temperature?: ",
    "How many elements are there in the periodic table?: "
)
medium_options = (
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
    ("A. Au", "B. Ag", "C. Cu", "D. Fe"),
    ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"),
    ("A. Pacific", "B. Atlantic", "C. Indian", "D. Arctic"),
    ("A. Neil Armstrong", "B. Alan Bean", "C. Buzz Aldrin", "D. Edgar Mitchell"),
    ("A. Silver", "B. Mercury", "C. Gold", "D. Iron"),
    ("A. 116", "B. 117", "C. 118", "D. 119")
)
medium_answers = ("B", "A", "C", "A", "C", "B", "C")

hard_questions = (
    "What is the powerhouse of the cell ?: ",
    "How many people have landed on moon?: ",
    "Who wrote the play "Romeo and Juliet"?: ",
    "What is the largest mammal in the world?: ",
    "In which year did the Titanic sink?: ",
    "What is the chemical symbol for element lead: ",
    "Which instrument is used to measure earthquakes?: "
)
hard_options = (
    ("A. White Blood Cell", "B. Chloroplast", "C. Ribosomes", "D. Mitochodria"),
    ("A. 8", "B. 12", "C. 9", "D. 14"),
    ("A. J.K.Rowling", "B. Mark Twain", "C. George Orwell", "D. William Shakespeare"),
    ("A. Blue whale", "B. African elephant", "C. Giraffe", "D. Polar bear"),
    ("A. 1912", "B. 1914", "C. 1916", "D. 1918"),
    ("A. Sb", "B. Ld", "C. Pb", "D. Tn"),
    ("A. Barometer", "B. Seismograph", "C. Hygrometer", "D. Altimeter")
)
hard_answers = ("D", "B", "D", "A", "A", "C", "B")

# Initialize levels
easy_level = QuizLevel(easy_questions, easy_options, easy_answers)
medium_level = QuizLevel(medium_questions, medium_options, medium_answers)
hard_level = QuizLevel(hard_questions, hard_options, hard_answers)

def play_level(level):
    guesses = []
    score = 0
    question_num = 0

    print("Welcome to the Quiz! Let's start.")
    print("Enter the letter corresponding to your answer (A, B, C, or D).")

    for question in level.questions:
        print("----------------")
        print(question)
        for option in level.options[question_num]:
            print(option)

        guess = input("Your answer: ").upper()
        guesses.append(guess)
        if guess == level.answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"The correct answer is: {level.answers[question_num]}")
        question_num += 1

    print("----------------")
    print("   RESULT    ")
    print("----------------")

    print("Answers: ", end="")
    for answer in level.answers:
        print(answer, end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score_percentage = int(score / len(level.questions) * 100)
    print(f"Your score is: {score_percentage}%")

# Play the game
play_level(easy_level)
play_level(medium_level)
play_level(hard_level)
"""

# Python quiz game with difficulty levels

class Quizgame:
    def __init__(self, questions, options, answers):
        self.questions = questions
        self.options = options
        self.answers = answers

easy_questions = (
    "What is the square root of 144?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are there in the human body?: ",
    "Who is known as the father or modern physics ?: ",
    "How many continents are there on Earth?: ",
    "Who painted the Mona Lisa?:"
)
easy_options = (
    ("A. 12", "B. 14", "C. 16", "D. 18"),
    ("A. Whale", "B. Anaconda", "C. Duck", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 300", "D. 209"),
    ("A. Thomas Edison", "B. Albert Einstein", "C. Nikola Tesla", "D. Isaac Newton"),
    ("A. 9", "B. 6", "C. 8", "D. 7"),
    ("A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Michelangelo")
)
easy_answers = ("A", "D", "A", "A", "B", "D", "A")

medium_questions = (
    "Which planet in the solar system is the hottest?: ",
    "What is the chemical symbol for gold?: ",
    "What is the capital of Australia?: ",
    "What is the largest ocean on Earth?: ",
    "Who was the second person to step on moon ?: ",
    "Which is the only metal that is liquid at room temperature?: ",
    "How many elements are there in the periodic table?: "
)
medium_options = (
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
    ("A. Au", "B. Ag", "C. Cu", "D. Fe"),
    ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"),
    ("A. Pacific", "B. Atlantic", "C. Indian", "D. Arctic"),
    ("A. Neil Armstrong", "B. Alan Bean", "C. Buzz Aldrin", "D. Edgar Mitchell"),
    ("A. Silver", "B. Mercury", "C. Gold", "D. Iron"),
    ("A. 116", "B. 117", "C. 118", "D. 119")
)
medium_answers = ("B", "A", "C", "A", "C", "B", "C")

hard_questions = (
    "What is the powerhouse of the cell ?: ",
    "How many people have landed on moon?: ",
    "Who wrote the play 'Romeo and Juliet'?: ",
    "What is the largest mammal in the world?: ",
    "In which year did the Titanic sink?: ",
    "What is the chemical symbol for element lead: ",
    "Which instrument is used to measure earthquakes?: "
)
hard_options = (
    ("A. White Blood Cell", "B. Chloroplast", "C. Ribosomes", "D. Mitochondria"),
    ("A. 8", "B. 12", "C. 9", "D. 14"),
    ("A. J.K.Rowling", "B. Mark Twain", "C. George Orwell", "D. William Shakespeare"),
    ("A. Blue whale", "B. African elephant", "C. Giraffe", "D. Polar bear"),
    ("A. 1912", "B. 1914", "C. 1916", "D. 1918"),
    ("A. Sb", "B. Ld", "C. Pb", "D. Tn"),
    ("A. Barometer", "B. Seismograph", "C. Hygrometer", "D. Altimeter")
)
hard_answers = ("D", "B", "D", "A", "A", "C", "B")

# Initialize levels
easy_level = Quizgame(easy_questions, easy_options, easy_answers)
medium_level = Quizgame(medium_questions, medium_options, medium_answers)
hard_level = Quizgame(hard_questions, hard_options, hard_answers)

def play_level(level):
    guesses = []
    score = 0
    question_num = 0

    print("Welcome to the Quiz! Let's start.")
    print("Enter the letter corresponding to your answer (A, B, C, or D).")

    for question in level.questions:
        print("----------------")
        print(question)
        for option in level.options[question_num]:
            print(option)

        guess = input("Your answer: ").upper()
        guesses.append(guess)
        if guess == level.answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"The correct answer is: {level.answers[question_num]}")
        question_num += 1

    print("----------------")
    print("   RESULT    ")
    print("----------------")
    

    print("Answers: ", end="")
    for answer in level.answers:
        print(answer, end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score_percentage = int(score / len(level.questions) * 100)
    print(f"Your score is: {score_percentage}%")
    return score_percentage

# Play the game
print("===== Easy Level =====")
easy_score = play_level(easy_level)
exit_option = input("Do you want to exit the game? (yes/no): ")
if exit_option.lower() == "yes":
    print("Exiting the game...")
    exit()
    
print("===== Medium Level =====")
medium_score = play_level(medium_level)
exit_option = input("Do you want to exit the game? (yes/no): ")
if exit_option.lower() == "yes":
    print("Exiting the game...")
    exit()

print("===== Hard Level =====")
hard_score = play_level(hard_level)

# Calculate total score
total_percentage = (easy_score + medium_score + hard_score) / 3
print("===== Final Score =====")
print(f"Total Score: {total_percentage}%")
print("THANKS FOR PLAYING THE GAME !!!")