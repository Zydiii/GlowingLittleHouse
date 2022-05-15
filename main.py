from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1.0)
scene.set_floor(-1, (1,1,1))
scene.set_background_color((0, 0, 0))
scene.set_directional_light((1.5, 0.5, 1), .1, (54/255/4,23/255/4,45/255/4))

@ti.kernel
def initialize_voxels():
    draw_house()
@ti.func
def draw_block(pos, size, mat, color, color_noise):
    for I in ti.grouped(ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]), (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, mat, color + color_noise * ti.random())
@ti.func
def draw_walls(pos, direction, length, height, color, dist0, dist1):
    for I in ti.grouped(ti.ndrange((length // dist0) + 1, (height // dist1) + 1)):
        if direction[2] == 1:
            draw_block(pos + direction * I[0] * dist0 + ivec3(0, I[1], 0) * dist1,
                       ivec3(2, dist1 - 1, dist0 - 1), 1, color, vec3(0.0))
        else:
            draw_block(pos + direction * I[0] * dist0 + ivec3(0, I[1], 0) * dist1,
                       ivec3(dist0 - 1, dist1 - 1, 2), 1, color, vec3(0.0))
@ti.func
def draw_house():
    draw_block(ivec3(-58, -64, -50), ivec3(100, 30, 80), 1, vec3(226,148,59)/255, vec3(0.3)) # 底座
    draw_block(ivec3(-38, -64, 30), ivec3(82, 34, 2), 1, vec3(55,60,56)/255, vec3(0.0)) # 前方栅栏
    draw_walls(ivec3(-40, -64, 30), ivec3(1, 0, 0), 82, 34, vec3(115,67,56)/255, 5, 2) # 前方砖块
    draw_block(ivec3(42, -64, -52), ivec3(2, 34, 84), 1, vec3(55,60,56)/255, vec3(0.0)) # 右方栅栏
    draw_walls(ivec3(42, -64, -52), ivec3(0, 0, 1), 84, 34, vec3(115,67,56)/255, 5, 2) # 右方砖块
    draw_block(ivec3(-60, -64, -52), ivec3(102, 34, 2), 1, vec3(55,60,56)/255, vec3(0.0)) # 后方栅栏
    draw_walls(ivec3(-60, -64, -52), ivec3(1, 0, 0), 102, 34, vec3(115,67,56)/255, 5, 2) # 后方砖块
    draw_block(ivec3(-60, -64, -52), ivec3(2, 34, 108), 1, vec3(55,60,56)/255, vec3(0.0)) # 左方栅栏
    draw_walls(ivec3(-60, -64, -52), ivec3(0, 0, 1), 108, 34, vec3(115,67,56)/255, 5, 2) # 左方砖块
    draw_block(ivec3(-58, -34, -50), ivec3(55, 28, 70), 1, vec3(250,214,137)/255, vec3(0.0)) # 第一层房屋
    draw_block(ivec3(-54, -32, 19), ivec3(12, 20, 1), 0, vec3(100,106,88)/255, vec3(0.0)) # 第一层房屋的门
    draw_block(ivec3(-54, -32, 18), ivec3(12, 20, 1), 1, vec3(100,106,88)/255, vec3(0.0)) # 第一层房屋的门
    draw_block(ivec3(-53, -23, 19), ivec3(2, 2, 1), 1, vec3(255,255,251)/255, vec3(0.0)) # 第一层房屋的门把手
    draw_block(ivec3(-30, -20, 18), ivec3(10, 10, 2), 0, vec3(0,92,175)/255, vec3(0.0)) # 第一层房屋的窗户1
    draw_block(ivec3(-30, -20, 17), ivec3(10, 10, 1), 2, vec3(221,165,45)/255, vec3(0.0)) # 第一层房屋的窗户1
    draw_block(ivec3(-5, -30, -35), ivec3(2, 20, 30), 0, vec3(0,92,175)/255, vec3(0.0)) # 第一层房屋的窗户2
    draw_block(ivec3(-6, -30, -35), ivec3(1, 20, 30), 2, vec3(221,165,45)/255, vec3(0.0)) # 第一层房屋的窗户2
    draw_block(ivec3(-3, -10, -35), ivec3(13, 2, 30), 1, vec3(226,148,59)/255, vec3(0.0)) # 第一层房屋的窗户棚子
    draw_block(ivec3(-3, -8, -35), ivec3(10, 2, 30), 1, vec3(226,148,59)/255, vec3(0.0)) # 第一层房屋的窗户棚子
    draw_block(ivec3(12, -34, -46), ivec3(20, 6, 6), 1, vec3(82,67,61)/255, vec3(0.0)) # 椅子
    draw_block(ivec3(12, -34, -50), ivec3(20, 12, 4), 1, vec3(82,67,61)/255, vec3(0.0)) # 椅子
    draw_block(ivec3(18, -34, 4), ivec3(20, 2, 20), 1, vec3(255,255,255)/255, vec3(0.0)) # 花盆
    draw_block(ivec3(20, -36, 6), ivec3(16, 6, 16), 1, vec3(27,129,62)/255, vec3(0.5)) # 绿叶
    draw_block(ivec3(0, -34, 4), ivec3(3, 2, 3), 1, vec3(255,255,255)/255, vec3(0.0)) # 花盆1
    draw_block(ivec3(1, -32, 5), ivec3(1, 5, 1), 1, vec3(120,85,43)/255, vec3(0.0)) # 花盆1
    draw_block(ivec3(0, -27, 4), ivec3(3, 4, 3), 1, vec3(208,16,16)/255, vec3(0.0)) # 花盆1
    draw_block(ivec3(0, -34, 14), ivec3(3, 2, 3), 1, vec3(255, 255, 255) / 255, vec3(0.0))  # 花盆2
    draw_block(ivec3(1, -32, 15), ivec3(1, 5, 1), 1, vec3(120, 85, 43) / 255, vec3(0.0))  # 花盆2
    draw_block(ivec3(0, -27, 14), ivec3(3, 4, 3), 1, vec3(208, 16, 16) / 255, vec3(0.0))  # 花盆2
    draw_block(ivec3(-60, -6, -52), ivec3(59, 2, 74), 1, vec3(55,60,56)/255, vec3(0.0)) # 第一层棚子
    draw_block(ivec3(-58, -4, -50), ivec3(45, 25, 60), 1, vec3(55,60,56)/255, vec3(0.0)) # 第二层房屋
    draw_block(ivec3(-14, 2, -30), ivec3(1, 14, 18), 2, vec3(221,165,45)/255, vec3(0.0)) # 第二层窗户1
    draw_block(ivec3(-12, 0, -31), ivec3(1, 18, 22), 1, vec3(255, 255, 255)/255, vec3(0.0)) # 第二层窗户1
    draw_block(ivec3(-12, 2, -30), ivec3(1, 14, 18), 0, vec3(51, 103, 116) / 255, vec3(0.0))  # 第二层窗户1
    draw_block(ivec3(-50, 2, 9), ivec3(8, 14, 1), 2, vec3(221,165,45)/255, vec3(0.0)) # 第二层窗户2
    draw_block(ivec3(-52, 0, 10), ivec3(12, 18, 1), 1, vec3(255, 255, 255)/255, vec3(0.0)) # 第二层窗户2
    draw_block(ivec3(-50, 2, 10), ivec3(8, 14, 1), 0, vec3(129, 199, 212)/255, vec3(0.0)) # 第二层窗户2
    draw_block(ivec3(-40, 2, 9), ivec3(8, 14, 1), 2, vec3(221,165,45) / 255, vec3(0.0))  # 第二层窗户3
    draw_block(ivec3(-42, 0, 10), ivec3(12, 18, 1), 1, vec3(255, 255, 255) / 255, vec3(0.0))  # 第二层窗户3
    draw_block(ivec3(-40, 2, 10), ivec3(8, 14, 1), 0, vec3(129, 199, 212) / 255, vec3(0.0))  # 第二层窗户3
    draw_block(ivec3(-60, 21, -52), ivec3(49, 2, 64), 1, vec3(55,60,56)/255, vec3(0.0)) # 第二层棚子
    draw_block(ivec3(-58, 23, -50), ivec3(40, 30, 25), 1, vec3(250,214,137)/255, vec3(0.0)) # 第三层房屋
    draw_block(ivec3(-56, 24, -46), ivec3(36, 25, 21), 0, vec3(138, 107, 190)/255, vec3(0.0)) # 第三层房屋
    draw_block(ivec3(-56, 48, -46), ivec3(36, 1, 21), 2, vec3(221,165,45)/255, vec3(0.0)) # 第三层房屋里的灯
    draw_block(ivec3(-19, 40, -45), ivec3(1, 8, 14), 2, vec3(221,165,45)/255, vec3(0.0)) # 第三层窗户
    draw_block(ivec3(-18, 38, -47), ivec3(1, 12, 18), 1, vec3(255, 255, 255)/255, vec3(0.0)) # 第三层窗户
    draw_block(ivec3(-18, 40, -45), ivec3(1, 8, 14), 0, vec3(255, 255, 255)/255, vec3(0.0)) # 第三层窗户
    draw_block(ivec3(-58, 48, -25), ivec3(38, 2, 27), 1, vec3(82,67,61)/255, vec3(0.0)) # 遮阳棚
    draw_block(ivec3(-58, 23, -25), ivec3(38, 2, 27), 1, vec3(82,67,61)/255, vec3(0.0)) # 遮阳棚
    draw_block(ivec3(-56, 25, -2), ivec3(2, 23, 2), 1, vec3(82,67,61)/255, vec3(0.0)) # 遮阳棚柱子
    draw_block(ivec3(-23, 25, -2), ivec3(2, 23, 2), 1, vec3(82,67,61)/255, vec3(0.0)) # 遮阳棚柱子
    draw_block(ivec3(50, -60, -58), ivec3(4, 90, 4), 1, vec3(82,67,61)/255, vec3(0.0)) # 路灯柱子
    draw_block(ivec3(46, -64, -62), ivec3(12, 2, 12), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯柱子底座
    draw_block(ivec3(47, -62, -61), ivec3(10, 2, 10), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯柱子底座
    draw_block(ivec3(48, 30, -60), ivec3(8, 2, 8), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯底座
    draw_block(ivec3(48, 32, -60), ivec3(8, 21, 8), 2, vec3(255, 255, 251)/255, vec3(0.0)) # 路灯灯芯
    draw_block(ivec3(48, 53, -60), ivec3(8, 2, 8), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯顶座
    draw_block(ivec3(49, 55, -59), ivec3(6, 3, 6), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯顶座
    draw_block(ivec3(48, 32, -60), ivec3(2, 21, 2), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯边框
    draw_block(ivec3(54, 32, -60), ivec3(2, 21, 2), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯边框
    draw_block(ivec3(48, 32, -54), ivec3(2, 21, 2), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯边框
    draw_block(ivec3(54, 32, -54), ivec3(2, 21, 2), 1, vec3(38, 107, 190)/255, vec3(0.0)) # 路灯边框
    draw_block(ivec3(-58, -64, 20), ivec3(18, 34, 10), 1, vec3(55,60,56) / 255, vec3(0.0))  # 台阶
    draw_block(ivec3(-58, -64, 30), ivec3(18, 30, 10), 1, vec3(55,60,56) / 255, vec3(0.0))  # 台阶
    draw_block(ivec3(-58, -64, 40), ivec3(18, 24, 17), 1, vec3(55,60,56) / 255, vec3(0.0))  # 台阶
    draw_block(ivec3(-40, -64, 40), ivec3(10, 18, 17), 1, vec3(55,60,56) / 255, vec3(0.0))  # 台阶
    draw_block(ivec3(-30, -64, 40), ivec3(10, 12, 17), 1, vec3(55,60,56) / 255, vec3(0.0))  # 台阶
    draw_block(ivec3(-20, -64, 40), ivec3(10, 6, 17), 1, vec3(55,60,56) / 255, vec3(0.0))  # 台阶
initialize_voxels()
scene.finish()