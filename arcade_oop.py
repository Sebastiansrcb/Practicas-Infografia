import arcade
from hello_arcade import draw_flower

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class TVScreen(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "TV sin señal")
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        # Static de la pantalla
        for x in range(0, SCREEN_WIDTH, 5):
            for y in range(0, SCREEN_HEIGHT, 5):
                if (x + y) % 20 == 0:
                    arcade.draw_point(x, y, arcade.color.WHITE, 1)

        # Bordes de la pantalla
        arcade.draw_rectangle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40, arcade.color.WHITE, 4)
        arcade.draw_rectangle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20, arcade.color.WHITE, 4)
        arcade.draw_rectangle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.WHITE, 4)

        # Dibujar cuatro flores en las esquinas
        draw_flower(50, 50)
        draw_flower(SCREEN_WIDTH - 50, 50)
        draw_flower(SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50)
        draw_flower(50, SCREEN_HEIGHT - 50)


    def update(self, delta_time):
        pass

def main():
    game = TVScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
