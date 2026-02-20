import random
import pygame
def loadDict(fileName):
    file = open(fileName)
    words = file.readlines()
    file.close()
    return [word[:5].upper() for word in words]
dict_Guessing= loadDict("assests/dictionary_5_letter.txt")
dict_Answers = loadDict("assests/targets_5_letter.txt")
ANSWER = random.choice(dict_Answers)
WIDTH = 600
HEIGHT =700
MARGIN = 10
T_MARGIN =100
B_MARGIN =100
LR_MARGIN =100
GREY = (70,70,80)
GREEN =(6,214,160)
YELLOW =(255,209,102)
RED =(255,0,0)
BLACK = (0,0,0)
INPUT = ""
GUESSES = []
ALPHABET = "ABCDEFGHIJKLMNOPQSTUVWXYZ"
UNGUESSED = ALPHABET
GAME_OVER =False
pygame.init()
pygame.font.init()
pygame.display.set_caption("Mohamed's Wordle Game")
SQ_SIZE =(WIDTH-4*MARGIN-2*LR_MARGIN) // 5
FONT =pygame.font.SysFont("free sans bold",SQ_SIZE)
FONT_SMALL =pygame.font.SysFont("free sans bold",SQ_SIZE//2)


def determine_unguessed_letters(guesses):
    guessed_letters = "".join(guesses)
    unguessed_letters = ""
    for letter in ALPHABET:
        if letter not in guessed_letters:
             unguessed_letters = unguessed_letters +letter
    return unguessed_letters

def determine_color(guess,j):
    letter = guess[j]
    if letter ==ANSWER[j]:
        return GREEN
    elif letter in ANSWER:
        n_target = ANSWER.count(letter)
        n_correct =0
        n_occurence = 0
        for i in range(5):
            if guess[i] == letter:
                if i<=j:
                    n_occurence+=1
                if letter ==ANSWER[i]:
                    n_correct+=1
        if n_target-n_correct -n_occurence >=0 :
            return YELLOW

        
    return GREY
# Create Screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# Animation loop :)
animating = True
while animating:
    #background color=(100,100,100)
    screen.fill("white")
    determine_unguessed_letters(GUESSES)
    #DRAW UNGESSED LETTERS
    letters = FONT_SMALL.render("Wordle Guess :)",False,GREEN)
    surface = letters.get_rect(center = (WIDTH//2+2,T_MARGIN//2))
    screen.blit(letters,surface)
    #setting Margins(T,B,LR) & Draw Guess
    y = T_MARGIN
    for i in range(6):
        x=LR_MARGIN
        for j in range(5):
            square = pygame.Rect(x,y,SQ_SIZE,SQ_SIZE)
            pygame.draw.rect(screen,GREY,square,width=2,border_radius=5)
            # words been guessed
            if i < len(GUESSES):
                color = determine_color(GUESSES[i],j)
                pygame.draw.rect(screen,color,square,border_radius=5)
                letter = FONT.render(GUESSES[i][j], False, (255,255,255))
                surface = letter.get_rect(center = (x+SQ_SIZE//2,y+SQ_SIZE//2))
                screen.blit(letter,surface)
            #user on go input
            if i == len(GUESSES) and j< len(INPUT) :
                letter = FONT.render(INPUT[j], False, BLACK )
                surface = letter.get_rect(center = (x+SQ_SIZE//2,y+SQ_SIZE//2))
                screen.blit(letter,surface)

            x+=SQ_SIZE+MARGIN
        y+=SQ_SIZE+MARGIN

    # showig the correct answer after a gameOVer: 
    if len(GUESSES) ==6 and GUESSES[5]!= ANSWER:
        GAME_OVER =True
        letters =FONT.render("The Word was: "+ANSWER,False,RED)
        surface = letters.get_rect(center=(WIDTH//2, HEIGHT-B_MARGIN//2-MARGIN) )
        screen.blit(letters,surface)
    
    


    

    #update Screen
    pygame.display.flip()
    # track user interface
    for event in pygame.event.get():
        #close window
        if event.type ==pygame.QUIT:
            animating =False
        #user presses key
        elif event.type == pygame.KEYDOWN:
            #escape key to Quit
            if event.key ==pygame.K_ESCAPE:
                animating = False
            #backsapces for user input
            if event.key ==pygame.K_BACKSPACE:
                if len(INPUT) > 0:
                    INPUT = INPUT[:len(INPUT)-1]
            # Return key to submit a guess
            elif event.key == pygame.K_RETURN:
                if len(INPUT) == 5 and INPUT in dict_Guessing:
                    GUESSES.append(INPUT)
                    UNGUESSED = determine_unguessed_letters(GUESSES)
                    GAME_OVER = True if INPUT  == ANSWER else False
                    INPUT = ""
            elif event.key ==pygame.K_SPACE:
                GAME_OVER =False
                GUESSES = []
                UNGUESSED = ALPHABET
                INPUT =""
                    

            # if the user inputs the word
            elif len(INPUT) <5 and not GAME_OVER:
                INPUT = INPUT +event.unicode.upper()
            
                
