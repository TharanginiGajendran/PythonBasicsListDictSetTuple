
# syntax => {key expression: value expression for item in iterable if condition == True}

square = {i: i*i for i in range(5)}
print(square)

# find even numbers
even = {i: i for i in range(0,10) if i % 2 == 0}
print(even)