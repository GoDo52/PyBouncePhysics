import pygame
import sys
from physics_objects import Ball, Circle


# ======================================================================================================================


pygame.init()


# ======================================================================================================================


width, height = 1960, 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Physics Simulation")


ball = Ball(x=width // 2, y=height // 2, radius=0, color=[255, 0, 0], velocity=[1, 1])
circle = Circle(x=width // 2, y=height // 2, radius=300, color=(0, 0, 0))


# ======================================================================================================================


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Simulate constant velocity
    ball.update_position()
    ball.handle_collision(circle=circle, velocity_increase=0)

    # Draw the ball
    screen.fill((255, 255, 255))
    ball.draw(screen)
    circle.draw(screen)
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(180)
