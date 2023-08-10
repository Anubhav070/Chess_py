# CHESS GAME

import pygame

# pygame setup
pygame.init()  # initializing package
pygame.display.set_caption('Chess')
display_width = 600
display_height = 600
screen = pygame.display.set_mode([display_width, display_height])
font = pygame.font.Font('freesansbold.ttf', 20)
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
valid_moves = []  # A list of all possible lists of moves for the current player
# loading in chess piece images (king, queen, rook, bishop, knight, pawn ) for white and black

black_queen = pygame.image.load('assets/black_queen.png')

black_king = pygame.image.load('assets/black_king.png')

black_rook = pygame.image.load('assets/black_rook.png')

black_bishop = pygame.image.load('assets/black_bishop.png')

black_knight = pygame.image.load('assets/black_knight.png')

black_pawn = pygame.image.load('assets/black_pawn.png')

white_queen = pygame.image.load('assets/white_queen.png')

white_king = pygame.image.load('assets/white_king.png')

white_rook = pygame.image.load('assets/white_rook.png')

white_bishop = pygame.image.load('assets/white_bishop.png')

white_knight = pygame.image.load('assets/white_knight.png')

white_pawn = pygame.image.load('assets/white_pawn.png')

black_images = [black_king, black_queen, black_knight, black_rook, black_bishop, black_pawn]

white_images = [white_king, white_queen, white_knight, white_rook, white_bishop, white_pawn]

piece_list = ['king', 'queen', 'knight', 'rook', 'bishop', 'pawn']
# check variables/ flashing counter
# counter = 0
winner = ''
game_over = False


# Chess Game Board
def chess_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        # drawing rectangle of 75*75px
        if row % 2 == 0:
            pygame.draw.rect(screen, 'white',
                             [(column * 150), row * 75, 75, 75])  # [column, row, column_width, row_width]
        else:
            pygame.draw.rect(screen, 'white', [(column * 150) + 75, row * 75, 75, 75])

        # Adding margins
        for j in range(0, 600, 75):
            pygame.draw.rect(screen, 'black', [0, j, 600, 75], 1)
            pygame.draw.rect(screen, 'black', [j, 0, 75, 600], 1)
        # for i in range(9):
        #     pygame.draw.line(screen, 'black', (0, 75* i), (600, 75 * i), 2)
        #     pygame.draw.line(screen, 'black', (700 * i, 0), (75 * i, 600), 2)


# Bringing chess pieces on board
def chess_piece():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index], (white_locations[i][0] * 75 + 7, white_locations[i][1] * 75 + 7))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [white_locations[i][0] * 75 + 1, white_locations[i][1] * 75 + 1,
                                                  75, 75], 2)
                # drawing blue box in the coordinate of white piece selection

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index], (black_locations[i][0] * 75 + 7, black_locations[i][1] * 75 + 7))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [black_locations[i][0] * 75 + 1, black_locations[i][1] * 75 + 1,
                                                 75, 75], 2)
                # drawing red box in the coordinate of white piece selection


#checking pawn available moves
def check_pawn(location, color):
    moves_list = []
    if color == 'white':
        if (location[0], location[1] + 1) not in white_locations and \
                (location[0], location[1] + 1) not in black_locations and location[1] < 7:
            # checking if pawn has another same color or opposite color pawn infront of it and if it is not crossing border
            moves_list.append((location[0], location[1] + 1))
        if (location[0], location[1] + 2) not in white_locations and \
                (location[0], location[1] + 2) not in black_locations and location[1] == 1:
            # checking if pawn has another same color or opposite color pawn in 2steps of it
            moves_list.append((location[0], location[1] + 2))
        if (location[0] + 1, location[1] + 1) in black_locations:
            # checking for en passant
            moves_list.append((location[0] + 1, location[1] + 1))
        if (location[0] - 1, location[1] + 1) in black_locations:
            # checking for en passant
            moves_list.append((location[0] - 1, location[1] + 1))
    else:
        if (location[0], location[1] - 1) not in white_locations and \
                (location[0], location[1] - 1) not in black_locations and location[1] > 0:
            # checking if pawn has another same color or opposite color pawn infront of it and if it is not crossing border
            moves_list.append((location[0], location[1] - 1))
        if (location[0], location[1] - 2) not in white_locations and \
                (location[0], location[1] - 2) not in black_locations and location[1] == 6:
            # checking if pawn has another same color or opposite color pawn in 2steps of it
            moves_list.append((location[0], location[1] - 2))
        if (location[0] + 1, location[1] - 1) in white_locations:
            # checking for en passant
            moves_list.append((location[0] + 1, location[1] - 1))
        if (location[0] - 1, location[1] - 1) in white_locations:
            # checking for en passant
            moves_list.append((location[0] - 1, location[1] - 1))
    return moves_list

def check_rook(location,color):
    pass
def check_bishop(location,color):
    pass
def check_queen(location,color):
    pass
def check_knight(location,color):
    pass
def check_king(location,color):
    pass

#checking all valid moves and adding to a list
def valid_move_check(pieces, locations, turn):
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

# # check for valid moves for selected piece
# def piece_valid_moves():
#     if turn_step < 2:
#         options_list = white_options
#     else:
#         options_list = black_options
#     valid_options = options_list[selection]
#     return valid_options
#
#
# # draw valid moves on screen
# def piece_valid_draw(valid_moves):
#     if turn_step < 2:
#         color = 'red'
#     else:
#         color = 'blue'
#     for i in range(len(valid_moves)):
#         pygame.draw.circle(screen, color, (valid_moves[i][0] * 75 + 37, valid_moves[i][1] * 75 + 37), 5)

# main game loop
black_options = valid_move_check(black_pieces, black_locations, 'black')
white_options = valid_move_check(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    screen.fill('brown')
    chess_board()
    chess_piece()

    # Moving piece on board through valid moves
    # if selection != 100:
    #     valid_moves = piece_valid_moves()
    #     piece_valid_draw(valid_moves)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 75
            y_coord = event.pos[1] // 75
            selected_piece = (x_coord, y_coord)
            if turn_step < 2:
                if selected_piece in white_locations:
                    selection = white_locations.index(selected_piece)
                    if turn_step == 0:
                        turn_step = 1
                if selected_piece in valid_moves and selection != 100:
                    white_locations[selection] = selected_piece
                    if selected_piece in black_locations:
                        black_piece = black_locations.index(selected_piece)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = valid_move_check(black_pieces, black_locations, 'black')
                    white_options = valid_move_check(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step >= 2:
                if selected_piece in black_locations:
                    selection = black_locations.index(selected_piece)
                    if turn_step == 2:
                        turn_step = 3
                if selected_piece in valid_moves and selection != 100:
                    black_locations[selection] = valid_move_check
                    if selected_piece in white_locations:
                        white_piece = white_locations.index(selected_piece)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = valid_move_check(black_pieces, black_locations, 'black')
                    white_options = valid_move_check(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

    pygame.display.flip()
pygame.quit()