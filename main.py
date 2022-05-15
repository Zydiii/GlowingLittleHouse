from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1.5)
scene.set_floor(-1, (63/255,43/255,54/255))
scene.set_background_color((0.8, 0.89, 1))
scene.set_directional_light((1, 1, -1), 0.1, (1, 0.8, 0.6))

@ti.kernel
def initialize_voxels():
    draw_house()

@ti.func
def draw_block(pos, size, mat, color):
    for I in ti.grouped(ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]), (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, mat, color)

@ti.func
def draw_house():
    draw_block(ivec3(-58, -64, -20), ivec3(100, 30, 80), 1, ivec3(1, 1, 1)) # 底座
    draw_block(ivec3(-38, -64, 60), ivec3(82, 34, 2), 1, ivec3(58, 143, 183)/255) # 前方栅栏
    draw_block(ivec3(42, -64, -22), ivec3(2, 34, 84), 1, ivec3(58, 143, 183)/255) # 右方栅栏
    draw_block(ivec3(-60, -64, -22), ivec3(102, 34, 2), 1, ivec3(58, 143, 183)/255) # 后方栅栏
    draw_block(ivec3(-60, -64, -22), ivec3(2, 34, 84), 1, ivec3(58, 143, 183)/255) # 左方栅栏
    draw_block(ivec3(-58, -34, -20), ivec3(55, 28, 65), 1, ivec3(138, 107, 190)/255) # 第一层房屋
    draw_block(ivec3(-60, -6, -22), ivec3(59, 2, 69), 1, ivec3(58, 143, 183)/255) # 第一层棚子
    draw_block(ivec3(-58, -4, -20), ivec3(45, 25, 60), 1, ivec3(138, 107, 190)/255) # 第二层房屋
    draw_block(ivec3(-60, 21, -22), ivec3(49, 2, 64), 1, ivec3(58, 143, 183)/255) # 第二层棚子
    draw_block(ivec3(-58, 23, -20), ivec3(40, 30, 25), 1, ivec3(138, 107, 190)/255) # 第三层房屋
    draw_block(ivec3(-58, 53, -20), ivec3(40, 2, 25), 1, ivec3(58, 143, 183)/255) # 第三层棚子
    draw_block(ivec3(-58, 44, 5), ivec3(38, 2, 27), 1, ivec3(38, 107, 190)/255) # 顶层棚子
    draw_block(ivec3(-58, 23, 5), ivec3(38, 2, 27), 1, ivec3(38, 107, 190)/255) # 顶层棚子
    draw_block(ivec3(-56, 25, 28), ivec3(2, 21, 2), 1, ivec3(358, 143, 183)/255) # 顶层柱子
    draw_block(ivec3(-23, 25, 28), ivec3(2, 21, 2), 1, ivec3(358, 143, 183)/255) # 顶层柱子
    draw_block(ivec3(50, -60, -28), ivec3(4, 98, 4), 1, ivec3(358, 143, 183)/255) # 路灯柱子
    draw_block(ivec3(46, -64, -32), ivec3(12, 2, 12), 1, ivec3(38, 107, 190)/255) # 路灯柱子底座
    draw_block(ivec3(47, -62, -31), ivec3(10, 2, 10), 1, ivec3(38, 107, 190)/255) # 路灯柱子底座
    draw_block(ivec3(48, 37, -30), ivec3(8, 2, 8), 1, ivec3(38, 107, 190)/255) # 路灯底座
    draw_block(ivec3(48, 39, -30), ivec3(8, 21, 8), 2, ivec3(255, 255, 251)/255) # 路灯灯芯
    draw_block(ivec3(48, 59, -30), ivec3(8, 2, 8), 1, ivec3(38, 107, 190)/255) # 路灯顶座
    draw_block(ivec3(49, 61, -29), ivec3(6, 3, 6), 1, ivec3(38, 107, 190)/255) # 路灯顶座
    draw_block(ivec3(48, 39, -30), ivec3(2, 21, 2), 1, ivec3(38, 107, 190)/255) # 路灯边框
    draw_block(ivec3(54, 39, -30), ivec3(2, 21, 2), 1, ivec3(38, 107, 190)/255) # 路灯边框
    draw_block(ivec3(48, 39, -24), ivec3(2, 21, 2), 1, ivec3(38, 107, 190)/255) # 路灯边框
    draw_block(ivec3(54, 39, -24), ivec3(2, 21, 2), 1, ivec3(38, 107, 190)/255) # 路灯边框


initialize_voxels()
scene.finish()
