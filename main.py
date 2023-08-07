# CHESS GAME

import pygame

# pygame setup
pygame.init()  # initializing package
pygame.display.set_caption('Chess')
display_width = 1000
display_height = 700
screen = pygame.display.set_mode([display_width, display_height])
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60


# chess variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

# 0 - whites turn no selection:
# 1-whites turn piece selected:
# 2- black turn no selection:
# 3 - black turn piece selected:

turn_step = 0
selection = 100
valid_moves = []
# loading in chess piece images (king, queen, rook, bishop, knight, pawn ) for white and black

black_queen = pygame.image.load('assets/black_queen.png')
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

black_king = pygame.image.load('assets/black_king.png')
black_king_small = pygame.transform.scale(black_king, (45, 45))

black_rook = pygame.image.load('assets/black_rook.png')
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

black_bishop = pygame.image.load('assets/black_bishop.png')
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_knight = pygame.image.load('assets/black_knight.png')
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_pawn = pygame.image.load('assets/black_pawn.png')
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

white_queen = pygame.image.load('assets/white_queen.png')
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_king = pygame.image.load('assets/white_king.png')
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_rook = pygame.image.load('assets/white_rook.png')
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_bishop = pygame.image.load('assets/white_bishop.png')
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_knight = pygame.image.load('assets/white_knight.png')
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_pawn = pygame.image.load('assets/white_pawn.png')
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

black_images = [black_king, black_queen, black_knight, black_rook, black_bishop, black_pawn]
black_images_small = [black_king_small, black_queen_small, black_knight_small,
                      black_rook_small, black_bishop_small, black_pawn_small]

white_images = [white_king, white_queen, white_knight, white_rook, white_bishop, white_pawn]
white_images_small = [white_king_small, white_queen_small, white_knight_small,
                      white_rook_small, white_bishop_small, white_pawn_small]

piece_list = ['king', 'queen', 'knight', 'rook', 'bishop', 'pawn']
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# Chess Game Board
def chess_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        # drawing rectangle of 75*75px
        if row % 2 == 0:
            pygame.draw.rect(screen, 'white', [(column * 150), row * 75, 75, 75])  #[column, row, column_width, row_width]
        else:
            pygame.draw.rect(screen, 'white', [(column * 150) + 75, row * 75, 75, 75])

        # Adding margins
        for j in range(0,600,75):
            pygame.draw.rect(screen, 'black', [0,j, 600, 75], 1)
            pygame.draw.rect(screen, 'black', [j,0, 75, 600], 1)
        # for i in range(9):
        #     pygame.draw.line(screen, 'black', (0, 75* i), (600, 75 * i), 2)
        #     pygame.draw.line(screen, 'black', (700 * i, 0), (75 * i, 600), 2)

        pygame.draw.rect(screen, 'black', [600, 0, 200, display_height], 3)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']

        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))

        screen.blit(medium_font.render('FORFEIT', True, 'black'), (0, 600))

# Bringing chess pieces on board
def chess_piece():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index], (white_locations[i][0] * 75 + 7, white_locations[i][1] * 75 + 7))
        # if turn_step < 2:
        #     if selection == i:
        #         pygame.draw.rect(screen, 'red', [white_locations[i][0] * 75 + 1, white_locations[i][1] * 75 + 1,
        #                                          75, 75], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index], (black_locations[i][0] * 75 + 7, black_locations[i][1] * 75 + 7))
        # if turn_step >= 2:
        #     if selection == i:
        #         pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
        #                                           100, 100], 2)

#checking all valid moves and adding to a list
def valid_moves(pieces, location, turn):
    moves_list = []
    all_moves_list = []  #list of all valid option the current player has
    for i in range (len(pieces)):
        location = locations[i]
        piece = pieces[i]

        if piece == "pawn":
            moves_list = check_pawn(location, turn)
        elif piece == "rook":
            moves_list = check_rook(location, turn)
        elif piece == "bishop":
            moves_list = check_bishop(location, turn)
        elif piece == "knight":
            moves_list = check_knight(location, turn)
        elif piece == "queen":
            moves_list = check_queen(location, turn)
        elif piece == "king":
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

#checking pawn available moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


# main game loop

run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    chess_board()
    chess_piece()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
