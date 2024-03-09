import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello, PyGame!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a font object
font = pygame.font.Font(None, 36)

def gameLoop():
   """
       This is the main game loop. The function never really returns
   :return:
   """
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

       # Clear the screen
       window.fill(WHITE)

       mouse_pos = pygame.mouse.get_pos()

       # Render the text
       text = font.render(f"Hello, World! {mouse_pos}", True, BLACK)
       text_rect = text.get_rect(center=(mouse_pos[0], mouse_pos[1]))
       window.blit(text, text_rect)

       # Update the display
       pygame.display.flip()
   # end while
# end of function main

gameLoop() # Call the gameLoop