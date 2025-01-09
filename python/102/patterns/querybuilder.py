class QueryBuilder:
    def __init__(self, collection):
        self.collection = collection

    def where(self, condition):
        self.collection = filter(condition, self.collection)
        return self  # Fluent interface: zwraca obiekt tej samej klasy

    def select(self, transform):
        self.collection = map(transform, self.collection)
        return self

    def to_list(self):
        return list(self.collection)

    def first(self):
        return next(iter(self.collection), None)

# Przykład użycia
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

query = QueryBuilder(data)
result = query.where(lambda x: x > 5).where(lambda x: x % 2 == 0).select(lambda x: x * 2).to_list()

print(result)  # [12, 16, 20]