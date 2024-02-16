import random

class Game:
    def __init__(self) -> None:
        self.sets_P1 = 0
        self.sets_P2 = 0
        self.games_P1 = 0
        self.games_P2 = 0
        self.cambioDeCancha = True
        self.name1 = input("Ingresa el nombre del jugador 1: ")
        self.name2 = input("Ingresa el nombre del jugador 2: ")
        self.player_ball = random.choice([1, 2])
        player = self.name1 if self.player_ball == 1 else self.name2
        print(f"Saque al servicio de {player}")
        
    def print_game(self, points_P1, points_P2):
        points = ["0", "15", "30", "40", "Adv"]
        points_P1_string = points[4] if points_P1 > 3 and points_P2 < points_P1\
            else "40" if points_P1 >= 3 else points[points_P1]
        points_P2_string = points[4] if points_P2 > 3 and points_P1 < points_P2 else\
            "40" if points_P2 >= 3 else points[points_P2]
        
        print(f"{self.name1}: {points_P1_string} points v {self.name2}: {points_P2_string} points")
        
        

    def check_game(self, current_points, opponent_points) -> bool:
        if current_points >= 3 and current_points - opponent_points > 0:
            saque = self.name2 if self.player_ball == 1 else self.name1
            self.player_ball = 2 if self.player_ball == 1 else 1
            print(f"Cambio de Saque a {saque}")
            return True
        return False
    def check_set(self):
        if self.games_P1 >= 6 and self.games_P1 - self.games_P2 >= 2:
            self.sets_P1 = self.sets_P1 + 1
            self.games_P1 = 0
            self.games_P2 = 0
            print(f"Sets:\n{self.name1}: {self.sets_P1} {self.name2}: {self.sets_P2}")
            return
        if self.games_P2 > 0 and self.games_P2 - self.games_P1 >= 2:
            self.sets_P2 = self.sets_P2 + 1
            self.games_P1 = 0
            self.games_P2 = 0
            print(f"Sets:\n{self.name1}: {self.sets_P1} : {self.name2} {self.sets_P2}")
            return
        
    def get_winner_point(self):
        try:
            winner_point = int(input("Quien gano el punto (1/2): "))
            return winner_point    
        except ValueError:
            print("Escribe bien el ganador 1 para jugador1, 2 para jugador2")
            return -1
    def play(self):
        points_P1 = 0
        points_P2 = 0
        
        while self.sets_P1 < 3 and self.sets_P2 < 3:
            if self.games_P1 + self.games_P2 % 2 == 1 and self.cambioDeCancha:
                print("Cambio de cancha")
                self.cambioDeCancha = False
            self.print_game(points_P1, points_P2)
            #winner = random.choice([1,2])
            winner = -1
            while winner != 1 and winner != 2:
                winner = self.get_winner_point()
            if winner == 1:
                game_over = self.check_game(points_P1, points_P2)
                self.games_P1 = self.games_P1 + 1 if game_over else self.games_P1
                points_P1 = points_P1 + 1
            else:
                game_over = self.check_game(points_P2, points_P1)
                self.games_P2 = self.games_P2 + 1 if game_over else self.games_P2
                points_P2 = points_P2 + 1
                
            if game_over:
                print(f"Games:\n{self.name1}: {self.games_P1} {self.name2}: {self.games_P2}")
                self.cambioDeCancha = True
                points_P1 = 0
                points_P2 = 0
        
            self.check_set()
        self.print_game(0, 0)
        winner = self.name1 if self.sets_P1 > self.sets_P2 else self.name2
        print(f"Game Ended. Winner: {winner}")
        
def main():
    game = Game()
    print("Tennis Game")
    game.play()
    return
main()
