import pygame
import pygame.draw
import pygame.colordict
from freepygame import freetext, freebutton
import time

pygame.init()
frame_number = 60
display_size = (1920, 1080)
pygame.display.set_caption("The beauty of mathematics")
pygame.display.set_icon(pygame.image.load("assets\\_.ico"))
screen = pygame.display.set_mode(display_size, pygame.FULLSCREEN | pygame.HWSURFACE)
screen.fill(pygame.colordict.THECOLORS.get("grey0"))
buffer = pygame.Surface(display_size)
clock = pygame.time.Clock()

event_text = freetext.SuperText(screen, [3, 5], "", "assets\\simhei.ttf", size = 10,
	                                color = pygame.colordict.THECOLORS.get("grey70"))
button_exit = freebutton.FreeButton(screen, [display_size[0] - 80, 0], [80, 40], "EXIT", "assets\\simhei.ttf",
	                                    border_color = pygame.colordict.THECOLORS.get("grey50"), draw_border = True, msg_tran = True, dsm = 1)

while True:
    event_text.set_msg("现在时间：" + str(time.localtime().tm_year) + "年 " + str(time.localtime().tm_mon) + "月 " +
	                   str(time.localtime().tm_mday) + "日 " + str(time.localtime().tm_hour) + "时 " +
					   str(time.localtime().tm_min) + "分 " + str(time.localtime().tm_sec) + "秒   " +
					   "当前帧速率 " + str(int(clock.get_fps())) + "     Copyright (c) 2023 freebird")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif freebutton.position_button_class(button_exit, pygame.mouse.get_pos()) is True:
            button_exit.set_msg_color(pygame.colordict.THECOLORS.get("grey95"))
            button_exit.check_button = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                exit()
        else:
            button_exit.check_button = False
        if event.type == pygame.WINDOWLEAVE:
            button_exit.check_button = False
            
    if button_exit.check_button is False:
        button_exit.set_msg_color(pygame.colordict.THECOLORS.get("grey75"))
    button_exit.draw()
            
    event_text.draw()
    button_exit.draw()
    pygame.display.flip()
    screen.fill(pygame.colordict.THECOLORS.get("grey0"))
    clock.tick(frame_number)
