import Fusion
import pygame 
import time 

f = Fusion.driver()

def liveUpdate (address):
    value = f.i2cRead(address, 0x80, 0x10)
    value += f.i2cRead(address, 0x90, 0x10)
    value += f.i2cRead(address, 0xA0, 0x10)
    value += f.i2cRead(address, 0xB0, 0x10)
    value += f.i2cRead(address, 0xC0, 0x10)
    value += f.i2cRead(address, 0xD0, 0x10)
    value += f.i2cRead(address, 0xE0, 0x10)
    value += f.i2cRead(address, 0xF0, 0x10)
    return value


factor = 3

size = width, height= 128*factor, 256
main = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
screen = pygame.Surface(size)

while True:
    temp = liveUpdate(0x40)
    screen.fill([0,0,0])
    
    for i in range(len(temp)):
        if (i == 0):
            pygame.draw.line(screen, 0xffffff, [0,0], [0, temp[i]], 1)
        else:
            pygame.draw.line(screen, 0xffffff, [(i-1)*factor, (temp[i-1])], [i*factor, temp[i]], 1)
    main.blit(screen, [0,0])
    pygame.display.flip()
    print "length = " + str(len(temp))
    print temp
    #while True: pass
