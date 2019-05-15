import os
import tkinter as tk
import random as rd

#遊戲狀態
#變動性
game_flag = ''

# 游戏窗口的标题及边界
window_title = "Plane Warface Game"
window_boundary_row = 600
window_boundary_col = 480

# 角色的生命状态
life_status_alive = 0   # 活动
life_status_dead = 1    # 死亡
life_status_reset = 2   # 重置
# 角色生命值
lives_num_enemy = 1
lives_num_hero = 3

# 游戏中部件图像所在路径及各部件图像文件名
#os.getcwd()當前工作目錄
images_path = os.getcwd()+ os.path.join("/Images/")
print(images_path)
filename_suffix = ".gif"
filename_sky = "background"
filename_pause = "pause"
filename_start = "start"
filename_smallplane = "smallplane"
filename_bee = "bee"
filename_bigplane = "bigplane"
filename_bullet = "bullet"
filename_hero = "hero"


# 游戏中各部件图像的宽与高
image_sky_width = 480
image_sky_height = 852
image_hero_width = 97
image_hero_height = 124
image_smallplane_width = 49
image_smallplane_height = 36
image_bigplane_width = 69
image_bigplane_height = 99
image_bullet_width = 8
image_bullet_height = 14
image_bee_width = 60
image_bee_height = 50

# 游戏中部件的初始锚点及对应初始显示位置坐标
# 天空 - 将图片的右下角显示在画布的(480,600)的坐标处
#       如下部件以相同方式进行显示

# 己方战机 - 出现在窗口的下三分之一处并水平居中
initial_anchor_hero = tk.CENTER
initial_anchor_hero_x = window_boundary_col / 2
initial_anchor_hero_y = window_boundary_row / 3 * 2

# 游戏中各部件的移动步长
step_length_default = 1
step_length_sky_x = 0
step_length_sky_y = 10
step_length_smallplane_x = 0
step_length_smallplane_y = 5
step_length_bigplane_x = 0
step_length_bigplane_y = 3
step_length_bee_x = 5
step_length_bee_y = 3
step_length_bullet_x = 0
step_length_bullet_y = 12
step_length_hero_x = 5
step_length_hero_y = 5

# 记录当前各种部件的数目
current_bullet_num = 1
#東南
initial_anchor_sky_1 = tk.SE
#窗口寬
initial_anchor_sky_x_1 = window_boundary_col
#窗口長
initial_anchor_sky_y_1 = window_boundary_row
# 击落战机数量
defeat_big_nums = 0
defeat_small_nums = 0
defeat_bee_nums = 0
