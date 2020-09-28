# TNT Run
# import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
import time
air=0
tnt=46
REDSTONE_ORE=73
BEDROCK_INVISIBLE=95
GLOWING_OBSIDIAN=246
NETHER_REACTOR=247
# connect with the Minecraft world
mc=Minecraft.create()
# get the player’s position
pos=mc.player.getTilePos()
# check if the end of the world will engulf your creation and move you if you’re too close
#if pos.z<-40:
#mc.postToChat(
#'teleporting to safer distance in progress!')
# mc.player.setPos(pos.x,pos.y,-40)
# pos=mc.player.getTilePos()
# mark where the teleport is
zpos=pos.z-40
# create the valley by hollowing it out with air
mc.setBlocks(pos.x-1,pos.y+3,pos.z,pos.x+1,pos.y-7,pos.z-88,0)
# build the invisible bedrock support
mc.setBlocks(pos.x,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,95)
mc.setBlocks(pos.x-1,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,95)
mc.setBlocks(pos.x+1,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,95)
mc.setBlocks(pos.x,pos.y-1,pos.z-88,pos.x-1,pos.y-7,pos.z-88,95)
mc.setBlocks(pos.x-1,pos.y-1,pos.z-88,pos.x,pos.y-7,pos.z-88,95)
mc.setBlocks(pos.x+1,pos.y-1,pos.z-88,pos.x,pos.y-7,pos.z-88,95)
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y-7,pos.z-92,95)
# build the bomb
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y,pos.z-88,46,1)
# build the end podium
mc.setBlocks(pos.x-2,pos.y,pos.z-93,pos.x+2,pos.y,pos.z-97,246)
mc.setBlocks(pos.x-1,pos.y+1,pos.z-94,pos.x+1,pos.y+1,pos.z-96,247,1)
mc.setBlock(pos.x,pos.y+2,pos.z-95,73)
# set how many teleports you have
teleport=1
# build the display teleport signal block
mc.setBlock(pos.x+1,pos.y+1,pos.z-44,247,2)
mc.setBlock(pos.x-1,pos.y+1,pos.z-44,247,2)
# teleport player when at a certain position
#while teleport ==1:
# pos=mc.player.getTilePos()
# if pos.z==zpos:
# mc.player.setPos(pos.x,pos.y,pos.z-24)
# teleport=0