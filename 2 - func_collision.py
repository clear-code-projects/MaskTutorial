import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

moving_surf = pygame.Surface((50,50))
moving_rect = moving_surf.get_rect(center = (300,300))
obstacle_surf = pygame.image.load('alpha.png').convert_alpha()
obstalce_pos = (100,100)

# mask 
moving_mask = pygame.mask.from_surface(moving_surf)
obstacle_mask = pygame.mask.from_surface(obstacle_surf)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('white')

	# obstacle 
	screen.blit(obstacle_surf,obstalce_pos)
	
	# moving part
	if pygame.mouse.get_pos(): moving_rect.center = pygame.mouse.get_pos()
	screen.blit(moving_surf,moving_rect)

	# offset
	offset_x = obstalce_pos[0] - moving_rect.left
	offset_y = obstalce_pos[1] - moving_rect.top
	
	# collision 1 point
	if moving_mask.overlap(obstacle_mask,(offset_x,offset_y)):
		moving_surf.fill('red')
		# print(moving_mask.overlap(obstacle_mask,(offset_x,offset_y)))
	else:
		moving_surf.fill('green')

	# # collision area
	# if moving_mask.overlap_area(obstacle_mask,(offset_x,offset_y)) > 500:
	# 	moving_surf.fill('red')
	# 	#print(moving_mask.overlap_area(obstacle_mask,(offset_x,offset_y)))
	# else:
	# 	moving_surf.fill('green')

	pygame.display.update()
	clock.tick(60)