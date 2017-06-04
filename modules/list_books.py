'''
Using Goodreads API to have a the database of books. Saving it 
to the text file called 'book.txt' with the comand line.
(python list_books.py > book.txt)
'''
from goodreads import client
gc = client.GoodreadsClient('6YrisUQhu9CMAUHNVp2A', 'iQ0dZVXJk0W4Ci9FyYux7yKxUNfBXFtfK7fzYlk')
for l in range(200, 300):
    try:
        book = gc.book(l)
        print(book.title)
    except Exception as e:
        pass






#6YrisUQhu9CMAUHNVp2A
#secret: iQ0dZVXJk0W4Ci9FyYux7yKxUNfBXFtfK7fzYlk