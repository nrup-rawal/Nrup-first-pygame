import pygame
import random
pygame.init()

#colors
white = (255,255,255)
red =  (255,0,0)
black = (0,0,0)


#creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))


#setting title
pygame.display.set_caption("Snake Game with Nrup")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)





def score_on_screen(text, color, x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])



def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        score_on_screen("Welcome to Snake Game with Nrup", black, 100,250)
        score_on_screen("Press spacebar to play", black, 100,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit_game= True 
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   gameloop()

        pygame.display.update()
        clock.tick(60)


#game loop

def gameloop():
    #game specific variables
    exit_game= False
    game_over= False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    fps = 60
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1

    food_x = random.randint(50,screen_width/1.5)
    food_y = random.randint(50,screen_height/1.5)
    score = 0
    init_velocity = 5
    

    with open("highscore.txt", "r") as f:
        highscore= f.read()

    
    
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            score_on_screen("Game over!! Press Enter to Continue",red, 100,250)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y =  + init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_LSHIFT:
                        score += 1
            
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<11 and abs(snake_y - food_y)<11:
                score += 1
                food_x = random.randint(50,screen_width/1.5)
                food_y = random.randint(50,screen_height/1.5)
                snake_length += 5
                if score>int(highscore):
                    highscore = score
                
                

            gameWindow.fill(white)
            score_on_screen("Score: "+ str(score) + "    Highscore: " + str(highscore), red , 5,5)
            

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            
            if head in snake_list[:-1]:
                game_over = True


            if snake_x<0 or snake_x> screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snake_list, snake_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()


