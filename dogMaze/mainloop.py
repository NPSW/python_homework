import pygame
import random
import time


class ML:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 450))
        pygame.display.set_caption('dog maze')

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((189, 189, 189))

        self.A = [[False] * 20 for i in range(20)]
        self.Path = []

        self.x = 9
        self.y = 9

        self.help = 0

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def screenBlit(self):
        self.screen.blit(self.background, (0, 0))

        pygame.draw.circle(self.screen, (80, 80, 80), (self.get_x(self.x), self.get_y(self.y)), 10)

        pygame.draw.circle(self.screen, (180, 0, 0), (self.get_x(self.x), self.get_y(self.help)), 8)

        pygame.draw.rect(self.screen, (150, 150, 150), (200, 25, 380, 380), 18)

        if len(self.Path) > 1:
            n = 0
            while n < (len(self.Path) - 1):
                xs = self.get_x(self.Path[n][0])
                ys = self.get_y(self.Path[n][1])
                xf = self.get_x(self.Path[n + 1][0])
                yf = self.get_y(self.Path[n + 1][1])

                pygame.draw.line(self.screen, (80, 80, 80), (xs, ys), (xf, yf), 4)
                n += 1

        pygame.display.flip()

    def refresh(self):
        self.A = [[False] * 20 for i in range(20)]
        self.Path = []

        self.x = 9
        self.y = 9

        self.help = 0

    def get_x(self, a):
        return 200 + (a * 20)

    def get_y(self, a):
        return 25 + (a * 20)

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # ЛОГИКА
            self.Path.append([self.x, self.y])
            self.A[self.x][self.y] = True

            # ОТРИСОВКА
            self.screenBlit()
            time.sleep(0.25)

            if (self.x <= 0) or (self.x >= 19) or (self.y <= 0) or (self.y >= 19):
                time.sleep(1)
                self.refresh()

            elif self.A[self.x - 1][self.y] and self.A[self.x + 1][self.y] and self.A[self.x][self.y - 1] and self.A[self.x][self.y + 1]:
                if self.y == self.help:
                    self.refresh()
                else:
                    self.help += 1

            else:
                while True:
                    r = random.randint(1, 5)

                    if (r == 1) and (not self.A[self.x + 1][self.y]):
                        self.x += 1
                        break
                    if (r == 2) and (not self.A[self.x - 1][self.y]):
                        self.x -= 1
                        break
                    if (r == 3) and (not self.A[self.x][self.y + 1]):
                        self.y += 1
                        break
                    if (r == 4) and (not self.A[self.x][self.y - 1]):
                        self.y -= 1
                        break
