from colorama import init, Fore
init()

print("""       TJ's Testing Suite
----------------------------------\n""")

def returnCheck(testFunc, wantedOutput):
    result = testFunc()
    if str(result) == str(wantedOutput):
        print(Fore.GREEN + "Test has passed - " + str(testFunc()) + " = " + str(wantedOutput))
    else:
        print(Fore.RED + "Test has failed - " + str(testFunc()) + " != " + str(wantedOutput))

