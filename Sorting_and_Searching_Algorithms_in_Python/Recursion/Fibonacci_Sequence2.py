"""
So, what is the Fibonacci sequence? 
The Fibonacci sequence is an infinite sequence of numbers, starting with 0 and 1, with every 
subsequent number being the sum of the previous two numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
"""

"""
 Using we integrate an optimization technique known as memoization to further enhance the function.
 With memoization, we store the results of previous Fibonacci number calculations.
"""
# Know We Start With 2 , 3 Not 0 , 1

def alt_fib(n, computed = {0:2,1:3}):
    if n not in computed:
        computed[n] = alt_fib(n - 1, computed) + alt_fib(n - 2, computed)
    return computed[n]

# Test the function with some values
print(alt_fib(0))  # Expected output: 2
print(alt_fib(1))  # Expected output: 3
print(alt_fib(2))  # Expected output: 5
print(alt_fib(3))  # Expected output: 8
print(alt_fib(4))  # Expected output: 13
print(alt_fib(5))  # Expected output: 21