
# Analagous to builtins.range(), but accepts float values
# stepped(5, 6, 0.2) -> [5, 5.2, 5.4, 5.6, 5.8]
def stepped(start, stop, step):
    values = []
    i = start
    while i < stop:
        values.append(i)
        i += step
    return values


# A linear space with a given number of samples
# linear(1, 2, 10) -> [1, 1.1, 1.2, 1.3, ..., 1.9]
def linear(start, stop, samples):
    pass


if __name__ == "__main__":
    print(stepped(2, 3, 0.05))
