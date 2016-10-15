from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getPos()
r = 10

print(mc.player.getPos())

# clears the area
for x_i in range(int(x - r), int(x + r)):
    for y_i in range(0, int(y + r)):
        for z_i in range(int(z - r), int(z + r)):
            mc.setBlock(x_i, y_i, z_i, 0)

# sets the ground
for x_i in range(int(x - r), int(x + r)):
    for z_i in range(int(z - r), int(z + r)):
        mc.setBlock(x_i, -1, z_i, 1)
