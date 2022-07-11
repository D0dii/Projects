import pygame,sys,random,time
#colors
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)
blue = pygame.Color(0,0,255)
#window size
frame_size_x = 800
frame_size_y = 700
#game window
pygame.display.set_caption("Falling stars")
game_window = pygame.display.set_mode(size=(frame_size_x,frame_size_y))
#other
size = 50
position_x = frame_size_x/2
position_y = frame_size_y - size
fps_controller = pygame.time.Clock()



#player
class Player:
    def __init__(self,position_x,position_y,size,color):
        self.position_x = position_x
        self.position_y = position_y
        self.size = size
        self.color = color
    def draw_player(self):
        pygame.draw.rect(game_window,self.color,pygame.Rect(self.position_x,self.position_y,self.size,self.size))

#stars
class Star:
    def __init__(self,star_pos_x,star_pos_y,star_size,star_color):
        self.star_pos_x = star_pos_x
        self.star_pos_y = star_pos_y
        self.star_size = star_size
        self.star_color = star_color
    def draw_star(self):
        pygame.draw.rect(game_window,self.star_color,pygame.Rect(self.star_pos_x,self.star_pos_y,self.star_size,self.star_size))




def game():
    player = Player(position_x,position_y,size,red)
    stars = []
    star_y = -300
    for a in range(1,7):
        stars.append(Star((random.randint(0,frame_size_x)//size)*size,star_y,size,blue))
        star_y += 50
    game = True
    score = 0
    speed = 50
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT or event.key == ord("d")) and player.position_x < frame_size_x - size:
                    player.position_x += size
                elif (event.key == pygame.K_LEFT or event.key == ord("a")) and player.position_x > 0:
                    player.position_x -= size



        game_window.fill(black)
        player.draw_player()
        for a in stars:
            a.draw_star()
            a.star_pos_y += speed
            if a.star_pos_y > frame_size_y:
                score += 1
                a.star_pos_y = 0
                a.star_pos_x = (random.randint(0,frame_size_x)//size) * size
            elif a.star_pos_y == player.position_y and a.star_pos_x == player.position_x:
                game = False
            
        
        pygame.display.update()
        fps_controller.tick(15)

    print("U LOST")
    print(score)
    pygame.quit()
    sys.exit()
    

game()