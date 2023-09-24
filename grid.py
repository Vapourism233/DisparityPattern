import numpy as np
import taichi as ti
import taichi.math as tm
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import math

ti.init(arch=ti.cpu)

WIDTH, HEIGHT = 21, 29.7

fig, ax = plt.subplots(figsize=(WIDTH, HEIGHT), dpi=100)
fig.subplots_adjust(left = 0, bottom= 0, right=1, top = 1)
fig.set_facecolor("gray")
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.axis("off")

grid_n = 30
res = (grid_n, grid_n)
dx = 1 / res[0]
inv_dx = res[0]
radius = dx * ti.sqrt(2)
desired_samples = 10000
grid = ti.field(dtype=int, shape=res)
samples = ti.Vector.field(2, float, shape=desired_samples)
grid.fill(-1)

def check_distance(l1, l2):
    if np.sqrt((l1[0] - l2[0])**2 + (l1[1] - l2[1])**2) < 2 * radius:
        return False
    return True

@ti.func
def check_collision(p, index):
    x, y = index
    collision = False
    for i in range(max(0, x - 2), min(grid_n, x + 3)):
        for j in range(max(0, y - 2), min(grid_n, y + 3)):
            if grid[i, j] != -1:
                q = samples[grid[i, j]]
                if (q - p).norm() < radius - 1e-6:
                    collision = True
    return collision

@ti.kernel
def poisson_disk_sample(desired_samples: int) -> int:
    samples[0] = tm.vec2(0.5)
    grid[int(grid_n * 0.5), int(grid_n * 0.5)] = 0
    head, tail = 0, 1
    while head < tail and head < desired_samples:
        source_x = samples[head]
        head += 1

        for _ in range(100):
            theta = ti.random() * 2 * tm.pi
            offset = tm.vec2(tm.cos(theta), tm.sin(theta)) * (1 + ti.random()) * radius
            new_x = source_x + offset
            new_index = int(new_x * inv_dx)

            if 0 <= new_x[0] < 1 and 0 <= new_x[1] < 1:
                collision = check_collision(new_x, new_index)
                if not collision and tail < desired_samples:
                    samples[tail] = new_x
                    grid[new_index] = tail
                    tail += 1
    return tail

num_samples = poisson_disk_sample(desired_samples)
for i in range(np.shape(samples)[0]):
    samples[i] = [samples[i][0] * WIDTH, samples[i][1] * HEIGHT]
print(num_samples)
# gui = ti.GUI("Poisson Disk Sampling", res=800, background_color=0xFFFFFF)
i = 0  # Initialize i
flag, flag1 = 0, 0
while i < 1000:
    j = 0  # Initialize j inside the outer loop
    while j < i:
        # print(samples.to_numpy()[i])
        if check_distance(samples.to_numpy()[i], samples.to_numpy()[j]):
            flag1 += 1
            if flag1 == 100:
                break
        else:
            circle = Circle((samples.to_numpy()[i][0], samples.to_numpy()[i][1]), radius=0.2, color="black")
            ax.add_patch(circle)
        j += 1  # Increment j
    i += 1  # Increment i outside the inner loop


plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('img')

# while gui.running:
#     gui.circles(samples.to_numpy()[:min(count * speed, num_samples)],
#                 color=0x000000,
#                 radius=1.5)
#     count += 1
#     gui.show()