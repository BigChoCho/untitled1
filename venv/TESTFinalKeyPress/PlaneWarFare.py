import tkinter
import time
import random as rd
#自訂包
import config
import mover
import sky
import bigplane
import smallplane
import bee as honeybee
import hero as heroplane
import bullet

# 创建天空背景
#root跟canvas由start_game至点击界面开始游戏的root_window, window_canvas接收而來
def create_sky(root, canvas):
    #傳入依序為(窗口,桌布,SE東南,窗口寬,窗口長,標籤)
    # sky_1.nw[0], sky_1.nw[1]為sky_1第一張圖左上的座標,分別為(0,-252)此為圖像座標
    sky_1 = sky.Sky(root, canvas,
                    config.initial_anchor_sky_1,
                    config.initial_anchor_sky_x_1,
                    config.initial_anchor_sky_y_1, "Sky01")
    #傳入依序為(窗口,桌布,SW西南,窗口寬,窗口長,標籤)

#獲取 sky_1.nw[0], sky_1.nw[1],轉為窗寬高,以SW判斷獲取座標,並與窗寬高進行運算得sky_2.nw
    #判斷sky_2圖片會高於sky_1
    sky_2 = sky.Sky(root, canvas, tkinter.SW, sky_1.nw[0], sky_1.nw[1], "Sky02")
    print("SKY1:PlaneWarFare.py,22", sky_1.nw[0], sky_1.nw[1])
    print("PlaneWarFare.py,23",sky_2.nw[0],sky_2.nw[1])
#繪製圖(放置圖片座標 窗寬,窗長,錨定SE東南,圖片地址,圖標籤(Sky01)
    tmp_canvas_img = canvas.create_image(sky_1.anchor_x,
                                         sky_1.anchor_y,
                                         anchor=sky_1.anchor,
                                         image=sky_1.bg_image,
                                         tags=sky_1.bg_image_tags)
    print("PlaneWarFare.py 29",sky_1.anchor_x,sky_1.anchor_y)
    #傳入已設置圖片至Move.py的set_canvas_image方法
    sky_1.set_canvas_image(tmp_canvas_img)
    #繪製圖(窗口寬高  sky_1.nw[0], sky_1.nw[1] ,SW西南,同樣圖址,Sky02)
    tmp_canvas_img = canvas.create_image(sky_2.anchor_x,
                                         sky_2.anchor_y,
                                         anchor=sky_2.anchor,
                                         image=sky_2.bg_image,
                                         tags=sky_2.bg_image_tags)
    print("PlaneWarFare.py 38",sky_2.anchor_x,sky_2.anchor_y)
    print("SKY2:PlaneWarFare.py,40", sky_2.nw[0], sky_2.nw[1])

    sky_2.set_canvas_image(tmp_canvas_img)
    print("PlaneWarFare.py 41", sky_1, sky_2)
    return [sky_1, sky_2]
 #移动天空，模拟前行
def move_sky(canvas, sky_1, sky_2):
    # 若sky_1已消失在窗口范围后，从重新移动到sky_2的上方

    #獲取左上角座標匹配,窗口 -10
    if sky_1.nw[1] >= config.window_boundary_row - sky_1.steps[1]:
        #偏移(標籤,x,-圖片高度+窗口高-10:即將消失在窗口前的座標)
        canvas.move(sky_1.bg_image_tags, 0, -(config.image_sky_height + sky_1.nw[1]))
        #傳入更新座標函數中,進行重置
        sky_1.update_positions(0, -(config.image_sky_height + sky_1.nw[1]))
    # 若sky_2已消失在窗口范围后，从重新移动到sky_1的上方
    elif sky_2.nw[1] >= config.window_boundary_row - sky_2.steps[1]:
        canvas.move(sky_2.bg_image_tags, 0, -(config.image_sky_height + sky_2.nw[1]))
        sky_2.update_positions(0, -(config.image_sky_height + sky_2.nw[1]))
    # 正常移动
    else:
        sky_1.exec_move()
        sky_2.exec_move()
