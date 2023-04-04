from brownianModule import BrownianMotion
import pygame
pygame.init()
Robot = BrownianMotion("red",640/2,640/2,10,2,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    Robot.draw()
    Robot.move()
    Robot.change_direction()
    