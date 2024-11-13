class wind:
    def __init__(self):
        with open("wind.txt") as self.open:
            self.data = self.open.read()


m = wind 

print(m.data)