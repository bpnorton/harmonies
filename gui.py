"""
Here lives the GUI!

oh boy here we go...
"""

import arcade
from arcade import draw_circle_filled

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Harmonies"
SCALE = 1.0
ANIMAL_SCALE = SCALE * 0.3



class GameWindow(arcade.Window):
    """
    Main window containing game board and cards
    """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        # Set window background color
        arcade.set_background_color((236,226,197,100))

        self.setup()

    def setup(self):

        # Initialize static elements
        self.card_shadows = self.card_shadows()
        self.token_spots = self.token_spots()


        # Initialize sprites
        self.all_sprites = arcade.SpriteList()

        self.bear = arcade.Sprite("Animal Sprites/GrizzlyBear.png", ANIMAL_SCALE)
        self.bear.bottom = 10
        self.bear.right = self.width - 10
        self.all_sprites.append(self.bear)

        self.flamingo = arcade.Sprite("Animal Sprites/Flamingo.png", ANIMAL_SCALE)
        self.flamingo.top = self.height - 10
        self.flamingo.right = self.width - 10
        self.all_sprites.append(self.flamingo)

        self.alligator = arcade.Sprite("Animal Sprites/Alligator.png", ANIMAL_SCALE)
        self.alligator.bottom = 10
        self.alligator.left = 10
        self.all_sprites.append(self.alligator)



    def on_draw(self):
        self.clear()
        self.card_shadows.draw()
        self.all_sprites.draw()
        self.token_spots.draw()

    def card_shadows(self):
        card_shadows = arcade.shape_list.ShapeElementList()
        # To change card shadow dimensions, spacing, color, change these values
        color = (185, 170, 155, 255)
        card_width = 160
        card_height = 240
        radius = 15
        spacing = 30
        # Create the shapes
        y = self.height - (card_height//2 + spacing)
        for x in range(card_width//2 + spacing, 4*(card_width + spacing) + card_width//2, card_width + spacing):
            # Rectangles
            wide_rect = arcade.shape_list.create_rectangle_filled(
                x, y, card_width, card_height - 2*radius, color)
            card_shadows.append(wide_rect)
            tall_rect = arcade.shape_list.create_rectangle_filled(
                x, y, card_width - 2*radius, card_height, color)
            card_shadows.append(tall_rect)
            # Corners
            upper_left = arcade.shape_list.create_ellipse_filled(
                x - card_width//2 + radius, y + card_height//2 - radius, 2*radius, 2*radius, color)
            card_shadows.append(upper_left)
            upper_right = arcade.shape_list.create_ellipse_filled(
                x + card_width//2 - radius, y + card_height//2 - radius, 2*radius, 2*radius, color)
            card_shadows.append(upper_right)
            lower_left = arcade.shape_list.create_ellipse_filled(
                x - card_width//2 + radius, y - card_height//2 + radius, 2*radius, 2*radius, color)
            card_shadows.append(lower_left)
            lower_right = arcade.shape_list.create_ellipse_filled(
                x + card_width//2 - radius, y - card_height//2 + radius, 2*radius, 2*radius, color)
            card_shadows.append(lower_right)

        return card_shadows

    def token_spots(self):
        token_spots = arcade.shape_list.ShapeElementList()
        # To change token dimensions, spacing, color, change these values
        color = (185, 170, 155, 255)
        big_radius = 200
        radius = 15
        # Create the shapes
        x = 950
        y = 500
        big_circle = arcade.shape_list.create_ellipse(x, y, big_radius, big_radius, color)
        token_spots.append(big_circle)


        return token_spots



# Main
if __name__ == "__main__":
    game = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()