try:
    from gtts import gTTS
    import os
except Exception as e:
    print(f"A Error Occour in module importation {e}")

# Function for user to input a stantence and the computer spack otu to them


def inputMode():
    textData = input(
        "Enter The word you want to convert the process file would be save as mp3 in your current directry and the would be plyed by your defualt mp3 player ")

    language = "en"

    output = gTTS(text=textData, lang=language, slow=False)

    output.save("output.mp3")

    os.system("start output.mp3")


def fileMode():
    filename = input(
        "Input the name of the file without .txt just the name and make sure it is stored in the same directry as app.py ")
    filename = filename + ".txt"

    if (os.path.exists(filename)):

        fh = open(filename, "r")

        textData = fh.read().replace("\n", " ")

        language = "en"

        output = gTTS(text=textData, lang=language, slow=False)

        fh.close()

        output.save("output.mp3")
    else:
        print("The file either not be found or is not a text file... MAke sure it is placed in the smae directey with the app.js ")


def application():
    print("Welcome, does you want to convert a text you will type in or do you want to covert a text file to audio ")
    users_choice = input(
        "Enter t if you want to type in the text or f if flie")
    if(users_choice == "t"):
        inputMode()
    elif(users_choice == "f"):
        fileMode()
    else:
        print("Sorry in cannot understand your response")


application()
