    class Fraction:
        def __init__(self):
            # Ask user what they want to do
            choice = int(input("What do you want to perform with fraction?\n"
                            "1: Addition\n"
                            "2: Subtraction\n"
                            "3: Multiplication\n"
                            "4: Division\n"))

            # Take two fractions as input
            print("\nEnter first fraction:")
            n1, d1 = self.get_fraction()

            print("\nEnter second fraction:")
            n2, d2 = self.get_fraction()

            # Perform operation based on choice
            if choice == 1:
                num = n1*d2 + n2*d1
                den = d1*d2
                print("Result (Addition):", f"{num}/{den}")

            elif choice == 2:
                num = n1*d2 - n2*d1
                den = d1*d2
                print("Result (Subtraction):", f"{num}/{den}")

            elif choice == 3:
                num = n1*n2
                den = d1*d2
                print("Result (Multiplication):", f"{num}/{den}")

            elif choice == 4:
                if n2 == 0:
                    print("Error: Cannot divide by zero fraction!")
                else:
                    num = n1*d2
                    den = d1*n2
                    print("Result (Division):", f"{num}/{den}")

            else:
                print("Invalid input!")

        def get_fraction(self):
            """Takes fraction input from user and returns numerator & denominator"""
            numerator = int(input("Enter numerator: "))
            denominator = int(input("Enter denominator: "))
            if denominator == 0:
                raise ValueError("Denominator cannot be zero!")
            return numerator, denominator



    Fraction()
