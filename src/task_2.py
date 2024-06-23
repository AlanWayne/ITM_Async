from threading import Thread
from os import makedirs

def create_file(index: int = 0):
    with open(f"text/file_{index}.txt", "w") as file:
        file.write(f"{index}")


def create_files(number: int = 10):
    makedirs("text", exist_ok=True)
    
    for index in range(number):
        thread = Thread(target=create_file, args=[index])
        thread.start()


if __name__ == "__main__":
    create_files()
