class File:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True

with File('ttt.txt', 'r') as ttt:
   for i in ttt:
       print(i)

# with File('ttt.txt', 'w') as www:
#     www.write('Привет')

