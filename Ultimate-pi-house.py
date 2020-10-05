#Ultimate PI House
from mcpi import minecraft
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
#basement
mc.setBlocks(x+7, y-1, z-2, x-13, y-6, z+5, 7)
#hollow out basement
mc.setBlocks(x+6, y-2, z-1, x-12, y-5, z+3, 0)
#house
mc.setBlocks(x-7, y, z-5, x+7, y+4, z+5, 5)
#change shape
mc.setBlocks(x+5, y, z-3, x+7, y+4, z-5, 0)
#hollows out house
mc.setBlocks(x-6, y+1, z-4, x+3, y+4, z+4, 0)
mc.setBlocks(x-6, y+1, z-1, x+6, y+4, z+4, 0)
#makes door
mc.setBlocks(x-4, y+1, z-5, x-4, y+2, z-5, 0)
mc.setBlocks(x-4, y+1, z-5, x-4, y+2, z-5, 64)
#front step
mc.setBlocks(x-3, y, z-8, x-5, y, z-8, 53, 2)
mc.setBlocks(x-2, y, z-6, x-6, y, z-7, 5)
mc.setBlocks(x-2, y+1, z-6, x-2, y+1, z-7, 85)
mc.setBlocks(x-6, y+1, z-6, x-6, y+1, z-7, 85)
mc.setBlocks(x-2, y, z-8, x-2, y, z-8, 37)
mc.setBlocks(x-6, y, z-8, x-6, y, z-8, 37)
#windows
mc.setBlocks(x-6, y+2, z-5, x-6, y+3, z-5, 102)
mc.setBlocks(x-2, y+2, z-5, x+2, y+3, z-5, 102)
mc.setBlocks(x+5, y+2, z+5, x+4, y+3, z+5, 102)
mc.setBlocks(x+5, y+2, z-2, x+5, y+3, z-2, 102)
mc.setBlocks(x-4, y+2, z+5, x-2, y+3, z+5, 102)
#roof
mc.setBlocks(x-7, y+5, z-6, x+4, y+5, z+6, 18, 1)
mc.setBlocks(x-7, y+6, z-5, x+4, y+6, z+5, 18, 1)
mc.setBlocks(x-7, y+7, z-4, x+4, y+7, z+4, 18, 1)
mc.setBlocks(x-7, y+8, z-3, x+4, y+8, z+3, 18, 1)
#small roof
mc.setBlocks(x+5, y+5, z-3, x+7, y+5, z+6, 18, 1)
mc.setBlocks(x+5, y+6, z-2, x+7, y+6, z+5, 18, 1)
mc.setBlocks(x+5, y+7, z-1, x+7, y+7, z+4, 18, 1)
mc.setBlocks(x+5, y+8, z  , x+7, y+8, z+3, 18, 1)
#chim base
mc.setBlocks(x+6, y, z  , x+8, y+2, z+3, 43, 3)
mc.setBlocks(x+7, y+3, z+1  , x+8, y+10, z+2, 43, 3)
mc.setBlocks(x+6, y+3, z+1  , x+6, y+7, z+2, 43, 3)
mc.setBlocks(x+8, y+3, z    , x+8, y+3, z  , 67, 2)
mc.setBlocks(x+8, y+3, z+3  , x+8, y+3, z+3, 67, 3)
mc.setBlocks(x+6, y+3, z    , x+6, y+3, z  , 67, 2)
mc.setBlocks(x+6, y+3, z+3  , x+6, y+3, z+3, 67, 3)
#chim smoke
mc.setBlocks(x+8, y+12, z+2  , x+8, y+12, z+2, 35, 0)
mc.setBlocks(x+10, y+14, z+2 , x+10, y+14, z+2, 35, 0)
mc.setBlocks(x+8, y+16, z+1  , x+8, y+16, z+1, 35, 0)
#double oven
mc.setBlocks(x+6, y+2, z+1  , x+6, y+2, z+2, 62, 4)
#kitchen
mc.setBlocks(x+6, y+1, z-1  , x+4, y+1, z-1, 58)
mc.setBlocks(x+6, y+1, z+4  , x+3, y+1, z+4, 58)
mc.setBlocks(x+4, y+2, z-1  , x+4, y+2, z-1, 40)
mc.setBlocks(x+6, y+2, z+4  , x+6, y+2, z+4, 39)
#kitchen floor
mc.setBlocks(x+4, y, z-1, x+6, y, z+4, 35, 0)
#table
mc.setBlocks(x, y+1, z-4, x, y+1, z-4, 43, 6)
mc.setBlocks(x-1, y+2, z-4, x+1, y+2, z-3, 44, 6)
mc.setBlocks(x-3, y+1, z-4, x-3, y+1, z-3, 53, 4)
mc.setBlocks(x+3, y+1, z-4, x+3, y+1, z-3, 53, 5)
#living room
mc.setBlocks(x-5, y+1, z+4, x-5, y+1, z+4, 54, 3)
mc.setBlocks(x-1, y+1, z+4, x-1, y+1, z+4, 54, 3)
mc.setBlocks(x-4, y+1, z+4, x-2, y+1, z+4, 67, 2)
mc.setBlocks(x, y+1, z+2, x, y+1, z+1, 67, 0)
#books
mc.setBlocks(x-6, y+1, z+2, x-6, y+2, z, 47)
#lights
mc.setBlocks(x-5, y+3, z+4, x-5, y+3, z+4, 50, 3)
mc.setBlocks(x-1, y+3, z+4, x-1, y+3, z+4, 50, 3)
mc.setBlocks(x-3, y+3, z-4, x-3, y+3, z-4, 50, 4)
mc.setBlocks(x-5, y+3, z-4, x-5, y+3, z-4, 50, 4)
#bedroom
mc.setBlocks(x-8, y, z-3, x-13, y+4, z+5, 5)
#hollows out bedroom
mc.setBlocks(x-8, y+1, z-2, x-12, y+4, z+4, 0)
mc.setBlocks(x-7, y+1, z-2, x-7, y+3, z-1, 0)
#bed roof
mc.setBlocks(x-8, y+5, z-4, x-13, y+5, z+6, 18, 1)
mc.setBlocks(x-8, y+6, z-3, x-13, y+6, z+5, 18, 1)
mc.setBlocks(x-8, y+7, z-2, x-13, y+7, z+4, 18, 1)
# bed windows
mc.setBlocks(x-9, y+2, z-3, x-11, y+3, z-3, 102)
mc.setBlocks(x-13, y+2, z, x-13, y+3, z+2, 102)
#bed floor
mc.setBlocks(x-8, y, z-2, x-12, y, z+4, 35, 7)
#bed
mc.setBlocks(x-10, y+1, z+4, x-10, y+1, z+3, 26)
mc.setBlocks(x-8, y+1, z+4, x-8, y+2, z+4, 47)
mc.setBlocks(x-12, y+1, z+4, x-12, y+2, z+4, 47)
mc.setBlocks(x-12, y+1, z-1, x-12, y+1, z-2, 54, 4)
#bed lights
mc.setBlocks(x-9, y+3, z+4, x-9, y+3, z+4, 50, 3)
mc.setBlocks(x-11, y+3, z+4, x-11, y+3, z+4, 50, 3)
mc.setBlocks(x-8, y+3, z, x-8, y+3, z, 50, 3)
#bed chair
mc.setBlocks(x-8, y+1, z+2, x-8, y+1, z+1, 67, 0)
#bush
mc.setBlocks(x-14, y, z-2, x-14, y, z+4, 6, 2)
#tunnel
mc.setBlocks(x+6, y+1, z-1, x+6, y-2, z-1, 0)
#basement light
mc.setBlocks(x+6, y-3, z, x+6, y-3, z+2, 50)
mc.setBlocks(x-12, y-3, z, x-12, y-3, z+2, 50)
mc.setBlocks(x+6, y-4, z-1, x-12, y-5, z+3, 9, 0)
mc.setBlocks(x+4, y-4, z-1, x+4, y-4, z+3, 67, 0)
mc.setBlocks(x+3, y-5, z-1, x+3, y-5, z+3, 67, 0)
mc.setBlocks(x-10, y-4, z-1, x-10, y-4, z+3, 67, 1)
mc.setBlocks(x-9, y-5, z-1, x-9, y-5, z+3, 67, 1)
mc.setBlocks(x+6, y-4, z-1, x+5, y-5, z+3, 1)
mc.setBlocks(x-12, y-4, z-1, x-11, y-5, z+3, 1)
mc.setBlocks(x+6, y-4, z+1, x-12, y-4, z+1, 1)