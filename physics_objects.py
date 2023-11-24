import math

import pygame


# ======================================================================================================================


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 2)


# ======================================================================================================================


class Ball:
    def __init__(self, x: float, y: float, radius: float, color: list = (255, 255, 255), velocity: list = (0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = velocity
        self.trace = []

    def update_position(self, gravity=0.1):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        self.velocity[1] += gravity

        self.trace.append((self.x, self.y))
        # if len(self.trace) > 100:
        #     self.trace.pop(0)

    def handle_collision(self, circle: Circle = None, velocity_increase: float = 0):
        circle_center = [circle.x, circle.y]
        circle_radius = circle.radius

        distance = math.sqrt((circle_center[0] - self.x)**2 + (circle_center[1] - self.y)**2)
        if self.radius + distance >= circle_radius:
            # Insure velocity is added in the right direction
            self.velocity[0] += (self.velocity[0] / abs(self.velocity[0])) * velocity_increase
            self.velocity[1] += (self.velocity[1] / abs(self.velocity[1])) * velocity_increase

            # Bounce of the circle object through calculating a vector
            dx = self.x - circle_center[0]
            dy = self.y - circle_center[1]
            normal_length = math.sqrt(dx ** 2 + dy ** 2)
            nx = dx / normal_length
            ny = dy / normal_length

            dot_product = self.velocity[0] * nx + self.velocity[1] * ny
            self.velocity[0] -= 2 * dot_product * nx
            self.velocity[1] -= 2 * dot_product * ny

    def draw(self, screen):
        if len(self.trace) >= 2:
            pygame.draw.lines(screen, self.color, False, self.trace, 1)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


# ======================================================================================================================


ball = Ball(x=2, y=10, radius=10, color="Red", velocity=[1, 0])
