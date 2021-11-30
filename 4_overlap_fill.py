import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

# ship setup
ship_surf = pygame.image.load('ship.png').convert_alpha()
ship_overlay_surf = pygame.image.load('ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (300,300))
ship_mask = pygame.mask.from_surface(ship_surf)

# obstacle setup
obstacle_surf = pygame.image.load('alpha.png').convert_alpha()
obstacle_pos = (100,100)
obstacle_mask = pygame.mask.from_surface(obstacle_surf)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('white')

	# obstacle 
	screen.blit(obstacle_surf,obstacle_pos)
	
	# moving part
	if pygame.mouse.get_pos():ship_rect.center = pygame.mouse.get_pos()
	screen.blit(ship_surf,ship_rect)
	
	# mask coloring 
	offset_x = obstacle_pos[0] - ship_rect.left
	offset_y = obstacle_pos[1] - ship_rect.top
	if ship_mask.overlap(obstacle_mask,(offset_x,offset_y)):
		new_mask = ship_mask.overlap_mask(obstacle_mask,(offset_x,offset_y))
		new_surf = new_mask.to_surface()
		new_surf.set_colorkey((0,0,0))

		surf_w, surf_h = new_surf.get_size()
		for x in range(surf_w):
			for y in range(surf_h):
				if new_surf.get_at((x,y))[0] != 0:
					new_surf.set_at((x,y),'orange')
		screen.blit(new_surf,ship_rect)


	pygame.display.update()
	clock.tick(60)