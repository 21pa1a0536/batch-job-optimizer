import time
import concurrent.futures

def task(name, duration):
    print(f"Running {name}...")
    time.sleep(duration)
    print(f"{name} completed.")
    return f"{name} done"

def main():
    jobs = [("Job1", 2), ("Job2", 3), ("Job3", 1)]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(task, name, duration) for name, duration in jobs]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()
