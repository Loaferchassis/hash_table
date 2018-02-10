import time


def main():
    print('Hello!')

    obj = HashMap()
    file = open('C:/Users/Alexander/PycharmProjects/tbms/text', encoding="utf8")
    obj.build(file)

    time1 = time.time()
    # print(buckets[0])
    # delete('give')
    for i in range(1, 10000):
        obj.search('never')

    print(time.time() - time1)


class HashMap:
    def __init__(self):
        self.num_of_buckets = 100
        self.buckets = [[] for _ in range(self.num_of_buckets)]

    def build(self, file):
        wordlist = file.readlines()
        # print(wordlist)
        for line in wordlist:
            for word in line.split(" "):
                self.insert(word)

        words = []
        for line in wordlist:
            for word in line.split(" "):
                words.append(word)
        # time1 = time.time()
        # for i in range(1, 10000):
        #     for word in words:
        #         if "never".__eq__(word):
        #             break
        # print(time.time() - time1)

    # hashFunction
    def hashFunction(self, key):
        return hash(key) % self.num_of_buckets

    # Insertion
    def insert(self, object):
        self.buckets[self.hashFunction(object)].append(object)

    # Delete
    def delete(self, object):
        self.buckets[self.hashFunction(object)].remove(object)
        print('Delete')

    # Search
    def search(self, object):
        mHash = self.hashFunction(object)
        for h in self.buckets[mHash]:
            if object.__eq__(h):
                return h, mHash


if __name__ == '__main__':
    main()
