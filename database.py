print("This is the database.py module.")
print("Python thinks this is called {}".format(__name__))

import blood_calculator

answer = blood_calculator.check_HDL(55)
print("The HDL of 55 is {}".format(answer))
