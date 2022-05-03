from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1.5)
scene.set_floor(0, (0.8, 1.0, 0.8))
scene.set_background_color((0.8, 0.89, 1))
scene.set_directional_light((1, 1, -1), 0.2, (1, 0.8, 0.6))

@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    # scene.set_voxel(vec3(0, 0, 0), 2, vec3(0.9, 0.1, 0.1))
    # draw_tree()
    draw_circle(ivec3(10, 0, 0), 10, vec3(1), vec3(0))

@ti.func
def draw_tree():
    # draw trunk
    draw_trunck(ivec3(0, 0, 0), ivec3(10, 20, 10), 4, vec3(0.28, 0.22, 0.17), vec3(0))

@ti.func
def draw_trunck(pos, size, radius, color, color_noise):
    for I in ti.grouped(ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]),(pos[2], pos[2] + size[2]))):
        if(vec2(I[0] - pos[0], I[2] - pos[2]).norm() <= radius):
          scene.set_voxel(I + ivec3(I[1] * ti.sin(I(1) * 0.03), 0, 0), 1, color + color_noise * ti.random())

@ti.func
def draw_circle(pos, radius, color, color_noise):
    for I in ti.grouped(ti.ndrange((-radius, radius), (-radius, radius))):
        x = ivec3(I[0], 0, I[1])
        if(x.norm() <= radius):
            scene.set_voxel(x + pos, 1, color + color_noise * ti.random())

# @ti.func
# def draw_roof(pos, height, radius, color, color_noise):
#     for h in ti.ndrange(height):
#
#     for I in ti.grouped(ti.ndrange((-radius, radius), (-radius, radius))):
#         x = ivec3(I[0], 0, I[1])
#         if(x.norm() <= radius):
#             scene.set_voxel(x + pos, 1, color + color_noise * ti.random())

initialize_voxels()

scene.finish()
