"""
   * Simple esample of co-routine using yield(), send() and exit()
"""


def complain(substring: str) -> None:
    print("Starting up!!!")
    try: # try-except block because exception send by exit()
        while True:
            search = (yield) # Handles values sent by send()
            if substring in search:
                print(f"Oh no, found a {substring}")
    except GeneratorExit: # Handle this exception when exit() is called
            print("Ok Quitting :'(")

