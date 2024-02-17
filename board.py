from settings import *
import random

class Board():
    def __init__(self):
        self.board = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]

        self.openSpace = 16
        self.addTile(2,[2])

        self.surface2 = pygame.Surface((TILESIZE,TILESIZE))
        self.surface2Rect = self.surface2.get_rect()
        self.surface2.fill("#f7d794")
        self.surface4 = pygame.Surface((TILESIZE,TILESIZE))
        self.surface4.fill("#f5cd79")
        self.surface8 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface8.fill("#f3a683")
        self.surface16 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface16.fill("#f19066")
        self.surface32 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface32.fill("#e77f67")
        self.surface64 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface64.fill("#e15f41")
        self.surface128 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface128.fill("#63cdda")
        self.surface256 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface256.fill("#3dc1d3")
        self.surface512 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface512.fill("#778beb")
        self.surface1024 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface1024.fill("#786fa6")
        self.surface2048 = pygame.Surface((TILESIZE, TILESIZE))
        self.surface2048.fill("#574b90")
        self.tileDict = {2:self.surface2,4:self.surface4,8:self.surface8,16:self.surface16,32:self.surface32,64:self.surface64,128:self.surface128,256:self.surface256,512:self.surface512,1024:self.surface1024,2048:self.surface2048}

        self.pressed = ""
        self.score = 0

        self.restartText = fontSmall.render("Press R to restart",True,"#f5f6fa")
        self.restartRect = self.restartText.get_rect(center = (WIDTH // 2,HEIGHT - MARGINSIZE // 2))
        self.scoreText = fontSmall.render(str(self.score),True,"#f5f6fa")
        self.scoreRect = self.scoreText.get_rect(center = (WIDTH // 2,MARGINSIZE // 2))

        # self.highScore = 0
        # self.scoreText = fontSmall.render(str(self.score), True, "#f5f6fa")
        # self.scoreRect = self.scoreText.get_rect(center=(WIDTH // 2, MARGINSIZE // 2))

        self.getScore()
        self.getOpenSpace()

    def addTile(self,amount,tileList):
        if self.openSpace > 0:
            pointx = random.randint(0,3)
            pointy = random.randint(0,3)
            for _ in range(amount):
                while self.board[pointy][pointx] != 0:
                    pointx = random.randint(0,3)
                    pointy = random.randint(0,3)
                self.board[pointy][pointx] = random.choice(tileList)

    def getOpenSpace(self):
        openSpaceCount = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    openSpaceCount += 1
        self.openSpace = openSpaceCount


    def getScore(self):
        score = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                score += self.board[r][c]

        self.score = score * 10 - 40
        self.scoreText = fontSmall.render(str(self.score), True, "#f5f6fa")
        self.scoreRect = self.scoreText.get_rect(center=(WIDTH // 2, MARGINSIZE // 2))
    def displayBoard(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                pygame.draw.rect(screen,"#bdc3c7",pygame.Rect(MARGINSIZE + c * TILESIZE,MARGINSIZE + r * TILESIZE,TILESIZE,TILESIZE))

    def borderLine(self):
        for i in range(5):
            if i % 4 == 0:
                pygame.draw.line(screen,"#2d3436",(MARGINSIZE + TILESIZE * i,MARGINSIZE),(MARGINSIZE + TILESIZE * i,WIDTH - MARGINSIZE),5)
                pygame.draw.line(screen, "#2d3436", (MARGINSIZE, MARGINSIZE + TILESIZE * i),(WIDTH - MARGINSIZE, MARGINSIZE + TILESIZE * i), 5)
            else:
                pygame.draw.line(screen, "#2d3436", (MARGINSIZE + TILESIZE * i, MARGINSIZE),(MARGINSIZE + TILESIZE * i, HEIGHT - MARGINSIZE), 2)
                pygame.draw.line(screen, "#2d3436", (MARGINSIZE, MARGINSIZE + TILESIZE * i),(WIDTH - MARGINSIZE, MARGINSIZE + TILESIZE * i), 2)

    def displayTile(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != 0:
                    screen.blit(self.tileDict.get(self.board[r][c]),(MARGINSIZE + TILESIZE * c,MARGINSIZE + TILESIZE * r))
                    if len(str(self.board[r][c])) == 1:
                        text = font1.render(str(self.board[r][c]), True, "#f5f6fa")
                    elif len(str(self.board[r][c])) == 2:
                        text = font2.render(str(self.board[r][c]), True, "#f5f6fa")
                    elif len(str(self.board[r][c])) == 3:
                        text = font3.render(str(self.board[r][c]), True, "#f5f6fa")
                    else:
                        text = font4.render(str(self.board[r][c]), True, "#f5f6fa")

                    textRect = text.get_rect(center=(MARGINSIZE + TILESIZE * c + TILESIZE // 2,MARGINSIZE + TILESIZE * r + TILESIZE//2))
                    screen.blit(text,textRect)

    def moveInput(self):
        key = pygame.key.get_pressed()
        if self.openSpace > 0:
            if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.pressed != "left":
                self.pressed = "left"
                self.moveLeft()
                self.addTile(1,[2,4])
                self.getOpenSpace()
                self.getScore()
            if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.pressed != "right":
                self.pressed = "right"
                self.moveRight()
                self.addTile(1,[2,4])
                self.getOpenSpace()
                self.getScore()
            if (key[pygame.K_UP] or key[pygame.K_w]) and self.pressed != "up":
                self.pressed = "up"
                self.moveUp()
                self.addTile(1,[2,4])
                self.getOpenSpace()
                self.getScore()
            if (key[pygame.K_DOWN] or key[pygame.K_s]) and self.pressed != "down":
                self.pressed = "down"
                self.moveDown()
                self.addTile(1,[2,4])
                self.getOpenSpace()
                self.getScore()



        if (key[pygame.K_r]) and self.pressed != "r":
            self.reset()
            self.pressed = "r"
        if (key[pygame.K_LEFT] == False and key[pygame.K_a] == False) and (
                key[pygame.K_RIGHT] == False and key[pygame.K_d] == False) and (
                key[pygame.K_UP] == False and key[pygame.K_w] == False) and (
                key[pygame.K_DOWN] == False and key[pygame.K_s] == False) and key[pygame.K_r] == False:

            self.pressed = ""
    def moveDown(self):
        for r in range(len(self.board)-1,-1,-1):
            for c in range(len(self.board[r])):
                if self.board[r][c] != 0:
                    piece = self.board[r][c]
                    for i in range(1,len(self.board) - r):
                        if self.board[r+i][c] == 0:
                            self.board[r+i][c] = piece
                            self.board[r+i-1][c] = 0
                        elif self.board[r+i][c] == piece:
                            self.board[r+i][c] = piece * 2
                            self.board[r + i - 1][c] = 0
                            self.board[r][c] =0
                            break
                        elif self.board[r+i][c] != 0 and self.board[r+i][c] != self.board[r][c]:
                            break

    def moveUp(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != 0:
                    piece = self.board[r][c]
                    for i in range(1,r + 1):
                        if self.board[r-i][c] == 0:
                            self.board[r-i][c] = piece
                            self.board[r-i+1][c] = 0
                        elif self.board[r-i][c] == piece:
                            self.board[r-i][c] = piece * 2
                            self.board[r - i + 1][c] = 0
                            self.board[r][c] =0
                            break
                        elif self.board[r-i][c] != 0 and self.board[r-i][c] != self.board[r][c]:
                            break

    def moveLeft(self):
        for c in range(len(self.board)):
            for r in range(len(self.board[c])):
                if self.board[r][c] != 0:
                    piece = self.board[r][c]
                    for i in range(1,c + 1):
                        if self.board[r][c-i] == 0:
                            self.board[r][c-i] = piece
                            self.board[r][c-i+1] = 0
                        elif self.board[r][c-i] == piece:
                            self.board[r][c-i] = piece * 2
                            self.board[r][c - i + 1] = 0
                            self.board[r][c] =0
                            break
                        elif self.board[r][c-i] != 0 and self.board[r][c-i] != self.board[r][c]:
                            break

    def moveRight(self):
        for c in range(len(self.board)-1,-1,-1):
            for r in range(len(self.board[c])):
                if self.board[r][c] != 0:
                    piece = self.board[r][c]
                    for i in range(1,len(self.board) - c):
                        if self.board[r][c+i] == 0:
                            self.board[r][c+i] = piece
                            self.board[r][c+i-1] = 0
                        elif self.board[r][c+i] == piece:
                            self.board[r][c+i] = piece * 2
                            self.board[r][c + i - 1] = 0
                            self.board[r][c] =0
                            break
                        elif self.board[r][c+i] != 0 and self.board[r][c+i] != self.board[r][c]:
                            break

    def reset(self):
        self.board = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        self.openSpace = 16
        self.addTile(2,[2])
        self.getScore()

    def displayText(self):

        screen.blit(self.scoreText,self.scoreRect)
        screen.blit(self.restartText,self.restartRect)

    def display(self):
        self.displayBoard()
        self.displayTile()
        self.borderLine()
        self.moveInput()
        self.displayText()

board = Board()