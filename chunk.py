from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()

def init():
    mc = Minecraft.create("192.162.7.117", 4711)
                                            
x, y, z = mc.player.getPos()  

mc.setBlocks(x,y, z, x+50, y-100, z+50, block.AIR.id)


#made by Trenton Zavala
