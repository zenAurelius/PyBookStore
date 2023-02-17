
import requests
from bookcase import Author, Book

class PyOpenLibrary:
   base_url = "https://openlibrary.org/api/books?bibkeys=" 

   def getBookISBN(self, isbn):
      '''Les données qu'on veut recupérer : 
         - titre
         - editeur
         - format ?
         - année de publication ?
         - liste des auteurs (ol_id)'''
      r = requests.get(f"{self.base_url}ISBN:{isbn}&format=json&jscmd=data", verify=False)
      detail = r.json().get(f"ISBN:{isbn}")
      print(detail)  
      
      book = Book().fromOL(detail)
      return book

   def getISBN(self, isbn):
      r = requests.get(f"https://openlibrary.org/isbn/{isbn}.json", verify=False)
      print("ISBN")
      print(r.json())

   def getBook(self, book_id):
      r = requests.get(f"https://openlibrary.org/books/{book_id}.json", verify=False)
      print("BOOK")
      print(r.json())
