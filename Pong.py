# Importing libraries
import pygame
import random
import time

# Initializing PyGame
pygame.init()

# Setting a window name
pygame.display.set_caption("Ping Pong")

# Creating a font
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)
pong_font = pygame.font.SysFont("Arial", 75)
winner_font = pygame.font.SysFont("Arial", 50)

# Set the height and width of the screen
window_width = 700
window_height = 500
size = [window_width, window_height]
game_win = pygame.display.set_mode(size)
game_win2 = pygame.display.set_mode(size)


# Creating a messaging system
def message(sentence, color, x, y, font_type, display):
    sentence = font_type.render(sentence, True, color)
    display.blit(sentence, [x, y])


# Creating colors
white = (225, 225, 225)
black = (0, 0, 0)
gray = (100, 100, 100)

# Setting up ball
ball_size = 25


class Ball:
    """
    Class to keep track of a ball's location and vector.
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0


def make_ball():
    ball = Ball()
    # Starting position of the ball.
    ball.x = 350
    ball.y = 250

    # Speed and direction of rectangle
    ball.change_x = 5
    ball.change_y = 5

    return ball


def main():
    # Scores
    left_score = 0
    right_score = 0

    pygame.init()

    # Loop until the user clicks the close button.
    done = False

    ball_list = []

    ball = make_ball()
    ball_list.append(ball)

    # Right paddle coordinates
    y = 200
    y_change = 0
    x = 50
    # Left paddle coordinates
    y1 = 200
    y1_change = 0
    x1 = 650

    while not done:
        
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -7

                elif event.key == pygame.K_s:
                    y_change = 7

                elif event.key == pygame.K_UP:
                    y1_change = -7

                elif event.key == pygame.K_DOWN:
                    y1_change = 7

            elif event.type == pygame.KEYUP:
                y_change = 0
                y1_change = 0

        y += y_change
        y1 += y1_change

        # Preventing from letting the paddle go off screen
        if y > window_height - 100:
            y -= 10
        if y < 50:
            y += 10
        if y1 > window_height - 100:
            y1 -= 10
        if y1 < 50:
            y1 += 10

        # Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y

            # Bounce the ball if needed
            if ball.y > 500 - ball_size or ball.y < ball_size:
                ball.change_y *= -1
            if ball.x > window_width - ball_size:
                ball.change_x *= -1
                left_score += 1
            if ball.x < ball_size:
                ball.change_x *= -1
                right_score += 1

            ball_rect = pygame.Rect(ball.x - ball_size, ball.y - ball_size, ball_size * 2, ball_size * 2)

            left_paddle_rect = pygame.Rect(x, y, 25, 75)
            if ball.change_x < 0 and ball_rect.colliderect(left_paddle_rect):
                ball.change_x = abs(ball.change_x)

            right_paddle_rect = pygame.Rect(x1, y1, 25, 75)
            if ball.change_x > 0 and ball_rect.colliderect(right_paddle_rect):
                ball.change_x = -abs(ball.change_x)

            if right_score == 10:
                message("RIGHT PLAYER HAS WON!!", white, 90, 220, winner_font, game_win)
                pygame.display.flip()
                pygame.event.poll()
                time.sleep(5)
                pygame.quit()
                quit()
            elif left_score == 10:
                message("LEFT PLAYER HAS WON!!", white, 90, 220, winner_font, game_win)
                pygame.display.flip()
                pygame.event.poll()
                time.sleep(5)
                pygame.quit()
                quit()

        # Drawing
        # Set the screen background
        game_win.fill(black)

        # Draw the balls
        for ball in ball_list:
            pygame.draw.circle(game_win, white, [ball.x, ball.y], ball_size)

        # Creating Scoreboard
        message("Left player score: " + str(left_score), white, 10, 10, font, game_win)
        message("Right player score: " + str(right_score), white, 450, 10, font, game_win)

        # Drawing a left paddle
        pygame.draw.rect(game_win, white, [x, y, 25, 100])
        # Drawing a right paddle
        pygame.draw.rect(game_win, white, [x1, y1, 25, 100])

        # Setting FPS
        FPS = pygame.time.Clock()
        FPS.tick(60)

        # Updating so actions take place
        pygame.display.flip()


while True:
    game_win2.fill(black)
    pygame.event.poll()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    message("Pong", white, 280, 100, pong_font, game_win2)
    if 150 + 100 > mouse[0] > 150 and 350 + 50 > mouse[1] > 350:
        pygame.draw.rect(game_win, gray, [150, 350, 100, 50])
        if click[0] == 1:
            break
    else:
        pygame.draw.rect(game_win, white, [150, 350, 100, 50])

    if 450 + 100 > mouse[0] > 450 and 350 + 50 > mouse[1] > 350:
        pygame.draw.rect(game_win, gray, [450, 350, 100, 50])
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(game_win, white, [450, 350, 100, 50])

    message("Start", black, 175, 357, font, game_win2)
    message("Quit", black, 475, 357, font, game_win2)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Wrap-up
    # Limit to 60 frames per second
    clock = pygame.time.Clock()
    clock.tick(60)

if __name__ == "__main__":
    main()
