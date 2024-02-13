import random
#Falta el servicio y el cambio de cancha
class Game:
    def __init__(self) -> None:
        self.sets_P1 = 0
        self.sets_P2 = 0
        self.games_P1 = 0
        self.games_P2 = 0
        
    def print_game(self, points_P1, points_P2):
        points = ["0", "15", "30", "40", "Adv"]
        points_P1_string = points[4] if points_P1 > 3 and points_P2 < points_P1\
            else "40" if points_P1 >= 3 else points[points_P1]
        points_P2_string = points[4] if points_P2 > 3 and points_P1 < points_P2 else\
            "40" if points_P2 >= 3 else points[points_P2]
        
        print(f"Player 1: {points_P1_string} points v Player 2: {points_P2_string} points")
        
        

    def check_game(self, current_points, opponent_points) -> bool:
        if current_points >= 3 and current_points - opponent_points > 0:
            print("Cambio de Saque")
            return True
        return False
    def check_set(self):
        if self.games_P1 >= 6 and self.games_P1 - self.games_P2 >= 2:
            self.sets_P1 = self.sets_P1 + 1
            self.games_P1 = 0
            self.games_P2 = 0
            print(f"Sets:\nPlayer1: {self.sets_P1} Player 2: {self.sets_P2}")
            return
        if self.games_P2 > 0 and self.games_P2 - self.games_P1 >= 2:
            self.sets_P2 = self.sets_P2 + 1
            self.games_P1 = 0
            self.games_P2 = 0
            print(f"Sets:\nPlayer1: {self.sets_P1} Player 2: {self.sets_P2}")
            return
        
        
    def play(self):
        points_P1 = 0
        points_P2 = 0
        
        while self.sets_P1 < 3 and self.sets_P2 < 3:
            if self.games_P1 + self.games_P2 % 2 == 1:
                print("Cambio de cancha")
            self.print_game(points_P1, points_P2)
            winner = random.choice([1,2])
            if winner == 1:
                game_over = self.check_game(points_P1, points_P2)
                self.games_P1 = self.games_P1 + 1 if game_over else self.games_P1
                points_P1 = points_P1 + 1
            else:
                game_over = self.check_game(points_P2, points_P1)
                self.games_P2 = self.games_P2 + 1 if game_over else self.games_P2
                points_P2 = points_P2 + 1
                
            if game_over:
                print(f"Games:\nPlayer1: {self.games_P1} Player 2: {self.games_P2}")

                points_P1 = 0
                points_P2 = 0
        
            self.check_set()
        self.print_game(0, 0)
        winner = "Player 1" if self.sets_P1 > self.sets_P2 else "Player 2"
        print(f"Game Ended. Winner: {winner}")
        
def main():
    game = Game()
    print("Tennis Game")
    game.play()
    return
main()
