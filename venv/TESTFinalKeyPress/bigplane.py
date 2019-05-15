import tkinter
import mover
import config


class BigPlane(mover.BaseMover):
    '''
        移动的敌机 - 大飞机
    '''
    #( , , SW西南,X = 窗寬-圖寬,Y =0,BigPlane)
    def __init__(self, root, canvas, position, x, y, tags):
        super().__init__(root, canvas, position, x, y, tags,
                         config.image_bigplane_width, config.image_bigplane_height, True)
        # 移动者的移动步长
        #0,3
        self.steps = [config.step_length_bigplane_x, config.step_length_bigplane_y]
        # 移动方向 - 向下
        self.move_direction = [0, 1]
        # 移动者加载背景图像
        self.bg_image_fullname = config.images_path + config.filename_bigplane + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        self.bg_image_tags = tags
        #正常情況往下走
        #小於600
    def exec_move(self):
        if self.nw[1] < config.window_boundary_row:
            # Y轴边界之内正常移动
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            self.base_move(self.bg_image_tags, x, y)
            #圖片移-600 往上跑
        else:
            # Y轴边界之外错误处理
            self.base_move(self.bg_image_tags, 0, -config.window_boundary_row)