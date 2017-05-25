import itunespy
def lookup_id():
    '''
    Checks if the digit is the ID of book. If yes - writes to the file.
    '''
    file = open('books.txt', 'w')
    for i in range(100000000,1000000000):
        try:
            lookup = itunespy.lookup_book(id=i)
            if lookup[0].type == 'ebook':
                lookup = str(lookup[0].track_id)
                file.write(lookup + '\n')
                print(lookup)
        except LookupError:
            print("Nothing")
        except ConnectionError:
            print("ZZzzzz...")
            time.sleep(5)
lookup_id()