import sys, pygame, random, math
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.jpg")
ballrect = ball.get_rect()
ballrect = ballrect.move(50,50)

paddle1 = pygame.image.load("paddle.jpg")
pdl1rect = paddle1.get_rect()


paddle2 = pygame.image.load("paddle.jpg")
pdl2rect = paddle2.get_rect()
pdl2rect = pdl2rect.move(width - pdl2rect.width,0)


def EnemyScore(ballrect):
	print "He scored."
	ballrect.center = [width/2, height/2]

def YouScore(ballrect):
	print "You scored."
	ballrect.center = [width/2, height/2]

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)

	# Someone got a point
	if ballrect.left < 0:
		EnemyScore(ballrect)
	if ballrect.right > width:
		YouScore(ballrect)

	# Ball colliding with top or bottom
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	# Ball colliding with a paddle
	if pdl1rect.colliderect(ballrect) or pdl2rect.colliderect(ballrect):
		speed[0] = -speed[0]

	# Enemy paddle movement
	difference = ballrect.center[1] - pdl2rect.center[1]
	if difference != 0:
		pdl2rect.move(0, difference / math.fabs(difference))

	screen.fill(black)
	screen.blit(ball, ballrect)
	screen.blit(paddle1, pdl1rect)
	screen.blit(paddle2, pdl2rect)
	pygame.display.flip()

