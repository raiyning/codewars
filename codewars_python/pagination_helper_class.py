# TODO: complete this class

import math
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
        return math.ceil(self.item_count() / self.items_per_page)
        
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        print('page_index is {} and page_count is {}'.format(page_index,self.page_count()))
        if page_index < 0:
            return -1
        page_index += 1
        if page_index > self.page_count():
            return -1
        if page_index < self.page_count():
            return self.items_per_page
        if page_index == self.page_count():
            if self.item_count() % self.items_per_page == 0:
                return self.items_per_page
            return self.item_count() % self.items_per_page
        return -1
 
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < self.item_count() and item_index >= 0 :
                return int(item_index/self.items_per_page)
        return -1

helper = PaginationHelper([], 4)


print(helper.item_count()) # should == 6
print(helper.page_count()) # should == 2
print(helper.page_item_count(0)) # should == 4
# print(helper.page_item_count(1)) # last page - should == 2
# print(helper.page_item_count(2)) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(-1)) # should == 1 (zero based index))
# print(helper.page_index(2)) # should == 0
# print(helper.page_index(20)) # should == -1
# print(helper.page_index(-10)) # should == -1 because negative indexes are invalid