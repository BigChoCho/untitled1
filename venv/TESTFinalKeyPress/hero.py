import tkinter
import mover
import config

class HeroPlane(mover.BaseMover):
    '''
           移动的敌机 - 大飞机
       '''
    def __init__(self, root, canvas, position, x, y, tags, lives):
        #(, , , 飛機距離窗口由上往下3/2 x,y ,標籤,圖寬,圖高, , )
        super().__init__(root, canvas, position, x, y, tags,
                         config.image_hero_width, config.image_hero_height, True)
        # 移动者的移动步长

        self.steps = [config.step_length_hero_x, config.step_length_hero_y]
        #默認情況下讓飛機始終保持前行
        self.move_direction = [0, -1]

        # 移动者加载背景图像
        self.bg_image_fullname = config.images_path + config.filename_hero + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        #創建按鈕並且傳入對應碼
        root.bind('<KeyPress-Left>', self.key_press)
        root.bind('<KeyPress-Up>', self.key_press)
        root.bind('<KeyPress-Down>', self.key_press)
        root.bind('<KeyPress-Right>', self.key_press)
        #不斷循環的判斷
    def exec_move(self):
        #在通常情況下,nw的x跟y軸大於0(西北向)se=東南,x,y軸小於是窗框高時保持正常移動
        if 0 < self.nw[0] and 0 < self.nw[1] \
                and self.se[0] < config.window_boundary_col \
                and self.se[1] < config.window_boundary_row:
            # X/Y轴边界之内正常移动,steps不變,move_direction始終改變1,0,-1 =方向的改變
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            # print(self, x, y)
            #在MOVE.PY的方法,傳入當前使用者標籤,bg_image_tags IN THE MOVE.PY
            self.base_move(self.bg_image_tags, x, y)
            #如果超過視窗
        else:
            # 不执行跨越边界的操作
            #在臨界時你是呈現-1往上的狀態此時讓尼保持在1,也就是把尼反彈回來
            if self.nw[0] <= 0:
                self.base_move(self.bg_image_tags, 1, 0)
            if self.nw[1] <= 0:
                self.base_move(self.bg_image_tags, 0, 1)
            if self.se[0] >= config.window_boundary_col:
                self.base_move(self.bg_image_tags, -1, 0)
            if self.se[1] >= config.window_boundary_row:
                self.base_move(self.bg_image_tags, 0, -1)

    def key_press(self, event):
        #傳入對應碼以做判斷
        code = event.keycode

        if code == 38:  # 上
            self.move_direction = [0, -1]
        elif code == 40:  # 下
            self.move_direction = [0, 1]
        elif code == 37:  # 左
            self.move_direction = [-1, 0]
        elif code == 39:  # 右
            self.move_direction = [1, 0]
