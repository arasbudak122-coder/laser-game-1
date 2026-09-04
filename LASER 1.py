import sys
import pygame

SIYAH = (0, 0, 0)
MAVI = (0, 0, 250)
YESIL = (0, 100, 0)
KIRMIZI = (255, 0, 0)
BEYAZ = (255, 255, 255)

pygame.init()

GENISLIK, YUKSEKLIK = 1024, 768
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("LASER GAME 1")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 50, bold=True)
oyuncu_fonts = pygame.font.SysFont("Arial", 18, bold=True)
skor_font = pygame.font.SysFont("Arial", 28, bold=True)

iz_katmani = pygame.Surface((GENISLIK, YUKSEKLIK))
iz_katmani.set_alpha(40)
iz_katmani.fill(SIYAH)

def oyunu_sifirla():
    karakter = pygame.Rect(100, 100, 50, 50)
    oyuncu_hizi = 20
    karakter_renk = MAVI

    hedef_x = 110.0
    hedef_y = 550.0
    hedef_hizi = 1.5
    hedef = pygame.Rect(int(hedef_x), int(hedef_y), 60, 60)

    baslangic_zamani = pygame.time.get_ticks()
    
    return karakter, oyuncu_hizi, karakter_renk, hedef_x, hedef_y, hedef_hizi, hedef, baslangic_zamani

karakter, oyuncu_hizi, karakter_renk, hedef_x, hedef_y, hedef_hizi, hedef, baslangic_zamani = oyunu_sifirla()

game_over = False
acik = True
dakika = 0
saniye = 0
salise = 0

while acik:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            acik = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x and not game_over:
                if karakter_renk == MAVI:
                    karakter_renk = YESIL
                else:
                    karakter_renk = MAVI

            if game_over and event.key == pygame.K_r:
                karakter, oyuncu_hizi, karakter_renk, hedef_x, hedef_y, hedef_hizi, hedef, baslangic_zamani = oyunu_sifirla()
                game_over = False

    if not game_over:
        gecen_milisaniye = pygame.time.get_ticks() - baslangic_zamani
        toplam_saniye = gecen_milisaniye // 1000
        
        dakika = toplam_saniye // 60
        saniye = toplam_saniye % 60
        salise = (gecen_milisaniye // 10) % 100

        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_w]:
            karakter.y -= oyuncu_hizi
        if tuslar[pygame.K_s]:
            karakter.y += oyuncu_hizi
        if tuslar[pygame.K_a]:
            karakter.x -= oyuncu_hizi
        if tuslar[pygame.K_d]:
            karakter.x += oyuncu_hizi

        if karakter.left < 0:
            karakter.left = 0
        if karakter.right > GENISLIK:
            karakter.right = GENISLIK
        if karakter.top < 0:
            karakter.top = 0
        if karakter.bottom > YUKSEKLIK:
            karakter.bottom = YUKSEKLIK

        if hedef_x < karakter.x:
            hedef_x += hedef_hizi
        elif hedef_x > karakter.x:
            hedef_x -= hedef_hizi

        if hedef_y < karakter.y:
            hedef_y += hedef_hizi
        elif hedef_y > karakter.y:
            hedef_y -= hedef_hizi

        hedef.x = int(hedef_x)
        hedef.y = int(hedef_y)

        hedef_hizi += 0.001

        if karakter.colliderect(hedef):
            game_over = True

    ekran.blit(iz_katmani, (0, 0))

    pygame.draw.rect(ekran, KIRMIZI, hedef)
    pygame.draw.rect(ekran, karakter_renk, karakter, border_radius=8)

    you_yazi = oyuncu_fonts.render("YOU", True, BEYAZ)
    ekran.blit(you_yazi, (karakter.x + 8, karakter.y - 25))

    laser_yazi = oyuncu_fonts.render("LASER", True, BEYAZ)
    ekran.blit(laser_yazi, (hedef.x + 5, hedef.y - 25))

    sure_yazi = skor_font.render(f"SURE: {dakika:02d}:{saniye:02d}:{salise:02d}", True, BEYAZ)
    ekran.blit(sure_yazi, (20, 20))

    if game_over:
        yazi = font.render("GAME OVER", True, BEYAZ)
        restart_yazi = oyuncu_fonts.render("Yeniden Baslamak Icin R'ye Basin", True, BEYAZ)
        ekran.blit(yazi, (250, 240))
        ekran.blit(restart_yazi, (260, 310))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()