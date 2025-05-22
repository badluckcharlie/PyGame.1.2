import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 640, 480
ekraan = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snegovik ja Foor – sinu_nimi")

valge = (255, 255, 255)
must = (0, 0, 0)
punane = (255, 0, 0)
kollane = (255, 255, 0)
roheline = (0, 200, 0)
taevasinine = (135, 206, 235)

def joonista_lumemees(ekraan, x, y):
    pygame.draw.circle(ekraan, valge, (x, y + 130), 40)
    pygame.draw.circle(ekraan, valge, (x, y + 70), 30)
    pygame.draw.circle(ekraan, valge, (x, y + 20), 20)
    pygame.draw.circle(ekraan, must, (x - 7, y + 15), 3)
    pygame.draw.circle(ekraan, must, (x + 7, y + 15), 3)
    pygame.draw.polygon(ekraan, (255, 100, 0), [(x, y + 20), (x + 15, y + 23), (x, y + 26)])

def joonista_foor(ekraan, x, y):
    pygame.draw.rect(ekraan, must, (x, y, 40, 120), border_radius=5)
    pygame.draw.circle(ekraan, punane, (x + 20, y + 20), 12)
    pygame.draw.circle(ekraan, kollane, (x + 20, y + 60), 12)
    pygame.draw.circle(ekraan, roheline, (x + 20, y + 100), 12)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ekraan.fill(taevasinine)
    joonista_lumemees(ekraan, 160, 120)
    joonista_foor(ekraan, 460, 180)
    pygame.display.flip()
