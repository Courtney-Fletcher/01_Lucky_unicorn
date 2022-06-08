
def yes_no (question):
    valid = False
    while not valid:
        response = input(question).lower()


        if response =="yes" or response =="y":
            response ="yes"
            return response
        elif response =="no" or response =="n":
            response ="no"
            return response
        else:
            print("Please answer yes / no ") 

def instructions():
    print("How to Play")
    print()
    print("Rules go here")
    print()
    return ""

played_before = yes_no("Have you played this game before? ")  
print("You chose {}!".format(played_before))

if played_before == "no":
    instructions()

print("Program continues")