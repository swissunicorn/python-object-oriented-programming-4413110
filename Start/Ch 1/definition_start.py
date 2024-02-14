# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
#    pass
  def __init__(self, title): # special fcn for working w classes
    self.title = title

# TODO: create instances of the class
book1 = Book("The Way of Kings")
book2 = Book("Words of Radiance")

# TODO: print the class and property
print(book1)
print(book1.title)

# right-click --> open in integrated terminal --> "python filename"