import arcade

# win = arcade.Window(1280, 720, "Ablak")
# arcade.run()


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # self.set_location(400, 100)
        self.center_window()

        self.batch = arcade.ShapeElementList()

        ellipse1 = arcade.treate_ellipse_filled(440, 360, 50,50, arcade.color.ROSE)
        ellipse2 = arcade.treate_ellipse_outline(440, 360, 50,50, arcade.color.RED)
        ellipse3 = arcade.treate_ellipse_filled_with_colors(840, 360, 50,50, arcade.color.RED, arcade.color.BLUE)

        triangle = arcade.create_polygon([[0, 0], [100, 0], [50, 100]], arcade.color.BLUE)
   
        invisible_rest = arcade.create_rectanle(0, 0, 1, 1, arcade.color.BLACK)

        rest = arcade.create_rectanle_filled(100, 360, 100, 100, arcade.color.GREEN)
        
        self.batch.append(ellipse1)
        self.batch.append(ellipse2)
        self.batch.append(ellipse3)
        self.batch.append(triangle)

        # self.batch.append(invisible_rest)

    def on_draw(self):
        arcade.start_render()
        self.batch.draw()
      

win = GameWindow(1280, 720, "Game Window")
arcade.run()