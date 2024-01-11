# Importeer pygame, datetime, sys en numpy als de afkorting np
import pygame
import datetime
import sys
import numpy as np
import time
import math
pygame.init() # initialiseert pygame
clock = pygame.time.Clock() # zet clock gelijk aan pygame.time.Clock

# Kleuren
Yellow = (255, 255, 0)
Black = (0, 0, 0)
Gray = (128, 128, 128)

# Lengte en breedte van het scherm
screenWidth = 550
screenHeight = 550

# Definieer het scherm
screen = pygame.display.set_mode((screenWidth, 650))
pygame.display.set_caption("Paused") # verandert de titel van het scherm naar Paused

# Stel de celgrootte en het aantal rijen/kolommen in.
cellSize = 30
numCells = 50
rows, cols = 650 // cellSize, screenWidth // cellSize
# definieer seizoen en grid
grid = np.random.choice([0, 1], size=(rows, cols)) # Genereert een NumPy-array 'grid' met 0'en en 1'en grootte bepaald door variabelen 'rows' en 'cols'
global current_time # Declareer current_time als een globale variabele

# Functie om de tijd in seconden te formatteren als mm:ss
def format_time(milliseconds):
    seconds = milliseconds // 1000 # zet seconds gelijk aan milliseconds gedeeld door 1000
    minutes = seconds // 60 # zet minutes gelijk aan seconds gedeel door 60
    seconds %= 60 # rekent de rest uit van seconds gedeeld door 60
    return f"{minutes:02}:{seconds:02}" # geeft de tijd weer in de vorm mm:ss

# Functie om het speelveld te tekenen
def drawRect():
    for x in range(cols): # checkt welke waarden van x ook in cols zit
        for y in range(rows): # checkt welke waarden van y ook in rows
            if grid[y][x] == 1: # checkt of de cel op positie [x, y] gelijk aan 1
                pygame.draw.rect(screen, Yellow, (x * cellSize, y * cellSize, cellSize, cellSize)) # tekent een geel vierkant
            else:
                pygame.draw.rect(screen, Black, (x * cellSize, y * cellSize, cellSize, cellSize)) # tekent een zwart vierkant
    pygame.display.flip() # update het scherm

# Functie om de volgende generatie te berekenen
def next_generation(curr_gen, iteratie):
    new_gen = np.zeros_like(curr_gen) # maakt een nieuwe array aan(new_gen) die hetzelfde is als curr_gen en is gevuld met nullen.
    global tijdelijke_iteratie
    if iteratie == 0:
        # Dit is de regel 2,234: Lente
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                total_neighbors = np.sum(curr_gen[i - 1:i + 2, j - 1:j + 2]) - curr_gen[i, j]
                if curr_gen[i, j] == 1 and (total_neighbors < 2 or total_neighbors > 4):
                    new_gen[i, j] = 0
                elif curr_gen[i, j] == 0 and total_neighbors == 2:
                    new_gen[i, j] = 1
                else:
                    new_gen[i, j] = curr_gen[i, j]
                tijdelijke_iteratie = tijdelijke_iteratie + 1
                
    if iteratie == 1:
        # Dit is regel 3,23: Zomer (normaal Conway)
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                total_neighbors = np.sum(curr_gen[i-1:i+2, j-1:j+2]) - curr_gen[i, j]
                if curr_gen[i, j] == 1 and (total_neighbors < 2 or total_neighbors > 3):
                    new_gen[i, j] = 0
                elif curr_gen[i, j] == 0 and total_neighbors == 3:
                    new_gen[i, j] = 1
                else:
                    new_gen[i, j] = curr_gen[i, j]
                tijdelijke_iteratie = tijdelijke_iteratie + 1
    if iteratie == 2:
        # Dit is regel 4, 234 : Herfst
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                total_neighbors = np.sum(curr_gen[i-1:i+2, j-1:j+2]) - curr_gen[i, j]
                if curr_gen[i, j] == 1 and (total_neighbors < 2 or total_neighbors > 4):
                    new_gen[i, j] = 0
                elif curr_gen[i, j] == 0 and total_neighbors == 4:
                    new_gen[i, j] = 1
                else:
                    new_gen[i, j] = curr_gen[i, j]
                tijdelijke_iteratie = tijdelijke_iteratie + 1
    if iteratie == 3:
        # Dit is regel 4,23: Winter
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                total_neighbors = np.sum(curr_gen[i-1:i+2, j-1:j+2]) - curr_gen[i, j]
                if curr_gen[i, j] == 1 and (total_neighbors < 2 or total_neighbors > 3):
                    new_gen[i, j] = 0
                elif curr_gen[i, j] == 0 and total_neighbors == 4:
                    new_gen[i, j] = 1
                else:
                    new_gen[i, j] = curr_gen[i, j]
                tijdelijke_iteratie = tijdelijke_iteratie + 1
    return new_gen
