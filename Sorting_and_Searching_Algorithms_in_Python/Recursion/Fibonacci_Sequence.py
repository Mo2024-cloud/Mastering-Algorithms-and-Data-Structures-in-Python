"""
So, what is the Fibonacci sequence? 
The Fibonacci sequence is an infinite sequence of numbers, starting with 0 and 1, with every 
subsequent number being the sum of the previous two numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
"""

"""
 Using we integrate an optimization technique known as memoization to further enhance the function.
 With memoization, we store the results of previous Fibonacci number calculations.
"""

def fib(n, computed={0:0,1:1,2:1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

print(fib(6))