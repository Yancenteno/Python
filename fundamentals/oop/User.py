class User:
    Display_All_Users = []
    
    def __init__(self, first, last, email, age):
        self.first = first
        self.last = last
        self.email = email
        self.age = age
        self.rewards_member = False
        self.gold_card_points = 0
        User.Display_All_Users.append(self)
    
    def display_info(self):
        print(f'Name : {self.first} {self.last}\nAge : {self.age}\nEmail : {self.email}\nMembership statues : {self.rewards_member}\nGold Card Points : {self.gold_card_points} ')
        print("======================================")
        
    def enroll(self):
        self.rewards_member = True
        self.gold_card_points = 200
        print(f'Congrats you have enrolled and now have {self.gold_card_points} points!')
        print("======================================")        
        if self.rewards_member:
            print("User already a member")
            print("======================================")
            
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough points")
            print("======================================")
            return
        
        self.gold_card_points = self.gold_card_points - amount
        print(f'{self.first}, Gold Card point balance is {self.gold_card_points}!')
        print("======================================")

yancie = User("Yancie", "Centeno", "yancie@gmail.com", 29)
yancie.enroll()
yancie.spend_points(50)

scazz = User("Scazz", "Centeno", "scazz@gmail.com", 21)
scazz.enroll()
scazz.spend_points(80)

nudeMafia = User("NudeMafia", "Centeno", "nudemafia@gmail.com", 22)