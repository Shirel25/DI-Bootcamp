class Pagination:
    def __init__(self, items = None, pageSize = 10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)
        self.currentPage = 1
        # len(the number of items) + len(the number of pages)-1 in the case the items don't fill completely the last page 
        self.totalPages = (len(self.items) + self.pageSize - 1) // self.pageSize

    def getVisibleItems(self):
        start = (self.currentPage-1) * self.pageSize   # lists start at 0 and currentPage = 1
        end = start + self.pageSize
        visibleItems = self.items[start:end]
        print(visibleItems)
        return visibleItems
    
    def prevPage(self):
        if self.currentPage > 1 :
            self.currentPage -= 1
            self.getVisibleItems() 
        else:
            print("You're already on the first page.")
        return self
    
    def nextPage(self):
        if self.currentPage < self.totalPages :
            self.currentPage += 1
            self.getVisibleItems() 
        else:
            print("You're already on the last page.")
        return self
    
    def firstPage(self):
        self.currentPage = 1
        self.getVisibleItems() 

    def lastPage(self):
        self.currentPage = self.totalPages
        self.getVisibleItems() 

    def goToPage(self, pageNum):
        if pageNum < 1:
            self.firstPage()
        elif pageNum > self.totalPages:
            self.lastPage()
        else:
            self.currentPage = pageNum
            self.getVisibleItems() 
    
            

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 3)
p.getVisibleItems() # ['a', 'b', 'c']

p.prevPage() # You're already on the first page.
p.nextPage() # ['d', 'e', 'f']

p.firstPage() # ['a', 'b', 'c']
p.lastPage() # ['y', 'z']

print("page 6 :")
p.goToPage(6) # ['p', 'q', 'r']
p.nextPage().nextPage() # ['s', 't', 'u']
                        # ['v', 'w', 'x']

print("closest to first page")
p.goToPage(-3) # ['a', 'b', 'c']
print("closest to last page")
p.goToPage(100) # ['y', 'z']

print("--------------")
p.goToPage(2) # ['d', 'e', 'f']
p.nextPage().nextPage().prevPage() # ['g', 'h', 'i']
                                   # ['j', 'k', 'l']
                                   # ['g', 'h', 'i']
