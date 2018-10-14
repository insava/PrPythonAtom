class HashMap:

    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def get_key(self):
            return self.key
        def get_value(self):
            return self.value
        def __eq__(self, other):
            if self.key == other.key:
                return True
            else:
                return False

    def __init__(self, bucket_num = 64):
        self.num = bucket_num
        self.list = []
        for i in range(bucket_num):
            self.list.append([])

    def get(self, key, default_value = None):
        for i in self.list[hash(key) % self.num]:
            if i.key == key:
                return {i.key, i.value}
        return default_value

    def put(self, key, value):
        element = Entry(key, value)
        for i in self.list[hash(key) % self.num]:
            if i.key == element.key:
                i.value = value
                break
        self.list[hash(key) % self.num].append(element)

    def __len__(self):
        return self.num

    def _get_hash(self, key):
        return hash(key)
    def _get_index(self, key):
        return hash(key) % self.num

    def values(self):
        a = []
        for backet in self.list:
            for elem in backet:
                a.append(elem.value)
        return(a)

    def keys(self):
        a = []
        for backet in self.list:
            for elem in backet:
                a.append(elem.key)
        return(a)

    def items(self):
        a = []
        for backet in self.list:
            for elem in backet:
                a.append({elem.key, elem.value})
        return(a)

    def __str__(self):
        print(self.items)


class HashSet(HashMap):
    def get(self, key):
        if super().get(key) is None:
            return None
        else
            return key

    def put(self, key):
        return super().put(key, 0)

    def __len__(self):
        return super().__len__()

    def values(self):
        return super().values()























