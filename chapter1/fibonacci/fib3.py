#without recursion it is simple and fast :)
#in recursive solution we worked backward, in iterative solution we worked forward.

def fib3(n: int) -> int:
    if n==0: return n
    last: int =0
    next: int =1
    for _ in range(1,n):
        last, next = next, last+next
    return next

if __name__ == "__main__":
    print(fib3(50))
    print(fib3(10))
        