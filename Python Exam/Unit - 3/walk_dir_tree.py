import os

if __name__ == "__main__":
    for root, dirs, files in os.walk('.', topdown=True):
        print(f"Root: {root}")
        print("Directories:", dirs)
        print("Files:", files)
        print('---------------------------------------------------------------------------------------------------------------------------------')
