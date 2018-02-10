num_of_buckets = 100
buckets = [[] for _ in range(num_of_buckets)]


def main():
    file = open('C:/Users/Alexander/PycharmProjects/tbms/text', encoding="utf8")
    wordlist = file.readlines()
    #print(wordlist)
    for line in wordlist:
        for word in line.split(" "):
            insert(word)
    #print(buckets[0])
    #delete('give')
    print(search('never'))


# hashFunction
def hashFunction(key):
    return hash(key) % num_of_buckets


# Insertion
def insert(object):
    buckets[hashFunction(object)].append(object)


# Delete
def delete(object):
    buckets[hashFunction(object)].remove(object)
    print('Delete')


# Search
def search(object):
    mHash = hashFunction(object)
    for h in buckets[mHash]:
        if object.__eq__(h):
            return h, mHash


if __name__ == '__main__':
    main()
