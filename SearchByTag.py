import json

class SearchByTag:
    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        if "items" in self._data:
            for item in self._data["items"]:
                if "tags" in item and self.query in item["tags"]:
                    yield item

    def first(self):
        try:
            return next(self.search())
        except StopIteration:
            raise StopIteration("No matching item found.")