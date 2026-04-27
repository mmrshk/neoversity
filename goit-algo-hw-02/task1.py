import uuid

from queue import Queue

def generate_request(q: Queue) -> None:
    request_id = uuid.uuid4();
    q.put(request_id)

    print(f"Added: {request_id}")


def process_request(q: Queue) -> None:
    item = q.get()
    print("Processed:", item)

def run_auto_mode(q: Queue) -> None:
    print("Auto mode started. Type 'stop' to return to menu.")
    step = 0

    while True:
        step += 1

        print(f"\n--- step {step} ---")

        generate_request(q)

        print(f"Queue now: {list(q.queue)}")

        cmd = input("Click Enter or 'stop' to exit auto: ").strip().lower()

        if cmd == "stop":
            while not q.empty():
                process_request(q)

            print("Queue is empty")
            print("Auto mode stopped.")
            break

def print_help() -> None:
    print("Available commands:")
    print("  add      - add new request")
    print("  dequeue  - process first request")
    print("  show     - show current queue")
    print("  help     - show this message")
    print("  stop     - exit program")
    print("  auto     - will add and dequeue requests automatically")

def main() -> None:
    q = Queue()
    print_help()

    while True:
        text = input("\nEnter command: ").strip().lower()

        if text == "stop":
            print("Bye!")
            break
        elif text == "add":
            generate_request(q)
            print(f"Queue: {list(q.queue)}")
        elif text == "dequeue":
            process_request(q)
        elif text == "auto":
            run_auto_mode(q)
        elif text == "show":
            print(f"Queue: {list(q.queue)}")
        elif text == "help":
            print_help()
        elif text == "":
            print("Empty input. Type 'help' to see commands.")
        else:
            print(f"Unknown command: '{text}'. Type 'help' to see valid commands.")


if __name__ == "__main__":
    main()
