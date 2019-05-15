import tkinter
import mover
import config
#mover.BaseMover進行運算後所有變量函數返回至便可供PlaneWarFare.py調用
class Sky(mover.BaseMover):
    '''
        移动的天空背景
    '''
    #由PlaneWarFare.py的create_sky傳入
    #依序傳入(窗口,桌布,東南SE座標,窗口寬,窗口長,標籤
    def __init__(self, root, canvas, position, x, y, tags):

        #傳給mover.BaseMover
        super().__init__(root, canvas, position, x, y, tags,
                         config.image_sky_width, config.image_sky_height, False)

        # 移动者的移动步长(0,10)
        self.steps = [config.step_length_sky_x, config.step_length_sky_y]
        # 移动方向 - 向下
        self.move_direction = [0, 1]
        #移动者加载背景图像
        self.bg_image_fullname = config.images_path + config.filename_sky + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        self.bg_image_tags = tags

    #被調後執行一次移動
    def exec_move(self):
        x = self.steps[0] * self.move_direction[0]
        y = self.steps[1] * self.move_direction[1]
        #傳入move.py的函數參數(當前移動圖的標籤,衡移通常為0,向下移為10
        self.base_move(self.bg_image_tags, x, y)
