import pygame as p 
import ChessEngine 

WIDTH = HEIGHT = 512
DIMENSION = 8 
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
whiteKnight = {}

def loadImage():
    whiteKnight["wN"] = p.transform.scale((p.image.load("images/wN.png")),(SQUARE_SIZE, SQUARE_SIZE))

def main():
    p.init()
    position = input("casa: ")
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    gs.choosePosition(position) # não pronta
    loadImage() # just once 
    running = True

    while running:

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color(165, 99, 66), p.Color(242,209 ,165)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2 )]
            p.draw.rect(screen, color, p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(whiteKnight[piece], p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()