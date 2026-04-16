
import math

ab = int(input())
bc = int(input())
angle_radians = math.atan2(ab, bc)

angle_degrees = math.degrees(angle_radians)
print(f"{round(angle_degrees)}{chr(176)}")
