from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory


print("Provides auto suggestion and history support. ctrl+r to search for history")

while 1:
    user_input = prompt('>',
                        history=FileHistory('history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                       )
    print(user_input)