class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1
    
class PaginationHelper2:

    def __init__(self, collection: list, items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return __import__('math').ceil(self.item_count() / self.items_per_page)

    def page_item_count(self, page_index):
        if self.item_count() % self.items_per_page and page_index == self.page_count() - 1:
            return self.item_count() - self.items_per_page * (self.page_count() - 1)
        return self.items_per_page if page_index in range(self.page_count()) else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page if item_index in range(self.item_count()) else -1