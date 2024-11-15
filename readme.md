## Spirograph Drawer
This Python script uses the turtle module to create a colorful spirograph pattern. The script generates a visually appealing design by drawing overlapping circles in random colors.

### Features
- Generates a spirograph pattern with vibrant, random colors.
- Adjustable spirograph size for customization.
- Interactive turtle graphics window that closes when clicked.

### How It Works
The program:

-- Sets up a turtle object (tom) to draw on the screen.

-- Uses the colors function to generate random RGB colors.

-- Implements the draw_spirograph function to draw a spirograph by:
- Changing the turtle's heading incrementally.
- Drawing a circle at each step with a random color.

### Prerequisites
- Python 3.x
- The turtle module (comes pre-installed with Python)

### Customization
You can customize the spirograph by modifying the draw_spirograph function's size parameter:

- Smaller values (e.g., 1): Produces a denser, more intricate spirograph.
- Larger values (e.g., 5): Produces a sparser, simpler spirograph.

### How to Run
- Save the script to a file, e.g., spirograph.py.
- Run the script
- A turtle graphics window will open and display the spirograph pattern.
- Click on the window to close it.