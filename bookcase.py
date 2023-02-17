import re
from tinyODM import TinyModel

class Author(TinyModel):
    
    id_name = 'ol_id'
    
    def __repr__(self) -> str:
        return f"Author : {self.name} ({self.ol_id})"

    def fromOL(self, ol_json):
        self.name = ol_json.get('name')
        result = re.search(r'authors\/(.+)\/', ol_json.get('url'))
        self.ol_id = result.group(1)
        return self

class Book(TinyModel):

    id_name = 'ol_id'
    
    def __init__(self, **kwargs):
        self.title : str = ''
        self.authors : list[Author] = []
        super().__init__(**kwargs)

    
    def __repr__(self) -> str:
        return f"Book : {self.title} ({self.ol_id})"

    def fromOL(self, ol_json):
        self.title = ol_json.get('title')
        result = re.search(r'books\/(.+)\/', ol_json.get('url'))
        self.ol_id = result.group(1)
        self.authors = [Author().fromOL(a) for a in ol_json.get('authors')]
        return self

    def from_db(self, b):
        self.title = b.get('title')
        self.ol_id = b.get('ol_id')
        return self

    def to_dict(self):
        return {'ol_id':self.ol_id, 'title':self.title, 'authors':self.get_children()}

    def get_children(self):
        ids = []
        for a in self.authors :
            author = a.__class__.get(a.ol_id)
        if author :
            ids.append(author.doc_id)
        else : 
            ids.append(a.insert())
        return ids

    @classmethod
    def get_all(cls):
        return [Book().from_db(b) for b in cls.table.all()]



    