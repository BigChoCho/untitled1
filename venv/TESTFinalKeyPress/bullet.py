import tkinter
import mover
import config

class Bullet(mover.BaseMover):
    def __init__(self, root, canvas, position, x, y, tags):
        super().__init__(root, canvas, position, x, y, tags,
                         config.image_bullet_width, config.image_bullet_height, False)
        # 移动者的移动步长
        self.steps = [config.step_length_bullet_x, config.step_length_bullet_y]
        self.move_direction = [0, -1]
        #移动者加载背景图像
        self.bg_image_fullname = config.images_path + config.filename_bullet + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)

    def exec_move(self):
        if self.nw[1] < config.window_boundary_row:
            # Y轴边界之内正常移动
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            self.base_move(self.bg_image_tags, x, y)
        # else:
        #     # Y轴边界之外错误处理
        #     self.update_life_status()
        #     self.errors_happened()