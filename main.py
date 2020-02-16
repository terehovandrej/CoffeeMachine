class CoffeeMachine:
    water_available = 400
    milk_available = 540
    beans_available = 120
    cups_available = 9
    money_available = 550
    state = None
    coffee_type = None
    water_needed = None
    milk_needed = None
    beans_needed = None

    def remaining(self):
        print(f"The coffee machine has:")
        print(f"{self.water_available} of water")
        print(f"{self.milk_available} of milk")
        print(f"{self.beans_available} of coffee beans")
        print(f"{self.cups_available} of disposable cups")
        print(f"{self.money_available} of money")

    def buy(self, water, milk, beans):
        if self.water_available - water < 0:
            print("Sorry, not enough water!")
        elif self.milk_available - milk < 0:
            print("Sorry, not enough milk!")
        elif self.beans_available - beans < 0:
            print("Sorry, not enough coffee beans!")
        elif self.cups_available <= 0:
            print("Sorry, not enough cups!")
        else:
            self.water_available -= water
            self.milk_available -= milk
            self.beans_available -= beans
            self.cups_available -= 1
            print("I have enough resources, making you a coffee!")

    def take(self):
        print(f"I gave you ${self.money_available}")
        self.money_available = 0

    def fill(self):
        added_water = int(input("Write how many ml of water do you want to add: "))
        self.water_available += added_water
        added_milk = int(input("Write how many ml of milk do you want to add: "))
        self.milk_available += added_milk
        added_beans = int(input("Write how many grams of coffee beans do you want to add: "))
        self.beans_available += added_beans
        added_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.cups_available += added_cups

    def action(self, input_data):
        if input_data == 'exit':
            self.state = input_data
        elif input_data == 'remaining':
            self.state = input_data
            self.remaining()

        elif input_data == 'buy':
            self.state = input_data
            self.coffee_type = input("What do you want to buy? 1 - espresso, "
                                     "2 - latte, 3 - cappuccino: 3, back -  to main menu: ")
            if self.coffee_type == "1":
                self.buy(250, 0, 16)
                self.money_available += 4

            elif self.coffee_type == "2":
                self.buy(350, 75, 20)
                self.money_available += 7

            elif self.coffee_type == "3":
                self.buy(200, 100, 12)
                self.money_available += 6
            elif self.coffee_type == "back":
                pass

        elif input_data == 'fill':
            self.fill()

        if input_data == 'take':
            self.state = input_data
            self.take()


machine = CoffeeMachine()

while True:
    machine.action(input('Write action (buy, fill, take, remaining, exit):'))
    if machine.state == 'exit':
        break
