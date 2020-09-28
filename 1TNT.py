import mcpi.minecraft as minecraft
mc: mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
tnt = 46
mc.setBlock(x, y, z, tnt, 1)