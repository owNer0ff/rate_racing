import pygame


# отрисовка курсора
def draw_cursor(screen, x, y):
    screen.blit(cursor, (x, y - 48))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Rate Racing.exe')
    pygame.display.set_icon(pygame.image.load('images/icon.jpg'))
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

# курсор
pygame.mouse.set_visible(False)
cursor = pygame.image.load('images/cursor.png')
# музыка
pygame.mixer.music.load('sounds/sound_1.mp3')
pygame.mixer.music.play(-1)
# стартовый экран
img_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
             '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47']
all_imgs = {}
for img in img_names:
    all_imgs[img] = pygame.image.load('images/road_animation/' + img + '.gif')
# start_display = pygame.image.load('images/road.gif')
# start_display_rect = start_display.get_rect()
play_btn = pygame.image.load('images/start_btn1.png')
play_btn_rect = play_btn.get_rect(center=(260, 450))
exit_btn = pygame.image.load('images/exit_btn1.png')
exit_btn_rect = exit_btn.get_rect(center=(550, 456))
# игровой цикл
img = 0
fps = 60
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(all_imgs[str(img)], all_imgs[str(img)].get_rect())
    img += 1
    if img >= 47:
        img = 0
    # screen.blit(start_display, start_display_rect)
    screen.blit(play_btn, play_btn_rect)
    screen.blit(exit_btn, exit_btn_rect)
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    draw_cursor(screen, x, y)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
