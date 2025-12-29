import math as m

def circle_square():
    """Calculate the square of a circle."""
    radius = int(input("Enter the radius: "))
    area = ((m.pi) * (radius ** 2 ))
    output = f"Area: {area:.2f} cm²."

    return output


print(circle_square())
