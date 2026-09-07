import sys, os, random
import pygame

KLASOR_YOLU = os.path.dirname(os.path.abspath(__file__))
RESIM_YOLU = os.path.join(KLASOR_YOLU, "ssa.jpg")
A1 = os.path.join(KLASOR_YOLU, "a1.jpg")
ARKAPLAN_YOLU = os.path.join(KLASOR_YOLU, "arkapl.jpg")

SIYAH = (0, 0, 0)
MAVI = (0, 0, 250)
YESIL = (0, 100, 0)
KIRMIZI = (255, 0, 0)
BEYAZ = (255, 255, 255)

pygame.init()
lazer_isigi = pygame.Surface((100, 100), pygame.SRCALPHA)
pygame.draw.circle(lazer_isigi, (255, 0, 0, 70), (50, 50), 45)
GENISLIK, YUKSEKLIK = 1024, 768
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("LASER GAME 1.2")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 50, bold=True)
oyuncu_fonts = pygame.font.SysFont("Arial", 18, bold=True)
skor_font = pygame.font.SysFont("Arial", 28, bold=True)

oyuncu_resmi = pygame.image.load(RESIM_YOLU)
oyuncu_resmi = pygame.transform.scale(oyuncu_resmi, (50, 50))

lazer_resmi = pygame.image.load(A1)
lazer_resmi = pygame.transform.scale(lazer_resmi, (60, 60))

arkaplan_resmi = pygame.image.load(ARKAPLAN_YOLU)
arkaplan_resmi = pygame.transform.scale(arkaplan_resmi, (GENISLIK, YUKSEKLIK))

LAZER_MESAJLARI = [
    "BRO İ WİLL CATCH YOU!!",
    "NO RUN!!",
    "COME!!"
]

def oyunu_sifirla():
    karakter = pygame.Rect(100, 100, 50, 50)
    oyuncu_hizi = 20
    karakter_renk = MAVI

    hedef_x = 110.0
    hedef_y = 550.0
    hedef_hizi = 1.5
    hedef = pygame.Rect(int(hedef_x), int(hedef_y), 60, 60)

    baslangic_zamani = pygame.time.get_ticks()
    son_mesaj_zamani = baslangic_zamani
    aktif_mesaj = ""
    
    return karakter, oyuncu_hizi, karakter_renk, hedef_x, hedef_y, hedef_hizi, hedef, baslangic_zamani, son_mesaj_zamani, aktif_mesaj

karakter, oyuncu_hizi, karakter_renk, hedef_x, hedef_y, hedef_hizi, hedef, baslangic_zamani, son_mesaj_zamani, aktif_mesaj = oyunu_sifirla()

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
                karakter, oyuncu_hizi, karakter_renk, hedef_x, hedef_y, hedef_hizi, hedef, baslangic_zamani, son_mesaj_zamani, aktif_mesaj = oyunu_sifirla()
                game_over = False

    if not game_over:
        su_anki_zaman = pygame.time.get_ticks()
        gecen_milisaniye = su_anki_zaman - baslangic_zamani
        toplam_saniye = gecen_milisaniye // 1000
        
        dakika = toplam_saniye // 60
        saniye = toplam_saniye % 60
        salise = (gecen_milisaniye // 10) % 100

        # Her 5 saniyede bir yeni mesaj secilir
        if su_anki_zaman - son_mesaj_zamani >= 5000:
            aktif_mesaj = random.choice(LAZER_MESAJLARI)
            son_mesaj_zamani = su_anki_zaman

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

    ekran.blit(arkaplan_resmi, (0, 0))

    ekran.blit(lazer_resmi, (hedef.x, hedef.y))
    ekran.blit(oyuncu_resmi, (karakter.x, karakter.y))

    you_yazi = oyuncu_fonts.render("YOU", True, SIYAH)
    ekran.blit(you_yazi, (karakter.x + 8, karakter.y - 25))

    laser_yazi = oyuncu_fonts.render("LASER", True, SIYAH)
    ekran.blit(laser_yazi, (hedef.x + 5, hedef.y - 25))

    if aktif_mesaj and not game_over:
        konusma_yazi = oyuncu_fonts.render(aktif_mesaj, True, KIRMIZI)
        ekran.blit(konusma_yazi, (hedef.x - 20, hedef.y - 45))

    sure_yazi = skor_font.render(f"Time: {dakika:02d}:{saniye:02d}:{salise:02d}", True, SIYAH)
    ekran.blit(sure_yazi, (20, 20))

    if game_over:
        yazi = font.render("GAME OVER", True, SIYAH)
        restart_yazi = oyuncu_fonts.render("If you play restart The Game Press 'R'", True, SIYAH)
        GG_yazi = oyuncu_fonts.render("GG! BRO YOU ARE SO BADD", True, (255, 0, 0))
        ekran.blit(GG_yazi, (hedef.x + 10, hedef_y - 50))
        ekran.blit(yazi, (250, 240))
        ekran.blit(restart_yazi, (260, 310))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()
