import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"Time taken: {end - self.start:.6f} seconds")
        return False
    
with Timer():
    total = 0
    for i in range(10000):
        total += i