# Voer de spelloop uit
def main():
    global grid  # Declareer grid als een globale variabele
    global current_time # Declareer current_time als een globale variabele
    global start_time # Declareer current_time als een globale variabele
    running = True # definieer running als True
    paused = True # definieer paused als True
    start_time = 0 # zet start_time gelijk aan 0
    global iteratie # Declareer iteratie als een globale variabele
    global tijdelijke_iteratie # Declareer tijdelijke_iteratie als een globale variabele
    iteratie = 0 # zet iteratie gelijk aan 0
    tijdelijke_iteratie = 0 # zet tijdelijke_iteratie gelijk aan 0
    

    while running: # checkt of running gelijk is aan True
                
        if not paused: # checkt of paused False 
            print(tijdelijke_iteratie) # schrijft de waarde van tijdelijke_iteratie in de terminal
            if tijdelijke_iteratie == 1520: # checkt of tijdelijke_iteratie gelijk is aan 1280
                iteratie = iteratie + 1 # vergroot iteratie met 1
                tijdelijke_iteratie = 0 # zet tijdelijke_iteratie gelijk aan 0
                # checkt of iteratie groter is dan 3 en zet iteratie gelijk aan 0
                if iteratie > 3: 
                    iteratie = 0 
                
                
            print(iteratie) # schrijft de waarde van iteratie in de terminal
            grid = next_generation(grid, iteratie) # teken de volgende generatie

        # Detecteer wanneer een knop wordt ingedrukt en voer dan de bijbehorende acties uit.
        for event in pygame.event.get():
            # Sluit het programma wanneer er op het kruisje wordt geklikt.
            if event.type == pygame.QUIT:
                running = False # zet running als False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verander de cel waarop geklikt is
                x, y = pygame.mouse.get_pos() # krijg de x, y positie van de muis
                # zet de x, y gelijk aan de x, y van de cel waarop geklikt is
                grid_x = x // cellSize 
                grid_y = y // cellSize
                grid[grid_y][grid_x] = 1 - grid[grid_y][grid_x]  # Wissel tussen 0 en 1
                pygame.draw.rect(screen, Yellow, (x * cellSize, y * cellSize, cellSize, cellSize), 1) # teken een vierkant in de cel waarop je heb geklikt
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # checkt of de spatiebalk is ingedrukt
                    paused = not paused # zet paused naar False
                    if paused: # checkt of paused True is
                        pygame.display.set_caption("Paused") # zet de titel van het scherm(witte balk bovenin) naar Paused
                    else:
                        pygame.display.set_caption("Playing") # zet de titel van het scherm naar PLaying
                        start_time = pygame.time.get_ticks() # zet de start_time gelijk aan het aantal miliseconden vanaf de start van het programma

        # Tijd bijwerken als de klok loopt
        if not paused: # checkt of paused False is
            current_time = pygame.time.get_ticks() - start_time # zet current_time gelijk aan het aantal miliseconden
        else:
            current_time = 0 # zet current_time gelijk aan 0
        
        
        # Tekenen van de tijd op het scherm
        #font = pygame.font.Font(None, 36) # zet de grootte van de font gelijk aan 36
        #time_text = font.render(format_time(current_time), True, Gray) 
        #iteratie_text = font.render(str(iteratie), True, Gray)
        #screen.blit(time_text, (100, 600))
        #screen.blit(iteratie_text, (100, 625))
        pygame.display.flip() # update het scherm
        # Teken het speelveld
        drawRect()

        # Teken lijnen voor rijen/kolommen.
        for i in range(numCells + 1):
            pygame.draw.line(screen, (255, 255, 255), (650, i * cellSize), (0, i * cellSize))
            pygame.draw.line(screen, (255, 255, 255), (i * cellSize, 0), (i * cellSize, 600))

        pygame.display.flip() #  update het scherm
        clock.tick(1)  # Aanpassen van de snelheid van de simulatie
        
# Update de display
    pygame.display.flip()

main()

# Sluit pygame
pygame.quit()