# 创建大飞机
def create_big_plane(root, canvas, enemy_list):
    #rd = 內建random隨機數
    #(0到,室窗口寬-飛機圖的最大寬度)
    x = rd.randint(0, config.window_boundary_col - config.image_bigplane_width)
    big_plane = bigplane.BigPlane(root, canvas, tkinter.SW, x, 0, "BigPlane")
    #(X為隨機,Y= 0,SE西南,BigPlane)
    tmp_canvas_img = canvas.create_image(big_plane.anchor_x,
                                         big_plane.anchor_y,
                                         anchor=big_plane.anchor,
                                         image=big_plane.bg_image,
                                         tags=big_plane.bg_image_tags)
    big_plane.set_canvas_image(tmp_canvas_img)
    #插入列表
    enemy_list.insert(0, big_plane)
    #增加敵機數量
    config.defeat_big_nums += 1
def create_small_plane(root, canvas, enemy_list):
    # 小飞机
    x = rd.randint(0, config.window_boundary_col - config.image_smallplane_width)
    small_plane = smallplane.SmallPlane(root, canvas, tkinter.SW, x, 0, "SmallPlane")
    tmp_canvas_img = canvas.create_image(small_plane.anchor_x,
                                         small_plane.anchor_y,
                                         anchor=small_plane.anchor,
                                         image=small_plane.bg_image,
                                         tags=small_plane.bg_image_tags)
    small_plane.set_canvas_image(tmp_canvas_img)
    enemy_list.insert(0, small_plane)
    config.defeat_small_nums += 1
# 创建小蜜蜂
def create_bee(root, canvas, enemy_list):
    # 蜜蜂
    x = rd.randint(0, config.window_boundary_col - config.image_bee_width)
    bee = honeybee.Bee(root, canvas, tkinter.SW, x, 100, "Bee")
    tmp_canvas_img = canvas.create_image(bee.anchor_x,
                                         bee.anchor_y,
                                         anchor=bee.anchor,
                                         image=bee.bg_image,
                                         tags=bee.bg_image_tags)
    bee.set_canvas_image(tmp_canvas_img)
    enemy_list.insert(0, bee)
    config.defeat_bee_nums += 1


# 创建英雄机
def create_hero(root, canvas, lives):
    #傳入hero.py(窗,布,置中,x/2,在3/2處,標籤,生命值)
    hero = heroplane.HeroPlane(root, canvas,
                               config.initial_anchor_hero,
                               config.initial_anchor_hero_x,
                               config.initial_anchor_hero_y,
                               "HeroPlane01", lives)
#傳入move.py的圖形編號函數(窗寬,高,置中,同上標籤)
    tmp_canvas_img = canvas.create_image(hero.anchor_x,
                                         hero.anchor_y,
                                         anchor=hero.anchor,
                                         image=hero.bg_image,
                                         tags=hero.bg_image_tags)
    hero.set_canvas_image(tmp_canvas_img)



    return hero
# 创建英雄机子彈(, , hero,部件數目(1))
def create_bullet_tags(root, canvas, anchor, x, y, tags):
    blt = bullet.Bullet(root, canvas, anchor, x, y, tags)
    tmp_canvas_img = canvas.create_image(blt.anchor_x,
                                         blt.anchor_y,
                                         anchor=blt.anchor,
                                         image=blt.bg_image,
                                         tags=blt.bg_image_tags)
    blt.set_canvas_image(tmp_canvas_img)
    return blt
# 创建子弹(, , hero,部件數目(1))
def create_bullet(root, canvas, mother, tag_id):
    # 每帧子弹
    blt_1 = create_bullet_tags(root, canvas,
                               tkinter.CENTER,
                               #位置會在中間
                               mother.nw[0] + mother.width / 2,
                               mother.nw[1],
                               "BulletMid" + str(tag_id))
    return blt_1
# 创建敌机
def create_enemys(root, canvas):
    # 敌机列表中插入新敌机
    enemy_list = []
    #(, , [])
    create_big_plane(root, canvas, enemy_list)
    create_small_plane(root, canvas, enemy_list)
    create_bee(root, canvas, enemy_list)
    return enemy_list
def move_enemy(root, canvas, enemy):
    enemy_list = enemy
    for item in enemy_list:
        if item.state is config.life_status_alive:
            item.exec_move()
        else:
            item.errors_happened()


# 创建己方战机
def create_owns(root, canvas):
    #實例化並傳參給英雄機函數(窗口,畫布,生命值)
    hero = create_hero(root, canvas, config.lives_num_hero)
    #(, ,返回的英雄函數,部件數目=1)
    bullet = create_bullet(root, canvas, hero, config.current_bullet_num)
    #部件數目+1
    #必須獲取載入訊息回傳
    return [hero, bullet]
