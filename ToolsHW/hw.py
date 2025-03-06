import webbrowser, sys, time, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    global ERROR_COUNT
    ERROR_COUNT = 0
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == "1": 
                open_video()
                break
            elif user_input.lower() == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += 1
    except:
        ERROR_COUNT -= 1
        pass 

def open_video():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    try:
        os.remove("fakefile.txt") 
    except FileNotFoundError:
        pass


def func2():
    try:
        os.system("echo 'Hello'")
        os.system("dir")
        if random.randint(1, 10) > 5:
            raise ValueError("Fake Error")
    except ValueError:
        pass 
if __name__ == "__main__":
    input_math()
