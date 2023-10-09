import datetime

class MultiClipboardList:

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    class Item:
        def __init__(self, name, value):
            self.name = name
            self.value = value 
            self.timestamp = datetime.datetime.now()
    
    def clear_list(self):
       self.items.clear()

    def item_exists(self, name):
        #Returns a false if items does not exist, or true if it does
        itemExists = False
        for index, item in enumerate(self.items):
            if item.name == name:
                itemExists = True
                break
        return itemExists      

    def add_item(self, name, value):
        item = self.Item(name, value)
        self.items.append(item)

    def get_item_by_name(self, name):
        for index, item in enumerate(self.items):
            if item.name == name:
                return item.value

    def get_last_item(self):
        return self.items[-1]

    def delete_item(self, index):
        del self.items[index]

    def delete_last_item(self):
        #Deletes first item that was added which is the last item on the list on the screen
        del self.items[0]
        
    def delete_item_by_name(self, name):
        for index, item in enumerate(self.items):
            if item.name == name:
                del self.items[index]
                break