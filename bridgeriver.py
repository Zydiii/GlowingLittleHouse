from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1.5)
scene.set_floor(-0.85, (0.8, 1.0, 0.8))
scene.set_background_color((0.8, 0.89, 1))
scene.set_directional_light((1, 1, -1), 0.2, (1, 0.8, 0.6))

@ti.kernel
def initialize_voxels():
    draw_ground()
    draw_river(ivec3(0, -40, -17), 27, 3)
    draw_bridge(ivec3(-10, -40, -45), 10, 20, 8, vec3(38, 45, 55) / 255, vec3(0))

@ti.func
def draw_ground():
    for i in range(4):
        create_block(ivec3(-60, -(i + 1) ** 2 - 40, -60), ivec3(120, 2 * i + 1, 120),
                     vec3(0.5 - i * 0.1) * vec3(94, 175, 37) / 255, vec3(0.05 * (3 - i)), 1)
    create_block(ivec3(-60, -40, -60), ivec3(120, 1, 120), vec3(87, 162, 33) / 255, vec3(0.01), 1)

@ti.func
def draw_river(centerpos, width, depth):
    for I in ti.grouped(ti.ndrange((-60, 60), (0, depth))):
        create_block(vec3(I[0] + centerpos[0], centerpos[1] - depth, (I[0] / 24) ** 3 - width / 2 + centerpos[2]),
                     ivec3(1, 1, width),
                     vec3(100, 194, 255) / 255, vec3(0.3), 1)
        create_block(vec3(I[0] + centerpos[0], centerpos[1] - (depth - I[1]) + 1,
                          (I[0] / 25) ** 3 - (width + I[1] * 2) / 2 + centerpos[2]),
                     ivec3(1, 1, width + I[1] * 2), vec3(100, 194, 255) / 255, vec3(0.3), 0)

@ti.func
def draw_step(pos, size, radius, color, color_noise):
    for I in ti.grouped(ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]), (pos[2], pos[2] + size[2]))):
        if (vec2(I[0] - pos[0], I[2] - pos[2]).norm() <= radius):
            scene.set_voxel(I + ivec3(I[1] * ti.sin(I(1) * 0.03), 0, 0), 1, color + color_noise * ti.random())

@ti.func
def create_block(pos, size, color, color_noise, mat):
    for I in ti.grouped(ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]), (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, mat, color + color_noise * ti.random())

@ti.func
def draw_bridge(pos, length, width, height, color, color_noise):
    for h in ti.ndrange((0, height)):
        create_block(pos + ivec3(0, h, h ** 2 * 0.5), ivec3(width, 1, length), color, color_noise, 1)
    posCenter = ivec3(0, height - 1, (height - 1) ** 2 * 0.5)
    for h in ti.ndrange((0, height)):
        create_block(ivec3(pos[0], pos[1] + h, posCenter[2] * 2 + pos[2] - h ** 2 * 0.5), ivec3(width, 1, length),
                     color, color_noise, 1)

@ti.func
def draw_brush(pos, height, radius, color, color_noise):
    for I in ti.grouped(ti.ndrange((-radius, radius), (0, height), (-radius, radius))):
        x = ivec3(I[0], 0, I[1])
        if x.norm() <= radius and ti.random() <= 0.5:
            x[1] = I[2]
            scene.set_voxel(x + pos, 1, color + color_noise * ti.random())

initialize_voxels()
scene.finish()
