import time
def time_this(num_runs=10):
        def decorator(func):
            def timer():
                avg_time = 0
                for i in range(num_runs):
                    t0 = time.time()
                    func()
                    t1 = time.time()
                    avg_time += (t1 - t0)
                avg_time /= num_runs
                print("Выполнение заняло %.5f секунд" % avg_time)
            return timer
        return decorator
@time_this(num_runs = 10)
def func_():
    for j in range(1000000):
        pass
func_()