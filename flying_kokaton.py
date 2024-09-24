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
    bg_img2 = pg.transform.flip(bg_img,True,False)
    #練習2
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False) #左右反転 P44
    kk_ret = kk_img.get_rect() #練習8　サーフェースからレクとを抽出
    kk_ret.center = 300,200 #練習8-2 初期座標設定

    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()#8-3
        move_x = 0
        move_y = 0
        if not any(key_lst):
            move_x = -1
        if key_lst[pg.K_UP]:
            move_x =-1
            move_y = -1
            #こうかトンの縦座標をー１する
            
        if key_lst[pg.K_DOWN]:
            move_x = -1
            move_y = +1
            
        if key_lst[pg.K_LEFT]:
            move_x = +1
            move_y = +1
            
        if key_lst[pg.K_RIGHT]:
            move_x = +1 *2
            move_y = -1
            #kk_ret.move_ip((+1*2,0))
        kk_ret.move_ip((move_x,move_y))   
            


        x = -(tmr %3200)
        
    #3 スクリーン全体に画像を張り付ける（大きい画像がからはる)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
    #練習4 kk_imgを張り付けている
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img,kk_ret) #練習４→練習8-5
        

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()