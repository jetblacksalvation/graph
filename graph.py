import pygame 
import random
#make sure that screen ratio is 1 by 1 
screen = 800

graph = [[ random.randrange(screen) for x in range(2)] for f in range(10)]#last one is how many pairs 
connect = [random.randrange(len(graph)) for x in range(len(graph))]

screen=pygame.display.set_mode((800,800))
pygame.init()
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
    
    screen.fill((0,0,0))
    for x in range(len(graph)):
        pygame.draw.line(screen,(255,255,255), (graph[x][0], graph[x][1]), (graph[connect[x]][0], graph[connect[x]][1]))
    
    pygame.display.flip()
