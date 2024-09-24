import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    #ゲームタイトル
    pg.display.set_caption("はばたけ！こうかとん")
    #ウィンドウを作成
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    #1 画像を読み込む サーフェース
    bg_img = pg.image.load("fig/pg_bg.jpg")
    #練習2
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False) #左右反転 P44


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr %1600)
    #3 スクリーン全体に画像を張り付ける（大きい画像がからはる)
        screen.blit(bg_img, [-tmr, 0])
    #練習4 kk_imgを張り付けている
        screen.blit(kk_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()