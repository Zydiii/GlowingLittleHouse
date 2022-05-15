from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1.5)
scene.set_floor(-0.85, (0.8, 1.0, 0.8))
scene.set_background_color((0.8, 0.89, 1))
scene.set_directional_light((1, 1, -1), 0.2, (1, 0.8, 0.6))

@ti.kernel
def initialize_voxels():
    draw_house()

@ti.func
def draw_block(pos, size, color):
    for I in ti.grouped(ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]), (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, 1, color)

@ti.func
def draw_house():
    draw_block(ivec3(-50, -60, -20), ivec3(100, 30, 80), ivec3(1, 1, 1)) # 底座 (-50, -60, -20)
    draw_block(ivec3(-30, -60, 60), ivec3(82, 34, 2), ivec3(0.0, 0.0, 1.0)) # 前方栅栏 (-30, -60, 60)
    draw_block(ivec3(50, -60, -22), ivec3(2, 34, 84), ivec3(0.0, 0.0, 1.0)) # 右方栅栏 (50, -60, -21)
    draw_block(ivec3(-52, -60, -22), ivec3(102, 34, 2), ivec3(0.0, 0.0, 0.5)) # 后方栅栏 (-52, -60, -21)
    draw_block(ivec3(-52, -60, -22), ivec3(2, 34, 84), ivec3(0.0, 0.0, 1.0)) # 左方栅栏 (-52, -60, -21)



initialize_voxels()
scene.finish()
