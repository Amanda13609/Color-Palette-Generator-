import pygame
import random
import sys

def generate_color_palette(num_colors):
    palette = []
    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        palette.append(pygame.Color(red, green, blue))
    return palette

def display_color_palette(palette):
    pygame.init()
    screen_width = 200 * len(palette)
    screen = pygame.display.set_mode((screen_width, 200))
    pygame.display.set_caption("Generated Color Palette")
    
    x_offset = 0
    for color in palette:
        pygame.draw.rect(screen, color, (x_offset, 0, 200, 200))
        x_offset += 200
    
    pygame.display.flip()

    # Print RGB values of each color
    for i, color in enumerate(palette):
        print(f"Color {i+1}: RGB({color.r}, {color.g}, {color.b})")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

def main():
    while True:
        user_input = input("How many colors would you like in the palette? Enter a number: ")
        try:
            num_colors = int(user_input)
            if num_colors <= 0:
                print("Please enter a positive number.")
                continue
            palette = generate_color_palette(num_colors)
            display_color_palette(palette)
        except ValueError:
            print("Please enter a valid number.")
            continue

        response = input("Would you like to generate another palette? (yes/no): ").lower()
        if response != "yes":
            print("Thank you for using Color Palette Generator!")
            break

if __name__ == "__main__":
    main()
