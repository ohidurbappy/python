from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory


print("Up and down arrow to navigate command history\nCTRL+R to search history")

while 1:
    user_input = prompt('>',
                        history=FileHistory('history.txt'),
                       )
    print(user_input)