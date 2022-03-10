def func_counter(func):
    def wrapped(*args, **kwargs):
        wrapped.counter += 1
        return func(*args, **kwargs)
    wrapped.counter = 0
    return wrapped

@func_counter
def foo(y):
    return y+2**3-34

foo(2)
foo(4)
foo(6)
print(foo.counter)