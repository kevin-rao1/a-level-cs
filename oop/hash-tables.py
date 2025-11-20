def hash(key:str):
    sum = 0
    for i in range(len(key)):
        sum += ord(key[i]) * ord(key[i])
    return sum % 523


class Hash_table:
    def __init__(self):
        self._table = [None for i in range(523)]

    def insert(self, key, value):
        index = 0
        index = hash(key)
        assert index <= 523
        self._table[index] = value

    def find(self, key):
        value = self._table[hash(str(key))]
        assert value != None
        return value

def test():
    table = Hash_table()
    table.insert("PEN", "PLUME")
    table.insert("CAT", "CHAT")
    table.insert("NOW", "MAINTENANT")
    assert table.find("PEN") == "PLUME"
    assert table.find("CAT") == "CHAT"
    assert table.find("NOW") == "MAINTENANT"
    print("All tests passed")
    return 0

if __name__ == "__main__":
    test()