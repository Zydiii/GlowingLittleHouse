from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1.0)
scene.set_floor(-1, (255/255,255/255,255/255))
scene.set_background_color((0, 0, 0))
scene.set_directional_light((1.5, 0.5, 1), .1, (109/255,46/255,91/255))

@ti.kernel
def initialize_voxels():
    draw_house()

@ti.func
def draw_block(pos, size, mat, color):
    for I in ti.grouped(ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]), (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, mat, color)

@ti.func
def draw_house():
    draw_block(ivec3(-58, -64, -50), ivec3(100, 30, 80), 1, ivec3(226,148,59)/255) # 底座
    draw_block(ivec3(-38, -64, 30), ivec3(82, 34, 2), 1, ivec3(115,67,56)/255) # 前方栅栏
    draw_block(ivec3(42, -64, -52), ivec3(2, 34, 84), 1, ivec3(115,67,56)/255) # 右方栅栏
    draw_block(ivec3(-60, -64, -52), ivec3(102, 34, 2), 1, ivec3(115,67,56)/255) # 后方栅栏
    draw_block(ivec3(-60, -64, -52), ivec3(2, 34, 110), 1, ivec3(115,67,56)/255) # 左方栅栏
    draw_block(ivec3(-58, -34, -50), ivec3(55, 28, 70), 1, ivec3(250,214,137)/255) # 第一层房屋
    draw_block(ivec3(-54, -32, 19), ivec3(12, 20, 1), 0, ivec3(100,106,88)/255) # 第一层房屋的门
    draw_block(ivec3(-54, -32, 18), ivec3(12, 20, 1), 1, ivec3(100,106,88)/255) # 第一层房屋的门
    draw_block(ivec3(-53, -23, 19), ivec3(2, 2, 1), 1, ivec3(255,255,251)/255) # 第一层房屋的门把手
    draw_block(ivec3(-5, -30, -35), ivec3(2, 20, 30), 0, ivec3(0,92,175)/255) # 第一层房屋的窗户
    draw_block(ivec3(-6, -30, -35), ivec3(1, 20, 30), 2, ivec3(69,130,177)/255) # 第一层房屋的窗户
    draw_block(ivec3(-3, -10, -35), ivec3(13, 2, 30), 1, ivec3(226,148,59)/255) # 第一层房屋的窗户棚子
    draw_block(ivec3(-3, -8, -35), ivec3(10, 2, 30), 1, ivec3(226,148,59)/255) # 第一层房屋的窗户棚子
    draw_block(ivec3(12, -34, -46), ivec3(20, 6, 6), 1, ivec3(82,67,61)/255) # 椅子
    draw_block(ivec3(12, -34, -50), ivec3(20, 12, 4), 1, ivec3(82,67,61)/255) # 椅子
    draw_block(ivec3(-60, -6, -52), ivec3(59, 2, 74), 1, ivec3(55,60,56)/255) # 第一层棚子
    draw_block(ivec3(-58, -4, -50), ivec3(45, 25, 60), 1, ivec3(55,60,56)/255) # 第二层房屋
    draw_block(ivec3(-14, 2, -30), ivec3(1, 14, 18), 2, ivec3(69,130,177)/255) # 第二层窗户1
    draw_block(ivec3(-12, 0, -31), ivec3(1, 18, 22), 1, ivec3(255, 255, 255)/255) # 第二层窗户1
    draw_block(ivec3(-12, 2, -30), ivec3(1, 14, 18), 0, ivec3(51, 103, 116) / 255)  # 第二层窗户1
    draw_block(ivec3(-50, 2, 9), ivec3(8, 14, 1), 2, ivec3(69,130,177)/255) # 第二层窗户2
    draw_block(ivec3(-52, 0, 10), ivec3(12, 18, 1), 1, ivec3(255, 255, 255)/255) # 第二层窗户2
    draw_block(ivec3(-50, 2, 10), ivec3(8, 14, 1), 0, ivec3(129, 199, 212)/255) # 第二层窗户2
    draw_block(ivec3(-40, 2, 9), ivec3(8, 14, 1), 2, ivec3(69,130,177) / 255)  # 第二层窗户3
    draw_block(ivec3(-42, 0, 10), ivec3(12, 18, 1), 1, ivec3(255, 255, 255) / 255)  # 第二层窗户3
    draw_block(ivec3(-40, 2, 10), ivec3(8, 14, 1), 0, ivec3(129, 199, 212) / 255)  # 第二层窗户3
    draw_block(ivec3(-60, 21, -52), ivec3(49, 2, 64), 1, ivec3(55,60,56)/255) # 第二层棚子
    draw_block(ivec3(-58, 23, -50), ivec3(40, 30, 25), 1, ivec3(250,214,137)/255) # 第三层房屋
    draw_block(ivec3(-56, 24, -46), ivec3(36, 25, 21), 0, ivec3(138, 107, 190)/255) # 第三层房屋
    draw_block(ivec3(-56, 48, -46), ivec3(36, 1, 21), 2, ivec3(255, 255, 255)/255) # 第三层房屋里的灯
    draw_block(ivec3(-58, 53, -50), ivec3(40, 2, 25), 1, ivec3(58, 143, 183)/255) # 第三层棚子
    draw_block(ivec3(-19, 40, -45), ivec3(1, 8, 14), 2, ivec3(129, 199, 212)/255) # 第三层窗户
    draw_block(ivec3(-18, 38, -47), ivec3(1, 12, 18), 1, ivec3(255, 255, 255)/255) # 第三层窗户
    draw_block(ivec3(-18, 40, -45), ivec3(1, 8, 14), 0, ivec3(255, 255, 255)/255) # 第三层窗户
    draw_block(ivec3(-58, 48, -25), ivec3(38, 2, 27), 1, ivec3(82,67,61)/255) # 遮阳棚
    draw_block(ivec3(-58, 23, -25), ivec3(38, 2, 27), 1, ivec3(82,67,61)/255) # 遮阳棚
    draw_block(ivec3(-56, 25, -2), ivec3(2, 23, 2), 1, ivec3(82,67,61)/255) # 遮阳棚柱子
    draw_block(ivec3(-23, 25, -2), ivec3(2, 23, 2), 1, ivec3(82,67,61)/255) # 遮阳棚柱子
    draw_block(ivec3(50, -60, -58), ivec3(4, 98, 4), 1, ivec3(82,67,61)/255) # 路灯柱子
    draw_block(ivec3(46, -64, -62), ivec3(12, 2, 12), 1, ivec3(38, 107, 190)/255) # 路灯柱子底座
    draw_block(ivec3(47, -62, -61), ivec3(10, 2, 10), 1, ivec3(38, 107, 190)/255) # 路灯柱子底座
    draw_block(ivec3(48, 37, -60), ivec3(8, 2, 8), 1, ivec3(38, 107, 190)/255) # 路灯底座
    draw_block(ivec3(48, 39, -60), ivec3(8, 21, 8), 2, ivec3(255, 255, 251)/255) # 路灯灯芯
    draw_block(ivec3(48, 59, -60), ivec3(8, 2, 8), 1, ivec3(38, 107, 190)/255) # 路灯顶座
    draw_block(ivec3(49, 61, -59), ivec3(6, 3, 6), 1, ivec3(38, 107, 190)/255) # 路灯顶座
    draw_block(ivec3(48, 39, -60), ivec3(2, 21, 2), 1, ivec3(38, 107, 190)/255) # 路灯边框
    draw_block(ivec3(54, 39, -60), ivec3(2, 21, 2), 1, ivec3(38, 107, 190)/255) # 路灯边框
    draw_block(ivec3(48, 39, -54), ivec3(2, 21, 2), 1, ivec3(38, 107, 190)/255) # 路灯边框
    draw_block(ivec3(54, 39, -54), ivec3(2, 21, 2), 1, ivec3(38, 107, 190)/255) # 路灯边框
    draw_block(ivec3(-58, -64, 20), ivec3(20, 34, 10), 1, ivec3(55,60,56) / 255)  # 台阶
    draw_block(ivec3(-58, -64, 30), ivec3(20, 30, 10), 1, ivec3(55,60,56) / 255)  # 台阶
    draw_block(ivec3(-58, -64, 40), ivec3(20, 24, 20), 1, ivec3(55,60,56) / 255)  # 台阶
    draw_block(ivec3(-38, -64, 40), ivec3(10, 18, 20), 1, ivec3(55,60,56) / 255)  # 台阶
    draw_block(ivec3(-28, -64, 40), ivec3(10, 12, 20), 1, ivec3(55,60,56) / 255)  # 台阶
    draw_block(ivec3(-18, -64, 40), ivec3(10, 6, 20), 1, ivec3(55,60,56) / 255)  # 台阶

initialize_voxels()
scene.finish()
