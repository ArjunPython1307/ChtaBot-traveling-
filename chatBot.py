import random
destination = {
    "Beach":["Bali","Maldives","Hooket"],
    "Mountains":["Everest","Himalayes","Swiss Alps"],
    "Cities":["Paris","Dubai","Dehi"]
}
tip = ["Kepp extra amount of clothes","Keep all your devices and their chargers paked","Check the wheather forecast"]



def recommend():
    print("Where do you want to go Beaches, Mountains or Cities ?")
    preference = input("Enter your preference?").lower()
    if preference in destination:
        sugesstion = random.choice(destination[preference])
    else:
        print("I don't understand")
def tips():
    print("The tip of the day is",random.choice(tip))

def joke():
    pass

def show_help():
    print("How can I help you ?")
    print("I have some suggestions for traveling spots(Say Recommendation)")
    print("I offer packing tip(Tips)")
    print("Do you want to hear a joke press(Joke)")
    print("To exit(Exit)")

def chat():
    print("I am a traveling CHATBOT")
    name = input("What is your name ?")
    print("Nice to meet you",name)
    show_help()
    while True:
        user_info = input("Enter the information below :").lower()
        if "reccommendation" in user_info:
            recommend()
        elif "tips" in user_info:
            tips()
        elif "joke" in user_info:
            joke()
        elif "exit" in user_info:
            break
        else:
            print("Could you repharse it as I don't understand.")

if __name__ == "__main__":
    chat()