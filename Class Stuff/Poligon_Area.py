import time
import sys
import threading
import math

def delete_printed_text(num_lines):
    for _ in range(num_lines):
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')  
    sys.stdout.flush()

class Shapes:
    def __init__(self):

        while True:
            shape = input("Enter the number of sides of the shape (3 to 6): ")
            if shape in {"3", "4", "5", "6"}:
                self.shape = shape
                break
            else:
                print("Invalid input. Please enter a number from 3 to 6.")

    
        if self.shape == "3":
            self.x = float(input("What is the base of the triangle?: "))
            self.y = float(input("What is the height of the triangle?: "))
        elif self.shape == "4":
            self.x = float(input("What is the base of the rectangle?: "))
            self.y = float(input("What is the height of the rectangle?: "))
        elif self.shape == "5":
            self.side = float(input("What is the side length of the pentagon?: "))
        else:  
            self.side = float(input("What is the side length of the hexagon?: "))

        def back_end():
            if self.shape == "3":
                self.area = 0.5 * self.x * self.y
            elif self.shape == "4":
                self.area = self.x * self.y
            elif self.shape == "5":
                self.area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side ** 2
            else: 
                self.area = (3 * math.sqrt(3) / 2) * self.side ** 2

        def front_end():
            for _ in range(3):
                print("Starting polygon calculator...")
                time.sleep(0.5)
                delete_printed_text(1)
                time.sleep(0.5)

        backend_thread = threading.Thread(target=back_end)
        frontend_thread = threading.Thread(target=front_end)

        frontend_thread.start()
        backend_thread.start()

        backend_thread.join()
        frontend_thread.join()

        print(f"The area is {self.area:.2f}")

obj = Shapes()