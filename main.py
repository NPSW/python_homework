import pygame
import mainloop


def main():
    # Initialise screen
    pygame.init()
    pygame.font.init()

    MainLoop = mainloop.ML()

    # Event loop
    MainLoop.loop()


if __name__ == '__main__': main()

