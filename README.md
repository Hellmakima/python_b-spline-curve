# Bezier Curve Drawing with Pygame

This project demonstrates drawing Bezier curves using Pygame, a popular library for game development in Python.

## Description

The project allows you to draw points on a Pygame window by clicking with the mouse. It then constructs and displays Bezier curves based on these points using various techniques:

- **Bezier Curve Calculation**: The project implements a function to calculate points on a Bezier curve given control points.
- **Curve Smoothing**: It smooths out the curve by adding additional control points between the original points.
- **Visualization**: Each point and segment of the curve is rendered using Pygame's drawing functions.

## Requirements

To run this project, you need:

- Python 3.x
- Pygame library (`pip install pygame`)

## How to Use

1. **Run the Program**: Execute the Python script (`python bezier_curves.py`).
2. **Add Control Points**: Click on the Pygame window to add control points. These points will define the Bezier curve.
3. **Quit**: Press any key or close the window to quit the program.

## Files

- **bezier_curves.py**: The main Python script containing the code to draw Bezier curves.
- **readme.md**: This file, providing information about the project.

## Credits

- **Author**: Sufiayn
- **License**: This project is licensed under nothing.

## Notes

- Modify the `fps` variable to adjust the frame rate.
- Adjust the `offset` parameter in `draw_bezier` function for smoother or coarser curves.
- Feel free to experiment with different points and curves to understand how Bezier curves work.

## Example

Here’s a screenshot of the program in action:

![Bezier Curves Example](https://github.com/Hellmakima/python_b-spline-curve/blob/main/b-spline_curve.PNG)

---

Feel free to expand this README with more details or explanations specific to your implementation or intended use of Bezier curves with Pygame.
