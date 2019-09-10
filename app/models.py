class source:
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description
        

class article:
    def __init__(self,article_id,author,title,description,url,urlToImage,publishedAt,content):
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
       
