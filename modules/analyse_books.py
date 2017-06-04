import itunespy
import random
from time import sleep

class Books:
    def __init__(self):
        pass

    def read_file(self):
        '''
        This method reads file called "book.txt" and saves the data
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



    def find_book(self):
        '''
        Checks the list from the method read_file() whether the books are present
        in the database of iTunes Store. Then saves only the name of the book, the author
        and price to the separate lists.
        '''
        books = list(self.read_file())
        book_attributes_needed = []
        personal_lst = []
        for book in books:
            try:
                lookup = itunespy.search_book(book)
                if lookup[0].type == 'ebook':
                    personal_lst.append(lookup[0].track_name)
                    personal_lst.append(lookup[0].artist_name)
                    personal_lst.append(lookup[0].price)
                    personal_lst.append(lookup[0].genres)
                    personal_lst.append(lookup[0].track_view_url)
                    book_attributes_needed.append(personal_lst)
                    personal_lst = []
            except:
                pass
        return book_attributes_needed


    def genres(self):
        '''
        Method prints all genres.
        :return: list of genres of books.
        '''
        needed_attributes = self.find_book()
        genre = set()
        for book_lst in needed_attributes:
            for element in book_lst:
                if element == book_lst[-2]:
                    for g in element:
                        genre.add(g)
        print("Here is the list of genres: ")
        for g in genre:
            print(g)
        return list(genre)


    def analyse_data(self):
        '''
        Asks user to input the price and the genre of book he wants to read/buy.
         Then, the books that suit the most for these requirements.
        :return: book title, author, price and genre of the book that user can like.
        '''
        needed_attributes = self.find_book()
        genres = self.genres()
        gen = ''
        result_lst = []
        result = ''
        price = eval(input("What price of the book do You prefer? If You want it free, just type '0'(USD): "))
        genre = input("Please, type 1 genre which you have chosen from the list above: ")
        for book in needed_attributes:
            if genre not in genres:
                print("This genre is not in the list")
            elif genre in book[3]:
                try:
                    if 2 <= price <= 5 and 2 <= book[2] <= 5:
                        result_lst.append(book)
                    elif 5 < price <= 8 and 5 < book[2] <= 8:
                        result_lst.append(book)
                    elif 8 < price <= 11 and  8 < book[2] <= 11:
                        result_lst.append(book)
                    elif 11 < price <= 15 and  11 < book[2] <= 15:
                        result_lst.append(book)
                    elif 15 < price <= 20 and  15 < book[2] <= 20:
                        result_lst.append(book)
                    elif 20 < price <= 25 and  20 < book[2] <= 25:
                        result_lst.append(book)
                    elif 25 < price <= 30 and  25 < book[2] <= 30:
                        result_lst.append(book)
                    elif 30 < price <= 40 and  30 < book[2] <= 40:
                        result_lst.append(book)
                    elif price > 40 and book[2] > 40:
                        result_lst.append(book)
                    elif price == 0 and book[2] == 0.0:
                        result_lst.append(book)
                except:
                    pass
        for book in result_lst:
            for g in book[3]:
                gen += str(g)
                if g != book[3][-1]:
                    gen += ', '
                elif g == book[3][-1]:
                    gen += '.'
            result = "\nTitle: " + str(book[0]) + "\n" + "Author: " + str(book[1]) + '\n' + "Price: " + str(book[2]) + '\n' + "Genres: " + gen + '\n'+ 'Url to the iTunes: ' + book[4] +'\n \n'
            print(result)
            result = ''
            gen = ''
        return result


#book = Books()
#print(book.analyse_data())