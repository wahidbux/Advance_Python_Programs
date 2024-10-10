import threading
import time
import random
from queue import Queue

# Function for the producer, adding items to the queue
def producer(queue, event):
    while not event.is_set():
        item = random.randint(1, 100)
        print(f"Producer produced item: {item}")
        queue.put(item)  # Add item to the queue
        time.sleep(random.random())  # Simulate time taken to produce an item

    print("Producer received event. Exiting...")

# Function for the consumer, taking items from the queue
def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        try:
            item = queue.get(timeout=0.05)  # Take item from the queue
            print(f"Consumer consumed item: {item}")
            queue.task_done()
        except:
            continue

    print("Consumer received event. Exiting...")

if __name__ == "__main__":
    q = Queue(maxsize=10)  # Shared queue between producer and consumer
    event = threading.Event()  # Event to stop the threads

    # Creating the producer and consumer threads
    producer_thread = threading.Thread(target=producer, args=(q, event))
    consumer_thread = threading.Thread(target=consumer, args=(q, event))

    # Start the threads
    producer_thread.start()
    consumer_thread.start()

    # Let the producer and consumer run for 5 seconds
    time.sleep(5)

    # Signal the producer and consumer to stop
    event.set()

    # Wait for both threads to finish
    producer_thread.join()
    consumer_thread.join()

    print("All tasks completed.")
