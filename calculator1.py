import calculations
print(calculations.add(5, 3))   
print(calculations.subtract(10, 4))
print(calculations.multiply(6, 7))
try:        
    print(calculations.divide(8, 0))
except ValueError as e: 
    print(e)