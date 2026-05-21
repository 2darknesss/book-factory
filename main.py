import random

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"

def generate_random_book():
    titles = ["1984", "Dune", "Foundation", "Neuromancer", "Solaris"]
    authors = ["George Orwell", "Frank Herbert", "Isaac Asimov", "William Gibson", "Stanislaw Lem"]
    
    return Book(
        title=random.choice(titles),
        author=random.choice(authors),
        year=random.randint(1950, 2023)
    )

if __name__ == "__main__":
    random_book = generate_random_book()
    print(random_book)