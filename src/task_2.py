from threading import Thread


def create_file(index: int = 0):
    with open(f"file_{index}.txt", "w") as file:
        file.write(f"{index}")
    print(f"File #{index} written successfully.")


def main():
    for index in range(10):
        thread = Thread(target=create_file, args=[index])
        thread.start()


if __name__ == "__main__":
    main()
