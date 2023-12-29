import json

class Meeting:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.starter = Player
        self.result = []

    def start_meeting(self):
        while (0, 0) not in self.result:
            print(self.player1.points)
            print(self.player2.points)
            # ToDo: change hardcoded player1 starter
            self.starter = self.set_starter(self.player1)
            self.ask_for_choice()
            self.add_result()
        self.write_to_json()

    def write_to_json(self):
        with open("/home/jerry/thesimplestgame/src/data/players.json", "r") as json_file:       
            json_data = json.load(json_file)
            for player in json_data["players"]:
                if player["id"] == self.player1.id:
                    player["points"] = self.player1.points            
            for player in json_data["players"]:
                if player["id"] == self.player2.id:
                    player["points"] = self.player2.points            
        
        with open("/home/jerry/thesimplestgame/src/data/players.json", "w") as json_file:
            json.dump(json_data, json_file, indent=2)
    
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
                self.result.append((2, -1))
            else:
                self.result.append((-1, 2))
        self.player1.points += self.result[-1][0]
        self.player2.points += self.result[-1][1]

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
    def __init__(self, id):
        self.id = id
        self.player_data = self.get_player_data()
        self.name = self.player_data["name"]
        self.points = self.player_data["points"]
        self.choice = bool
    
    def get_player_data(self):
        with open("/home/jerry/thesimplestgame/src/data/players.json", "r") as players_data_json_file:
            json_data = json.load(players_data_json_file)
            for player in json_data["players"]:
                if player["id"] == self.id:
                    return player
            return {"id": -1, "name": "Jan Pawel Tester", "score": 2137}

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
    player0 = Player(0)
    player1 = Player(1)

    meeting = Meeting(player0, player1)
    meeting.start_meeting()
    meeting.start_meeting()

    print()
    print(player0.name)
    print(player0.points)
    print()
    print(player1.name)
    print(player1.points)
    print()

if __name__ == "__main__":
    main()