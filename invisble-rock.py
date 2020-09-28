import mcpi.minecraft as minecraft
mc: mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
tnt = 46
mc.setBlocks(x, y, z, x+30, y+10, z+30, 95)