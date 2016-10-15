from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getPos()

# makes a house
length = 7
width = 5
hight = 4

z = z + 2

block_choice = 45

# 45 brick
# 57 diamond


for i in range(hight):
    for j in range(width):
        mc.setBlock(x + j, y + i, z, block_choice)
        mc.setBlock(x + j, y + i, z + length, block_choice)
        
    for j in range(length):
        mc.setBlock(x, y + i, z + j, block_choice)
        mc.setBlock(x + width, y + i, z + j, block_choice)

    
