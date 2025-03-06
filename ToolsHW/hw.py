import webbrowser, sys, time, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ERROR_COUNT = 0
def input_math():
    while(1):
        user_input = input("1 times 1 = ? ")
        if user_input == "1": 
            open_video()
            break
        elif user_input.lower() == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")
            ERROR_COUNT += 1
        
def open_video():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
        
if __name__ == "__main__":
    input_math()
