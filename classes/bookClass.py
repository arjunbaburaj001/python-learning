class Book:
    def __init__(self, title, author, current_page=1):
        self.title = title
        self.author = author
        self.current_page = int(current_page)
    
    def book_info(self):
        return f"title: {self.title}, author: {self.author}, current page: {self.current_page}"
    
    def bookmark(self, page_number):
        self.current_page = page_number
        print(f"Bookmark set ot page {self.current_page}")

book1 = Book("Percy Jackson", "Rick Riordan", 129)
print(book1.book_info())
book1.bookmark(278)
print(book1.book_info())