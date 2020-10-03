#made by levi sergeant
#whool tree house
from mcpi import minecraft
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
#house
mc.setBlocks(x-5, y, z-5, x+5, y+4, z+5, 35)
#hollows out house
mc.setBlocks(x-4, y+1, z-4, x+4, y+4, z+4, 0)
#makes door
mc.setBlocks(x, y+2, z-5, x, y+1, z, 0)
#chimeney
mc.setBlocks(x-1, y+1, z+1, x+1, y+3, z+2, 4)
#oven
mc.setBlocks(x, y+1, z+1, x, y+1, z+1, 62, 2)
#space obove oven
mc.setBlocks(x, y+2, z+1, x, y+2, z+1, 0)
from mcpi import minecraft
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
#house
mc.setBlocks(x-5, y, z-5, x+5, y+4, z+5, 35)
#hollows out house
mc.setBlocks(x-4, y+1, z-4, x+4, y+4, z+4, 0)
#makes door
mc.setBlocks(x, y+2, z-5, x, y+1, z, 0)
#chimeney
mc.setBlocks(x-1, y+1, z+1, x+1, y+3, z+2, 4)
#oven
mc.setBlocks(x, y+1, z+1, x, y+1, z+1, 62, 2)
#space obove oven
mc.setBlocks(x, y+2, z+1, x, y+2, z+1, 0)
#chim stack
mc.setBlocks(x, y+2, z+2, x, y+11, z+2, 4)
#roof
mc.setBlocks(x-6, y+5, z-6, x+6, y+5, z+6, 18)
mc.setBlocks(x-5, y+6, z-5, x+5, y+6, z+5, 18)
mc.setBlocks(x-4, y+7, z-4, x+4, y+7, z+4, 18)
mc.setBlocks(x-3, y+8, z-3, x+3, y+8, z+3, 18)
mc.setBlocks(x-2, y+9, z-2, x+2, y+9, z+2, 18)
#front step
mc.setBlocks(x, y, z-5, x, y, z-5, 67, 2)
#BED
mc.setBlocks(x-4, y+1, z+3, x-4, y+1, z+4, 26)
#books
mc.setBlocks(x+4, y+1, z-4, x+4, y+2, z-3, 47)
#torches
mc.setBlocks(x, y+3, z-4, x, y+3, z-4, 50, 4)
mc.setBlocks(x, y+3, z+4, x, y+3, z+4, 50, 4)
#cobwabe
mc.setBlocks(x+4, y+4, z+4, x+4, y+4, z+4, 30)
#CHEST
mc.setBlocks(x+4, y+1, z-2, x+4, y+1, z-2, 54, 4)#chim stack
mc.setBlocks(x, y+2, z+2, x, y+11, z+2, 4)
#roof
mc.setBlocks(x-6, y+5, z-6, x+6, y+5, z+6, 18)
mc.setBlocks(x-5, y+6, z-5, x+5, y+6, z+5, 18)
mc.setBlocks(x-4, y+7, z-4, x+4, y+7, z+4, 18)
mc.setBlocks(x-3, y+8, z-3, x+3, y+8, z+3, 18)
mc.setBlocks(x-2, y+9, z-2, x+2, y+9, z+2, 18)
#front step
mc.setBlocks(x, y, z-5, x, y, z-5, 67, 2)
#BED
mc.setBlocks(x-4, y+1, z+3, x-4, y+1, z+4, 26)
#books
mc.setBlocks(x+4, y+1, z-4, x+4, y+2, z-3, 47)
#torches
mc.setBlocks(x, y+3, z-4, x, y+3, z-4, 50, 4)
mc.setBlocks(x, y+3, z+4, x, y+3, z+4, 50, 4)
#cobwabe
mc.setBlocks(x+4, y+4, z+4, x+4, y+4, z+4, 30)
#CHEST
mc.setBlocks(x+4, y+1, z-2, x+4, y+1, z-2, 54, 4)