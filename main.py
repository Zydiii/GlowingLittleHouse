from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1.5)
scene.set_floor(-0.85, (0.8, 1.0, 0.8))
scene.set_background_color((0.8, 0.89, 1))
scene.set_directional_light((1, 1, -1), 0.2, (1, 0.8, 0.6))

@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    # scene.set_voxel(vec3(0, 0, 0), 2, vec3(0.9, 0.1, 0.1))
    # draw_tree()
    # draw_circle(ivec3(10, 0, 0), 10, vec3(1), vec3(0))
    # draw_house(ivec3(0, 0, 0), 8, vec3(1), vec3(0))
    draw_ground()
    draw_river(ivec3(0, -40, -17), 27)
    draw_bridge(ivec3(-10, -40, -45), 10, 20, 8, vec3(38,45,55) / 255, vec3(0))
    create_tree(ivec3(10, -40 + 10, -45), 10, vec3(0,109,41) / 255, vec3(174,23,104) / 255)
    create_tree(ivec3(-40, -40 + 10, 10), 10, vec3(0,109,41) / 255, vec3(174,23,104) / 255)
    create_tree(ivec3(30, -40 + 10, 20), 10, vec3(0,109,41) / 255, vec3(174,23,104) / 255)
    create_tree(ivec3(40, -40 + 10, -40), 10, vec3(0,109,41) / 255, vec3(174,23,104) / 255)

# @ti.func
# def draw_tree():
#     # draw trunk
#     draw_trunck(ivec3(0, 0, 0), ivec3(10, 20, 10), 4, vec3(0.28, 0.22, 0.17), vec3(0))

@ti.func
def draw_ground():
    for i in range(4):
        create_block(ivec3(-60, -(i + 1)**2 - 40, -60), ivec3(120, 2 * i + 1, 120), vec3(0.5 - i * 0.1) * vec3(94,175,37) / 255, vec3(0.05 * (3 - i)))
    create_block(ivec3(-60, -40, -60), ivec3(120, 1, 120), vec3(87,162,33) / 255, vec3(0.01))

@ti.func
def draw_river(centerpos, width):
    for i in range(-60, 60):
        width_ran = width + ti.random() * 4
        create_block(vec3(i + centerpos[0], centerpos[1] - 20, (i / 25)**3-width_ran/2 + centerpos[2]), ivec3(1, 21, width_ran),
                     vec3(100, 194, 255) / 255, vec3(0.3))

@ti.func
def draw_step(pos, size, radius, color, color_noise):
    for I in ti.grouped(ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]),(pos[2], pos[2] + size[2]))):
        if(vec2(I[0] - pos[0], I[2] - pos[2]).norm() <= radius):
          scene.set_voxel(I + ivec3(I[1] * ti.sin(I(1) * 0.03), 0, 0), 1, color + color_noise * ti.random())

@ti.func
def draw_circle(pos, height, radius, color, color_noise, flag):
    for I in ti.grouped(ti.ndrange((-radius, radius), (-radius, radius), (0, height))):
        x = ivec3(I[0], 0, I[1])
        if flag and x.norm() >= radius:
            continue
        x[1] = I[2]
        scene.set_voxel(x + pos, 1, color + color_noise * ti.random())

@ti.func
def draw_roof(pos, height, color, color_noise):
    for h in range(0, height / 2):
        draw_circle(pos + ivec3(0, h, 0), 1, height - h, color, color_noise, 1)

@ti.func
def draw_poles(pos, height, color, color_noise):
    draw_circle(pos + ivec3(1 * height / 1.5, 0, 1 * height / 1.5), height, 1, color, color_noise, 0)
    draw_circle(pos + ivec3(1 * height / 1.5, 0, -1 * height / 1.5), height, 1, color, color_noise, 0)
    draw_circle(pos + ivec3(-1 * height / 1.5, 0, 1 * height / 1.5), height, 1, color, color_noise, 0)
    draw_circle(pos + ivec3(-1 * height / 1.5, 0, -1 * height / 1.5), height, 1, color, color_noise, 0)

@ti.func
def draw_base(pos, height, color, color_noise):
    draw_circle(pos, 2, height, color, color_noise, 0)

@ti.func
def draw_house(pos, height, color, color_noise):
    draw_roof(pos + ivec3(0, height + 2, 0), height, color, color_noise)
    draw_poles(pos + ivec3(0, 2, 0), height, color, color_noise)
    draw_base(pos, height, color, color_noise)

@ti.func
def create_block(pos, size, color, color_noise):
    for I in ti.grouped(
            ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]),
                       (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, 1, color + color_noise * ti.random())

@ti.func
def draw_steps(pos, length, width, height, color, color_noise):
    create_block(pos, ivec3(width, height, length), color, color_noise)

@ti.func
def draw_bridge(pos, length, width, height, color, color_noise):
    for h in ti.ndrange((0, height)):
        create_block(pos + ivec3(0, h, h ** 2 * 0.5), ivec3(width, 1, length), color, color_noise)
    posCenter = ivec3(0, height - 1, (height - 1) ** 2 * 0.5)
    for h in ti.ndrange((0, height)):
        create_block(ivec3(pos[0], pos[1] + h, posCenter[2] * 2 + pos[2] - h ** 2 * 0.5), ivec3(width, 1, length), color, color_noise)

@ti.func
def create_tree(pos, radius, color, color1):
    for I in ti.grouped(
            ti.ndrange((-radius, radius), (-radius, radius),
                       (-radius, +radius))):
        f = I / radius
        h = 0.5 - max(f[1], -0.5) * 0.5
        d = vec2(f[0], f[2]).norm()
        prob = max(0, 1 - d) ** 2 * h  # xz mask
        prob *= h  # y mask
        # noise
        prob += ti.sin(f[0] * 5 + pos[0]) * 0.02
        prob += ti.sin(f[1] * 9 + pos[1]) * 0.01
        prob += ti.sin(f[2] * 10 + pos[2]) * 0.03
        if prob < 0.1:
            prob = 0.0
        if ti.random() < prob:
            scene.set_voxel(pos + I, 1, color + (ti.random() - 0.5) * 0.2)
        if ti.random() < prob and not I[0] % 5:
            scene.set_voxel(pos + I, 1, color1 + (ti.random() - 0.5) * 0.2)

initialize_voxels()

scene.finish()
