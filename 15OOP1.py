class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def readBook(self):
        print("Reading "+self.title)

hp=Book("Harry Potter","J K Rollings", 526)
rp=Book("Rich Dad Poor Dad","Robert Kiyosaki", 368)
bs=Book("Bitcoin Story","Sathoshi Nakamoto", 792)

hp.readBook()
rp.readBook()
bs.readBook()

