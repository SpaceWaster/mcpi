from mcpi.minecraft import Minecraft

def init():
    mc = Minecraft.create ("192.162.7.97", 4711)
	#x, y, z = mc.player.getPos()        
    return mc


	

#default ip ("172.0.0.1")
#IANS IP 192.162.7.96
#colemans IP 192.162.7.226

mc = Minecraft.create()   
mc.postToChat("this is trenton and 42")
