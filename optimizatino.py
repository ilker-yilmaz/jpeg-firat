import cProfile

def sample_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

def main():
    for _ in range(1000):
        sample_function(1000)

if __name__ == "__main__":
    cProfile.run("main()")
