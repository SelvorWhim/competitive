class PaginationHelper:
  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.num_items = len(collection)
      self.page_size = items_per_page
      # not strictly necessary but convenient to avoid repeating calculations:
      tail = self.num_items % self.page_size
      self.last_page_size = tail if tail > 0 else self.page_size
      self.num_pages = (self.num_items - 1) // self.page_size + 1 # modular division that rounds up without floats
  
  # returns the number of items within the entire collection
  def item_count(self):
      return self.num_items
  
  # returns the number of pages
  def page_count(self):
      return self.num_pages
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self, page_index):
      if page_index < 0 or page_index >= self.num_pages:
          return -1
      if page_index == self.num_pages - 1:
          return self.last_page_size
      return self.page_size
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      return item_index // self.page_size if 0 <= item_index < self.num_items else -1
