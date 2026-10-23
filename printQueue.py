from collections import deque

print_queue = deque()

print_queue.append({"id": "J01", "pages": 5})
print_queue.append({"id": "J02", "pages": 10})
print_queue.append({"id": "J03", "pages": 2})

print("Printing jobs in FIFO order:")

while print_queue:
    job = print_queue.popleft()
    print(
        f"Job {job['id']} - "
        f"{job['pages']} page(s)"
    )