class Books():
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'{self.name} is an awesome book with {self.pages} pages'    

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book has been deleted")    

b = Books(name="Lord of the Rings", pages=340)

print(b)
print(len(b))

del(b)