class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        self.other = other
        # total_pages = other.pages
        return self.other + self.pages

    def __gt__(self, other):
        return self.pages > self.other




c = Book(100)

c1 = Book(200)

print(c1 + c)
print(c > c1)