import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mareks Ciguzis 211RDB274")
background = pygame.image.load("wall.jpg")
button = pygame.image.load("button.png")
# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

# Define font
font = pygame.font.Font(None, 36)


replaynumbers = [3, 5, 6, 3, 6, 3, 8, 9]
numbers = replaynumbers.copy()
player_turn = None
player1_score = 0
player2_score = 0
game_over = False

Sum = pygame.Rect(screen.get_width() // 3 - 50, 350, 100, 50)
Subt = pygame.Rect(2 * screen.get_width() // 3 - 50, 350, 100, 50)


def draw_board(numbers):
    x = 250
    y = 100

    Sum_button = pygame.draw.rect(screen, (255, 0, 0), (600, 300, 100, 50))
    Sub_button = pygame.draw.rect(screen, (255, 0, 0), (300, 300, 100, 50))
    Sum_text = font.render("-", True, (255, 255, 255))
    Sub_text = font.render("+", True, (255, 255, 255))
    Sum_text_rect = Sum_text.get_rect(center=Sum_button.center)
    Sub_text_rect = Sub_text.get_rect(center=Sub_button.center)
    screen.blit(Sum_text, Sum_text_rect)
    screen.blit(Sub_text, Sub_text_rect)

    for i in range(len(numbers)):
        temp_surf = pygame.Surface((50, 50), pygame.SRCALPHA)
        temp_surf.fill((255, 255, 255, 0))
        num_surf = font.render(str(numbers[i]), True, black)
        num_rect = num_surf.get_rect(center=(25, 25))
        temp_surf.blit(num_surf, num_rect)
        screen.blit(temp_surf, (x, y))
        x += 60


# Start screen


def start_screen():
    screen.blit(background, (0, 0))
    text = font.render("SumSub Game", True, black)
    text_rect = text.get_rect()
    text_rect.center = (screen.get_width() // 2, 100)
    screen.blit(text, text_rect)

    p1_text = font.render("Choose Who Does First Move", True, black)
    p1_rect = p1_text.get_rect()
    p1_rect.center = (screen.get_width() // 2, 250)
    screen.blit(p1_text, p1_rect)

    p1_button_rect = pygame.Rect(screen.get_width() // 3 - 50, 350, 100, 50)
    pygame.draw.rect(screen, black, p1_button_rect)

    p2_button_rect = pygame.Rect(2 * screen.get_width() // 3 - 50, 350, 100, 50)
    pygame.draw.rect(screen, black, p2_button_rect)

    p1_button_text = font.render("Player", True, white)
    p1_button_text_rect = p1_button_text.get_rect()
    p1_button_text_rect.center = p1_button_rect.center
    screen.blit(p1_button_text, p1_button_text_rect)

    p2_button_text = font.render("AI", True, white)
    p2_button_text_rect = p2_button_text.get_rect()
    p2_button_text_rect.center = p2_button_rect.center
    screen.blit(p2_button_text, p2_button_text_rect)

    pygame.display.flip()


def check_score(board):
    if board[0] == 1:
        # print("Player 1 ")
        return -1
    elif board[0] == -1:
        # print("Player 2 ")
        return 1
    else:
        return 0

#Minimax algorithm
def check_game_over(board):
    global game_over
    if board[0] == 1:
        print("Player wins!")
        game_over = True
    elif board[0] == -1:
        print("AI wins!")
        game_over = True
    elif len(board) == 1:
        print("Tie!")
        game_over = True


def minimax(board, depth, ismaximizing):
    status = None
    if board[0] == -1:
        print("checking numbers: ", board, " depth: ", depth, "ismaxing?: ", ismaximizing)
    status = check_score(board)
    maxdepth = 20
    if depth == maxdepth:
        return 0
    if status is not None:
        # print(status)
        return status

    if (ismaximizing):
        bestscore = -1000
        # print("Maxing")
        for i in range(2):
            # print(i)
            new_board = board[:]
            if i == 0:
                new_board[0] += new_board[1]
            elif i == 1:
                new_board[0] -= new_board[1]
            new_board.pop(1)
            # print(board)
            score = minimax(new_board, depth + 1, False)
            print("bs: ", bestscore, "board: ", new_board)
            if score is not None:
                bestscore = max(bestscore, score)

        return bestscore

    else:
        # print("Mining")
        bestscore = 1000
        for i in range(2):
            print(i)
            new_board = board.copy()
            if i == 0:
                new_board[0] += new_board[1]
            else:
                new_board[0] -= new_board[1]
            new_board.pop(1)
            score = minimax(board, depth + 1, True) * -1
            bestscore = min(bestscore, score)
            print("bs in not max: ", bestscore, "board: ", new_board)
        return bestscore


def best_move(board):
    best_score = None
    best_movee = None
    for i in range(2):
        print(i)
        new_board = board[:]
        if i == 0:
            new_board[0] += new_board[1]
            new_board.pop(1)
            # print(new_board)
            score1 = minimax(new_board, 0, False)
        else:
            new_board[0] -= new_board[1]
            new_board.pop(1)
            score2 = minimax(new_board, 0, False)
    if score1 > score2:
        best_movee = 1
    else:
        best_movee = 2

    return best_movee
# End of Minimax



p1_button_rect = pygame.Rect(screen.get_width() // 3 - 50, 350, 100, 50)
p2_button_rect = pygame.Rect(2 * screen.get_width() // 3 - 50, 350, 100, 50)

Sum_button_rect = pygame.Rect(600, 300, 100, 50)
Sub_button_rect = pygame.Rect(300, 300, 100, 50)
startingscreen = True


def scoreboard(numbers):
    screen.blit(background, (0, 0))
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        # Check if Player 1 has won the game
        number = font.render(str(numbers[0]), True, (0, 0, 0))
        if numbers[0] == 1:
            text = font.render("Player  wins!", True, (0, 0, 0))
        elif numbers[0] == -1:
            text = font.render("AI wins!", True, (0, 0, 0))
        else:
            text = font.render("Tie!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2 - 150))
        number_rect = number.get_rect(center=(screen_width / 2, screen_height / 2 - 125))
        screen.blit(text, text_rect)
        screen.blit(number, number_rect)
        pygame.display.update()

        # Add an "Exit" button
        replay_button = pygame.draw.rect(screen, (255, 0, 0), (600, 300, 100, 50))
        exit_button = pygame.draw.rect(screen, (255, 0, 0), (300, 300, 100, 50))
        exit_text = font.render("Exit", True, (255, 255, 255))
        replay_text = font.render("Replay", True, (255, 255, 255))
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        replay_text_rect = replay_text.get_rect(center=replay_button.center)
        screen.blit(exit_text, exit_text_rect)
        screen.blit(replay_text, replay_text_rect)


        mouse_pos = pygame.mouse.get_pos()
        if exit_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                break
        elif replay_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                print("replay")
                gameplay()


def gameplay():
    numbers = replaynumbers.copy()
    global game_over
    game_over = False
    startingscreen = True
    while not game_over:
        screen.blit(background, (0, 0))
        check_game_over(numbers)
        while startingscreen:
            start_screen()
            pygame.draw.rect(screen, black, p1_button_rect)
            pygame.draw.rect(screen, black, p2_button_rect)
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if p1_button_rect.collidepoint(event.pos):
                        player_turn = 1
                        startingscreen = False
                    elif p2_button_rect.collidepoint(event.pos):
                        player_turn = 2
                        startingscreen = False


        pygame.draw.rect(screen, black, Sum_button_rect)
        pygame.draw.rect(screen, black, Sub_button_rect)

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Sub_button_rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        numbers[0] = numbers[0] + numbers[1]
                        del numbers[1]
                        pygame.time.wait(100)
                if Sum_button_rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        numbers[0] = numbers[0] - numbers[1]
                        del numbers[1]
                        pygame.time.wait(100)
                check_game_over(numbers)
                player_turn = 2

                if len(numbers) == 1:
                    check_game_over(numbers)
                    if game_over:
                        scoreboard(numbers)
                    if game_over:
                        break
                else:
                    continue
        check_game_over(numbers)
        if game_over:
            scoreboard(numbers)


        if player_turn == 2 and not game_over:

            board_copy = numbers.copy()
            bot_move = best_move(board_copy)
            if bot_move == 1:
                numbers[0] = numbers[0] + numbers[1]
                print("Bot Summed")
                del numbers[1]
            elif bot_move == 2:
                print("Bot Subtracted")
                numbers[0] = numbers[0] - numbers[1]
                del numbers[1]

            else:
                print("Computer Is Lost")

        check_game_over(numbers)

        if game_over:
            scoreboard(numbers)
        player_turn = 1

        screen.blit(background, (0, 0))
        draw_board(numbers)

        pygame.display.update()

gameplay()

pygame.quit()
