import threading
import pygame

class GameWindow:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.window = pygame.display.set_mode((self.width, self.height))
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.draw.rect(self.window, (255, 0, 0), (0, 0, self.width, self.height))
            pygame.display.update()
        pygame.quit()

def create_window():
    pygame.init()
    game_window = GameWindow()
    game_window.start()

if __name__ == '__main__':
    num_windows = 5
    threads = []
    for i in range(num_windows):
        thread = threading.Thread(target=create_window)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
