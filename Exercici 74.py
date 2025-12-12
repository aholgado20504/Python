import pygame
import sys

# Constants
AMPLADA = 800
ALCADA = 600
FPS = 60

RUTA_BASE = "/home/cicles/AO/Tasca11/"
IMG_FONS = RUTA_BASE + "fons.png"
IMG_PALA = RUTA_BASE + "pala.png"
IMG_PILOTA = RUTA_BASE + "pilota.png"
IMG_MAÓ = RUTA_BASE + "mao.png"

COLOR_FONS = (0, 0, 0)

class Pala(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMG_PALA).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (AMPLADA // 2, ALCADA - 30)
        self.velocitat = 7

    def update(self, tecles):
        if tecles[pygame.K_LEFT]:
            self.rect.x -= self.velocitat
        if tecles[pygame.K_RIGHT]:
            self.rect.x += self.velocitat
        # Limitar als marges
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > AMPLADA:
            self.rect.right = AMPLADA

class Pilota(pygame.sprite.Sprite):
    def __init__(self, pala):
        super().__init__()
        self.image = pygame.image.load(IMG_PILOTA).convert_alpha()
        self.rect = self.image.get_rect()
        self.pala = pala
        self.en_joc = False
        self.dx = 4
        self.dy = -4
        self.reset()

    def reset(self):
        self.en_joc = False
        self.rect.centerx = self.pala.rect.centerx
        self.rect.bottom = self.pala.rect.top - 5

    def update(self, maons_group):
        if not self.en_joc:
            # Segueix la pala fins que començam
            self.rect.centerx = self.pala.rect.centerx
            return

        self.rect.x += self.dx
        self.rect.y += self.dy

        # Rebot parets
        if self.rect.left <= 0 or self.rect.right >= AMPLADA:
            self.dx = -self.dx
        if self.rect.top <= 0:
            self.dy = -self.dy

        # Surt per baix -> reset
        if self.rect.top > ALCADA:
            self.reset()

        # Col·lisions amb la pala
        if self.rect.colliderect(self.pala.rect) and self.dy > 0:
            self.dy = -self.dy

        # Col·lisions amb maons
        maons_col = pygame.sprite.spritecollide(self, maons_group, True)
        if maons_col:
            self.dy = -self.dy

class Mao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(IMG_MAÓ).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

def crear_murs(maons_group):
    files = 5
    columnes = 10
    marge_x = 10
    marge_y = 10
    espai_x = 5
    espai_y = 5

    mostra = pygame.image.load(IMG_MAÓ).convert_alpha()
    ample_mao = mostra.get_rect().width
    alt_mao = mostra.get_rect().height

    total_ample = columnes * ample_mao + (columnes - 1) * espai_x
    inici_x = (AMPLADA - total_ample) // 2
    y = 80

    for fila in range(files):
        x = inici_x
        for col in range(columnes):
            ma = Mao(x, y)
            maons_group.add(ma)
            x += ample_mao + espai_x
        y += alt_mao + espai_y

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((AMPLADA, ALCADA))
    pygame.display.set_caption("Arkanoid AO")
    rellotge = pygame.time.Clock()

    # Fons (opcional; si no existeix, pintam color llis)
    try:
        fons = pygame.image.load(IMG_FONS).convert()
    except pygame.error:
        fons = None

    pala = Pala()
    pilota = Pilota(pala)

    tots = pygame.sprite.Group()
    maons = pygame.sprite.Group()
    tots.add(pala)
    tots.add(pilota)
    crear_murs(maons)

    joc_actiu = False  # es comença amb espai

    while True:
        rellotge.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    joc_actiu = True
                    pilota.en_joc = True

        tecles = pygame.key.get_pressed()
        pala.update(tecles)
        if joc_actiu:
            pilota.update(maons)

        # Dibuix
        if fons:
            pantalla.blit(fons, (0, 0))
        else:
            pantalla.fill(COLOR_FONS)

        maons.draw(pantalla)
        tots.draw(pantalla)

        pygame.display.flip()

if __name__ == "__main__":
    main()
