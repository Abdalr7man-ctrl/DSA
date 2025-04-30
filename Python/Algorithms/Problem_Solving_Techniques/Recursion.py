"""
https://youtu.be/ngCos392W4w?si=s36PtojzQGNGJFHw # 5 Simple Steps for Solving Any Recursive Problem
https://youtu.be/9bsK03SlmNM?si=3onRF6GgFcD8s7GC # indian guy # Done
https://youtu.be/B0NtAFf4bvU?si=g9ub8uKblgKn6M1a  # Cs Dogo
https://youtu.be/Gqn6hmm9HEw?si=b5s3zACY9_fFbGF5 Mahmoud Sami # Done

https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php # Exercises
"""

def recursion(n):
    if n >= 0: # Base Case
        return n + recursion(n-1) # Recursive case
    else :
        return n

print(recursion(3))
