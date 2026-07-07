import cowsay
from pyfiglet import Figlet
from PIL import Image, ImageDraw, ImageFont
import qrcode
import sys


def main():
    header("Tools and game software")
    choice = menu()
    if choice == 1:
        print(qr())
        restart()
    elif choice == 2:
        cow()
        restart()
    elif choice == 3:
        game()
        restart()


# Created to use cool figlet fonts when necessary
def header(word):
    # Done with CS50p's lessons and https://pypi.org/project/pyfiglet/
    figlet = Figlet(width=200)
    h = figlet.renderText(word)
    print(h)
    return f"{word} rendered"


# Helps the program return to the beginning
def restart():
    user_response("Back to main menu?")
    return main()


# Prints main menu and handles user input
def menu():
    # Options
    print("1. QR Generator")
    print("2. CowSay")
    print("3. Astronaut license (game)")

    # Loop to keep prompting the user for the right answer
    while True:
        try:
            n = int(input("Select a number: "))
            if n > 3 or n < 1:
                raise ValueError
            return n
        except ValueError:
            pass


# Can generate qrcodes that contain strings
def qr():
    # Coded with help of https://pypi.org/project/qrcode/
    header("qr generator")
    user_input = input("Input the content of the qr: ")
    image = qrcode.make(user_input)
    try:
        image.save("qr.png", "PNG")
        return f"qr code generated."
    except:
        return f"qr code not generated."


# Generate any animal with the text you want.
def cow():
    # Coded with help of https://pypi.org/project/cowsay/
    header("Cow Say !")
    animals = cowsay.char_names

    print("Available animals", end="\n\n")
    for i, animal in enumerate(animals):
        print(i + 1, animal)

    while True:
        try:
            n = int(input("Select the number of your animal: "))
            if n > len(animals):
                raise ValueError
            animal = animals[n - 1]
            message = input("What do you want to say? ")
            getattr(cowsay, animal)(message)
            return f"generated"
        except ValueError:
            pass


# Become an astronaut game
def game():
    header("Become an astronaut today")
    print("You will play 3 levels")
    print("If you score 7 or higher, you'll get your astronaut license!")
    user_response("Are you ready?")

    # Level 1
    header("Level 1 - Trivia")
    score = 0

    print("1. Who was the first person to walk on the Moon?")
    print_options(1)
    score = score + answer_question("b")

    print("2. What was the first animal in space?")
    print_options(2)
    score = score + answer_question("a")

    print("3. What kind of fuel does a rocket burn?")
    print_options(3)
    score = score + answer_question("c")

    print("4. What does NASA stand for?")
    print_options(4)
    score = score + answer_question("a")

    print("🚀 Your score is:", score)

    # Level 2
    user_response("Ready for level 2? ")
    header("Level 2 - Math Skills")

    print("5. A spaceship travels 20 km on day one and 30 km on day two.\n   How far did it travel in total?")
    print_options(5)
    score = score + answer_question("a")

    print("6. A ship makes 4 orbits every 2 hours. How many in 10 houts?")
    print_options(6)
    score = score + answer_question("b")

    print("7. One astronaut eats 6 meals a day for 5 dats. Total meals ?")
    print_options(7)
    score = score + answer_question("c")

    print("🪐 Your score is:", score)

    # Level 3
    user_response("Ready for level 3? ")
    header("Level 3 - complete the word")
    print("Type the missing letters to complete the word, you have 3 attempts:\n")
    word = ["A", "_", "T", "R", "O", "_", "A", "_", "T"]
    attempt = 0
    while True:
        try:
            print()
            print(''.join(word))
            letter = input("Letter: ").strip().lower()

            if letter == "s" and word[1] == "_":
                word[1] = "S"
                score += 1
            elif letter == "n" and word[5] == "_":
                word[5] = "N"
                score += 1
            elif letter == "u" and word[7] == "_":
                word[7] = "U"
                score += 1
            else:
                attempt += 1
                if attempt != 3:
                    print("Attempts left", 3 - attempt)
                if attempt == 3:
                    print("You've run out of attempts")
                    break

            if word[1] != "_" and word[5] != "_" and word[7] != "_":
                print(''.join(word))
                print("Congratulations! You have completed Level 3 successfully.")
                break
        except ValueError:
            pass

    print("⭐ Your score is:", score)

    if score > 6:
        license()
    elif score < 7:
        print("Score too low | mission failed")
        return f"game over: lost"


# This function stores and prints the options for the questions
def print_options(n):
    n = int(n)

    q1 = ["A. Yuri Gagarin", "B. Neil Armstrong", "C. Buzz Lightyear"]
    q2 = ["A. Dog", "B. Monkey", "C. Cat"]
    q3 = ["A. Gasoline", "B. Diesel", "C. Liquid oxygen"]
    q4 = ["A. National Aeronautics and Space Administration",
          "B. National Astronomy and Science Agency", "C. North American Space Association"]
    q5 = ["A. 50 km", "B. 60 km", "C. 10 km"]
    q6 = ["A. 15", "B. 20", "C. 24"]
    q7 = ["A. 36", "B. 24", "C. 30"]

    if n == 1:
        questions = q1
    elif n == 2:
        questions = q2
    elif n == 3:
        questions = q3
    elif n == 4:
        questions = q4
    elif n == 5:
        questions = q5
    elif n == 6:
        questions = q6
    elif n == 7:
        questions = q7
    else:
        return f"No questions found at {n}"

    for question in questions:
        print(question)

    return f"Questions q{n} printed successfully"


# Keeps prompting the user to get the appropiate input
def answer_question(right_answer):
    while True:
        try:
            answer = input("Answer: ").strip().lower()
            if answer not in ["a", "b", "c"]:
                raise ValueError
            break
        except ValueError:
            pass
    return valid(right_answer, answer)


# This function compares two strings
def valid(right_answer, answer):
    if answer == right_answer:
        print("Correct 😀", end="\n\n")
        return 1
    else:
        print("Incorrect 🙁", end="\n\n")
        return 0


# Asks the user Yes or no questions
def user_response(text):
    while True:
        try:
            res = input(f"{text} [Y/N] ").strip().lower()
            if res in ["y", "yes"]:
                return
            elif res in ["n", "no"]:
                sys.exit("Good bye!")
            else:
                raise ValueError
        except ValueError:
            pass


# Generates an image Licese
def license():
    '''
    Coded with help from:
        https://pillow.readthedocs.io/en/stable/reference/Image.html
        https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#module-PIL.ImageDraw
        https://pillow.readthedocs.io/en/stable/reference/ImageFont.html#module-PIL.ImageFont
    '''
    name = input("What's your name? ")
    img = Image.open("template.PNG").convert("RGBA")
    draw = ImageDraw.Draw(img)

    # Font taken from: https://www.dafont.com/super-squad.font
    if len(name) < 14:
        font = ImageFont.truetype("super.ttf", 40)
    else:
        font = ImageFont.truetype("super.ttf", 20)

    # Positioning text
    width, height = img.size
    x = (width/2) - 80
    y = (height/2) - 70

    # Drawing text in the image
    name = f"Name:\n{name}"
    draw.text((x, y), name, font=font, fill=(255, 255, 255, 255))

    # Generating image
    img.convert("RGB").save("license.PNG")
    print('Your "license.PNG" has been generated.')


if __name__ == "__main__":
    main()
