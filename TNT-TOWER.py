import mcpi.minecraft as minecraft
mc: mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
tnt = 46
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)