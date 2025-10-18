"""
Formatting & Display
21. Create a banner with asterisks around text.
22. Display a multiplication table for a number.
23. Format output to two decimal places.
24. Align text left, right, and center.
25. Print network device details in a table format."""


# Banner with asterisk round text.
print('Hello Cyber Security'.center(30, "*"))

# Display multiplication table.
print("\nMultiplication table for 2")print('2 x 1 =', 2*1)
print('2 x 2 =', 2*2)
print('2 x 3 =', 2*3)
print('2 x 4 =', 2*4)
print('2 x 5 =', 2*5)
print('2 x 6 =', 2*6)
print('2 x 7 =', 2*7)
print('2 x 8 =', 2*8)
print('2 x 9 =', 2*9)
print('2 x 10 =', 2*10)
print('2 x 11 =', 2*11)
print('2 x 12 =', 2*12)



# format output to 2 decimal placed.
import math as m
radius = int(input('\nEnter the radius of  circle: '))
angle_in_theta = int(input("Enter angle in tetha: "))
length_of_arc = ((angle_in_theta / 360) * (2 * m.pi * radius))

print(f"Length of Arc: {length_of_arc:.2f}" )


# format text to left, right, center.
user_input = input("\nEnter a text: ").strip()
center_align = user_input.center(12)
left_just = user_input.ljust(12)
right_just = user_input.rjust(12)
print(center_align)
print(left_just)
print(right_just)


print("\nNetwork Device Details")
print(f"{'Device':<15}{'IP Address':<20}{'Status':<10}")
print("-" * 45)
print(f"{'Router':<15}{'192.168.1.1':<20}{'Active':<10}")
print(f"{'Switch':<15}{'192.168.1.2':<20}{'Active':<10}")
print(f"{'Firewall':<15}{'192.168.1.254':<20}{'Inactive':<10}")



    