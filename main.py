import json

from tinydb import TinyDB, Query
from tinydb_serialization import Serializer, SerializationMiddleware
from tinydb.storages import JSONStorage
from tinyODM import TinyModel
from pyOpenLibrary import PyOpenLibrary
from bookcase import Book, Author

#def __init__(self, **kwargs):
#for key, value in kwargs.items():
#            setattr(self, key, value)

def add_books():
    isbn = '9782070370818'
    ol = PyOpenLibrary()
    b = ol.getBookISBN(isbn)
    print(b)
    print(b.authors)

    for k,v in b.__dict__.items():
        print(k)
        print(type(v))

    #existing_book = Book.get(b.ol_id)
    #if not existing_book :
    #    b.insert()

class TinyModelSerializer(Serializer):
    OBJ_CLASS = TinyModel  # The class this serializer handles

    def encode(self, obj):
        print(obj)
        id = obj.get()
        if id is None :
            print('insert')
            id = obj.insert()
        return f"{str(obj.__class__)}|{str(id)}"

    def decode(self, s):
        return s

serialization = SerializationMiddleware(JSONStorage)
#serialization.register_serializer(TinyModelSerializer(), 'TinyModel')

db = TinyDB('bookstore2.json', storage=serialization)
Author.collection = db.table('authors')
Book.collection = db.table('books')

#db.truncate()
#db.drop_tables()

# recherche et ajout d'un livre
#add_books()

a = Author(ol_id='1A',name='toto')
a.remove()
b = Book(ol_id='2M',title='livre2',authors=[a])
#print(b)

b.insert()

book = Book.get_id('2M')
print(book)
print(book.authors)


# lecture de la liste
# books = Book.get_all()
# print(books)
 
# b_get = Book.get(books[0].ol_id)
# print(b_get)
# print(b_get.authors)