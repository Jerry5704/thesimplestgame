class Meeting:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.starter = Player
        self.result = []

    def start_meeting(self):
        while (0, 0) not in self.result:
            # ToDo: change hardcoded player1 starter
            self.starter = self.set_starter(self.player1)
            self.ask_for_choice()
            self.add_result()
            print(self.result[-1])
        self.add_result_to_points()

    def set_starter(self, starter):
        self.starter = starter

    def get_starter(self):
        return self.starter

    def add_result(self):
        if self.player1.choice == self.player2.choice:
            if self.player1.choice == False:
                self.result.append((0, 0))
            else:
                self.result.append((1, 1))
        else:
            if self.player1.choice == False:
                self.result.append((2, 0))
            else:
                self.result.append((0, 2))

    def add_result_to_points(self):
        for round in self.result:
            self.player1.points += round[0]
            self.player2.points += round[1]

    def ask_for_choice(self):
        if input("Player1 choice [1/0]: ") == "1":
            self.player1.set_choice(True)
        else:
            self.player1.set_choice(False)
        if input("Player2 choice [1/0]: ") == "1":
            self.player2.set_choice(True)
        else:
            self.player2.set_choice(False)

class Player:
    def __init__(self) -> None:
        self.name = str
        self.points = int
        self.choice = bool
    
    def set_name(self, name):
        self.name = name

    def set_points(self, points):
        self.points = points

    def set_choice(self, choice):
        self.choice = choice

    def get_name(self):
        return self.name
    
    def get_points(self):
        return self.points
    
    def get_choice(self):
        return self.choice


def main():
    player1 = Player()
    player1.set_name("Marcin")
    player1.set_points(0)
    
    player2 = Player()
    player2.set_name("Janusz")
    player2.set_points(0)

    meeting = Meeting(player1, player2)
    meeting.start_meeting()
    print(player1.get_points())
    print(player2.get_points())

if __name__ == "__main__":
    main()