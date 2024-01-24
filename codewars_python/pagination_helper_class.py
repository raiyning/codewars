# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return round(self.item_count()/self.items_per_page)
        
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.page_count():
            return -1
        if page_index < self.page_count():
            return self.items_per_page
        if page_index == self.page_count():
            return self.item_count() % self.items_per_page
 
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        pass

helper = PaginationHelper(['a','b','c','d','e','f'], 4)

print(helper.item_count())
print(helper.page_count())
print(helper.page_item_count(1))