def main():
    with open('input.txt', 'wb') as out:
        out.seek(100 * 1024 - 1)
        out.write(b"\0")


if __name__ == "__main__":
    main()

