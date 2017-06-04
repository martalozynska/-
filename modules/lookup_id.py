import itunespy
import random
from time import sleep

def read_file():
    '''
    This function reads file called "book.txt" and saves the data
    to the list, then formates it to set (if some books appear twice and more times)
    and then back to list.
    '''
    lst_of_books = []
    file = open("books.txt", 'r')
    for line in file:
        line = line.strip()
        lst_of_books.append(line)
    lst_of_books = set(lst_of_books)
    return lst_of_books

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
               personal_lst.append(lookup[0].track_name)
               personal_lst.append(lookup[0].artist_name)
               personal_lst.append(lookup[0].price)
               book_attributes_needed.append(personal_lst)
               personal_lst = []
        except:
            pass
    
    return book_attributes_needed
  
needed_attributes = find_book()
print(needed_attributes)
def analyse_data():
    result_lst = []
    result = ''
    price = eval(input("What price of the book do You prefer? If You want it free, just type '0': "))
    for book in needed_attributes:
         try:
            if 2 <= price <= 5 and 2 <= book[3] <= 5:
                result_lst.append(book)
            elif 5 < price <= 8 and 5 < book[3] <= 8:
                result_lst.append(book)
            elif 8 < price <= 11 and  8 < book[3] <= 11:
                result_lst.append(book)
            elif 11 < price <= 15 and  11 < book[3] <= 15:
                result_lst.append(book)
            elif 15 < price <= 20 and  15 < book[3] <= 20:
                result_lst.append(book)
            elif 20 < price <= 25 and  20 < book[3] <= 25:
                result_lst.append(book)
            elif 25 < price <= 30 and  25 < book[3] <= 30:
                result_lst.append(book)
            elif 30 < price <= 40 and  30 < book[3] <= 40:
                result_lst.append(book)
            elif price > 40 and book[3] > 40:
                result_lst.append(book)
            elif price == 0 and book[3] == 0.0:
                result_lst.append(book)
         except:
             pass
    for book in result_lst:
        result = "Title: " + str(book[0]) + "\n" + "Author: " + str(book[1]) + '\n' + "Price: " + str(book[3]) + '\n'
        print(result)
        result = ''


    return result


#print(analyse_data())
