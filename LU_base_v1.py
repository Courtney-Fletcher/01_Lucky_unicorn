# Functions
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

def num_check(question, low, high):

    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid: 
        try:
            response = int(input(question))
            if low < response <= high:
                return response

            else:
                print(error)
        except ValueError:
            print(error)

#Main Routine
played_before = yes_no("Have you played this game before? ")  
print("You chose {}!".format(played_before))

if played_before == "no":
    instructions()

how_much = num_check("How much money would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
