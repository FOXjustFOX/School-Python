import sys
import pygame


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('i dont know the name for this game')

    def run_game(self):
        run = True
        while run:
            # self.check_events()
            for event in pygame.event.get():
                if event.type == pygame.quit():
                    run = False
                    # sys.exit()
                    # break
            # self.update_screen()

        sys.exit()
    def update_screen(self):
        self.screen.fill(0, 0, 0)
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.quit():
                sys.exit()
                break


if __name__ == '__main__':
    game = Game()
    game.run_game()
