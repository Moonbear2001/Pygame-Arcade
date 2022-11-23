from Game import Game

if __name__ == "__main__":
    print("Running...")
    game = Game()
    while game.running:
        game.game_loop()
