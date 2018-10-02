from colorama import init, Fore
init()

def returnCheck(testFunc, wantedOutput):
    result = testFunc()
    if result == wantedOutput:
        print(Fore.GREEN + "Test has passed - " + str(testFunc()) + " = " + str(wantedOutput))
    else:
        print(Fore.RED + "Test has failed - " + str(testFunc()) + " != " + str(wantedOutput))

