import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kt_img = pg.image.load("ex01/fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    kt_img10= pg.transform.rotozoom(kt_img, 10, 1.0)
    kt_img3 = pg.transform.rotozoom(kt_img,3,1.0)
    kt_img7 = pg.transform.rotozoom(kt_img,7,1.0)
    kt_img1 = pg.transform.rotozoom(kt_img,1,1.0)
    kt_img2 = pg.transform.rotozoom(kt_img,2,1.0)
    kt_img4 = pg.transform.rotozoom(kt_img,4,1.0)
    kt_img5 = pg.transform.rotozoom(kt_img,5,1.0)
    kt_img6 = pg.transform.rotozoom(kt_img,6,1.0)
    kt_img8 = pg.transform.rotozoom(kt_img,8,1.0)
    kt_img9 = pg.transform.rotozoom(kt_img,9,1.0)


    kt_imgs = [kt_img1, kt_img2,kt_img3,kt_img4,kt_img5,kt_img6,kt_img7,kt_img8,kt_img9,kt_img10]


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img,[1600-x,0])
        screen.blit(kt_imgs[tmr%10], [300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()