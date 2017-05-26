import itunespy
import random
from time import sleep

def read_file():
    '''
    This function reads file called "book.txt" and saves the data
    to the list, then formates it to set (if some books appear twice and more times)
    and then back to list.
    '''
    lst = []
    file = open("book.txt", 'r')
    for line in file:
        line = line.strip()
        lst.append(line)
    lst = set(lst)
    return lst

books = list(read_file())

def find_book():
    '''
    Checks the list from the function read_file() whether the books are present 
    in the database of iTunes Store. Then saves only the name of the book, the author
    and price to the separate lists.
    '''
    book_attributes_needed = []
    personal_lst = []
    for book in books:
        try:
            lookup = itunespy.search_book(book)
            if lookup[0].type == 'ebook':
               book_attributes_needed.append(lookup[0].track_name)
               book_attributes_needed.append(lookup[0].artist_name)
               book_attributes_needed.append(lookup[0].price)
               book_attributes_needed.extend([personal_lst])
               personal_lst = []
        except:
            pass
    
    
    return book_attributes_needed
   
find_book()

