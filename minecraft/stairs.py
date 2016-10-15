from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getPos()

# makes a spiral staircase
x_i = x + 2
y_i = y
z_i = z
side = 1
side_count = 1

for i in range(9):

    if side == 1:
        x_i += 1
    elif side == 2:
        y_i += 1
    elif side == 3:
        x_i -= 1
    elif side == 4:
        y_i -= 1

    if side_count == 3:
        side_count = 1
        side += 1
        if side == 5:
            side = 1
    
    mc.setBlock(x_i, y_i, z_i + i, 1)
