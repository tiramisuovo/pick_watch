import os
import json

class ContentItem:
    """Base class representing a piece of entertainment content"""
    def __init__(self, title, release_date, overview, poster):
        self.title = title # str
        self.release_date = release_date # str
        self.overview = overview # str
        self.poster = poster # poster path
    
    def to_dict(self):
        return {
            "title": self.title,
            "release_date": self.release_date,
            "overview": self.overview,
            "poster": self.poster
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["release_date"], data["overview"], data["poster"])

class Movie(ContentItem):
    pass

class Anime(ContentItem):
    pass

class FavList:
    """Manages a list of favorite content items, methods including save, load, add, delete, and find"""
    def __init__(self, mode=0):
        self.favlist = [] # fav list of contentItem
        self.mode = mode # 0 = movie, 1 = anime
        if self.mode == 0:
            self.cls = Movie
            self.file_path = os.path.join(os.path.expanduser("~"),"fav_movies.json")
        elif self.mode == 1:
            self.cls = Anime
            self.file_path = os.path.join(os.path.expanduser("~"),"fav_anime.json")
            
    def __repr__(self):
        titles = []
        for content in self.favlist:
            titles.append(content.title)
        return f"{titles}"
    
    def save_to_file(self):
        data = []
        for content in self.favlist:
            data.append(content.to_dict())
        with open(self.file_path,"w") as f:
            json.dump(data, f, indent = 4)
    
    def load_from_file(self):
        self.favlist.clear()
        try:
            with open(self.file_path,"r") as f:
                loaded_data = json.load(f)
                for content in loaded_data:
                    self.favlist.append(self.cls.from_dict(content))
        except FileNotFoundError:
            pass
        return self.favlist
    
    def add(self, content):
        self.favlist.append(content)
    
    def find(self, title):
        # find a fav content given title
        for content in self.favlist:
            if content.title == title:
                return content
            
    def delete(self, content):
        # delete a content from the favlist
        new_favlist = []
        for c in self.favlist:
            if content.title != c.title or content.overview != c.overview or content.release_date != c.release_date:
                new_favlist.append(c)
        self.favlist = new_favlist
        return self.favlist
    
class MovieFavList(FavList):
    def __init__(self):
        super().__init__(mode=0)

class AnimeFavList(FavList):
    def __init__(self):
        super().__init__(mode=1)