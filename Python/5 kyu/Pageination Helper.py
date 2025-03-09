# For this exercise you will be strengthening your page-fu mastery.
# You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.
#
# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page.
# The types of values contained within the collection/array are not relevant.

class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.pages = int((len(self.collection) / self.items_per_page) + (len(self.collection) %  self.items_per_page > 0))

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return self.pages

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        page_no = page_index + 1
        if page_no > self.pages or page_index < 0:
            return -1
        elif page_no < self.pages:
            return self.items_per_page
        else:
            if self.item_count() % self.items_per_page > 0:
                return self.item_count() % self.items_per_page
            else:
                return self.items_per_page

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index + 1 <= self.item_count() and item_index >= 0:
            return int(item_index / self.items_per_page)
        else:
            return -1