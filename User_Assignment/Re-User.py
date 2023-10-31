
# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:
# first_name
# last_name
# email
# age
# Also include default attributes:
# is_rewards_member - default value of False
# gold_card_points = 0

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    # Methods:

    # display_info(self) - Have this method print all of the users' details on separate lines.
    #* Show Way For A String Identifiying And your Value
    def displayInfo(self):
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Rewards Member: {self.is_rewards_member}')
        print(f'Gold Card Points: {self.gold_card_points}')
        
    # enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    # Ninja Bonuses:
    # Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
    def enroll(self):
        if self.is_rewards_member == True:
            print("Already Member!!!! Cannot RE-ENROLL")
            return False #* NOTE: Could Simply Put "return" (same effect) BUUUUT This is 'SIMPLY' to  tell the coder that the enrollment method was UNSUCCESSFUL
        
        self.is_rewards_member = True
        self.gold_card_points = 200

    # spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spendPoints(self, amount):
        
        if self.gold_card_points < amount:
            print("Aint Got Enough To Spend")
            return
        
        self.gold_card_points -= amount

Fred = User("Fred", "Farkle", "FredFarkle@gmail.com", 37)
Fred.enroll()
Fred.spendPoints(50)
Fred.displayInfo()

print("++++++++++++")

Jimmy = User("Jimmy", "Jeep", "JimmyTheJeep@gmail.com", 54)
Jimmy.enroll()
Jimmy.spendPoints(80)
Jimmy.displayInfo()

print("============")

Phil = User("Phil", "Smith", "PhilSmith@gmail.com", 24)
Phil.enroll()
Phil.spendPoints(40)
Phil.displayInfo()

# Ninja Bonuses:
# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.

# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.