# 移动己方战机( , , 我方戰機create_owns(得到[hero, bullet])
def move_owns(root, canvas, own_list):
    for item in own_list:
        #在飛機以及子彈中(腳色狀態判定)在move.py.state中的移動者狀態 is 腳色生命狀態
        if item.state is config.life_status_alive:
            #每一次判定以後調用飛機以及子彈的exec_move
            item.exec_move()
        # else:
        #     item.errors_happened()
# 碰撞测试
def check_collision(root, canvas, enemy, own):
    # 英雄机与敌机的碰撞
    for item in enemy:
        #英雄.英雄的函數,傳入英雄
        #調用的是英雄的move,傳入的是敵人的函數
        if own[0].is_hit_another(item):
            own[0].update_life_status()
            print("哦!一DA")
        return enemy, own



# 创建图片,接收參數路徑字串,返回並創建圖片(遊戲開始畫面圖)
def create_img(filename):
    start_image_fullname = config.images_path+filename+config.filename_suffix
    print(start_image_fullname)
    #返回並創建(路徑)
    return tkinter.PhotoImage(file=start_image_fullname)
def start_game(event, root, canvas):

    #遊戲標誌

    config.game_flag = 'start'
    print("PlaneWarFare.py 59當前遊戲狀態"+config.game_flag)
    # 屏蔽开始界面
    # delete_canvas_img(canvas, "Start")
    #把開始畫面圖偏移到不見畫面(圖像自定義ID,x座標,y座標)
    canvas.move("Start", 0, config.window_boundary_row * 3 / 2)
    # 创建天空
    sky_first,sky_second = create_sky(root, canvas)
    # 创建敌方战机
    enemy_list = create_enemys(root, canvas)
    # 创建己方战机,跟子彈
    own_list = create_owns(root, canvas)
    # 更新窗口画面
    root.update()

    # 定时更新数据
    while config.game_flag == 'start':
        # 移动天空、(桌布,第一張圖函數,第二張圖函數)
        move_sky(canvas, sky_first, sky_second)
        #敵機
        move_enemy(root, canvas, enemy_list)
        # 每次都調用移動飛機( , , 我方戰機函數)
        move_owns(root, canvas, own_list)

        # 每帧创建一个新子弹
        #傳入hero方法,以獲取座標,定用create_bullet方法創建子彈
        new_blt = create_bullet(root, canvas, own_list[0], config.current_bullet_num)
        config.current_bullet_num += 1
        own_list.append(new_blt)


        # 碰撞测试
        enemy_list, own_list = \
            check_collision(root, canvas, enemy_list, own_list)


        root.update()
        time.sleep(0.0333)


# 退出游戏
def quit_game(event, root, canvas):
    print('quit_game')
    config.game_flag = 'quit'
    canvas.delete("all")
    root.update()
    time.sleep(3)
    quit()
# 程序入口函数
def main():
    # 创建游戏窗口
    root_window = tkinter.Tk()
    #視窗標題
    root_window.title("PlaneWarfareGame")
    #視窗鎖死
    root_window.resizable(width=False, height=False)
    # 创建画布
    window_canvas = tkinter.Canvas(root_window,
                                   width=config.window_boundary_col,
                                   height=config.window_boundary_row)
    #???
    window_canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    # 创建开始界面,傳入配置包參數
    start_img = create_img(config.filename_start)
    #傳入畫布(寬,長,放置中間,圖片位置,標籤)
    window_canvas.create_image(config.window_boundary_col / 2,
                               config.window_boundary_row / 2,
                               anchor=tkinter.CENTER,
                               image=start_img,
                               tags="Start")
    # 创建暂停界面
    #圖片重疊,做減法的目的在於隱藏pause圖片
    pause_img = create_img(config.filename_pause)
    window_canvas.create_image(config.window_boundary_col / 2,
                               -(config.window_boundary_row / 2),
                               anchor=tkinter.CENTER,
                               image=pause_img,
                               tags="Pause")
    # 点击界面开始游戏
    #按鍵啟用臨時函數,傳入多個參數(本身函數名,窗口tkinter,畫布)
    root_window.bind('<KeyPress-space>', lambda event: start_game(event, root_window, window_canvas))
    root_window.bind('<KeyPress-q>', lambda event: quit_game(event, root_window, window_canvas))
    root_window.bind('<KeyPress-Escape>', lambda event: quit_game(event, root_window, window_canvas))
    tkinter.mainloop()


main()