# Import the turtle package
import turtle

# Function to initialize the turtle screen and turtle object
def initialize_turtle():
    screen = turtle.Screen()
    screen.setup(600, 600)  # Set up the screen size to 600x600
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(100)  # Set the turtle speed to maximum
    return screen, turtle_obj

# Function to draw a square of a given size
def draw_square(turtle_obj, size):
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)

# Function to draw a checkerboard of 8x8 squares
def draw_checkerboard(turtle_obj, square_size):
    for row in range(8):
        # Move to the start of each row
        turtle_obj.up()
        turtle_obj.setpos(0, square_size * row)
        turtle_obj.down()

        for col in range(8):
            # Set color based on the position (alternating black and white)
            color = 'black' if (row + col) % 2 == 0 else 'white'
            turtle_obj.fillcolor(color)

            # Start filling the square with the selected color
            turtle_obj.begin_fill()

            # Draw the square
            draw_square(turtle_obj, square_size)

            # Complete the fill
            turtle_obj.end_fill()

            # Move the turtle forward to the next square position
            turtle_obj.forward(square_size)

# Main function to run the program
def main():
    # Initialize the turtle screen and turtle object
    screen, turtle_obj = initialize_turtle()

    # Set the square size for the checkerboard
    square_size = 30

    # Draw the checkerboard
    draw_checkerboard(turtle_obj, square_size)

    # Hide the turtle and keep the window open
    turtle_obj.hideturtle()
    screen.mainloop()

# Run the program
if __name__ == "__main__":
    main()

