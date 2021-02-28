# TODO: complete this class
import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.itemsNums = len(collection)
        self.pageSize = items_per_page
        self.ind = {i: collection[i] for i in range(len(collection), )}
        self.pages = [collection[i:i + items_per_page] for i in range(0, len(collection), items_per_page)]

    # returns the number of items within the entire collection
    def item_count(self):
        return self.itemsNums

    # returns the number of pages
    def page_count(self):
        return len(self.pages)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= len(self.pages) or page_index < 0: return -1
        return len(self.pages[page_index])

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= self.itemsNums or item_index < 0: return -1
        return math.ceil(item_index // self.pageSize)


collection = list(range(1, 25))
helper = PaginationHelper(collection, 10)
