##############################################
# Bloom Filter                               #
# by Vishal Nirmal                           #
##############################################




class BloomFilter:

    def __init__(self, size, hash_functions):

        self.size = size*15

        self.bit_array = list([0]*self.size)

        self.hash_functions = hash_functions

    def add_element(self, data):

        for i in self.hash_functions:

            index = i(str(data))%self.size

            self.bit_array[index] = 1

    def check_element(self, data):

        for i in self.hash_functions:

            index = i(str(data))%self.size

            if self.bit_array[index] == 0:

                return False

        return True

    def add_elements(self, arr):

        for i in arr:

            self.add_element(i)

def XORHash(key):

    h = 0

    for i in key:

        h ^= ord(i)

    return h

def shiftAddXorHash(key):

    h = 0

    for i in key:

        h ^= (h >> 5) + (h << 2) + ord(i)

    return h

def search(arr, data):

    hash_functions = [XORHash, shiftAddXorHash]

    fltr = BloomFilter(len(arr), hash_functions)

    fltr.add_elements(arr)

    result = fltr.check_element(data)

    del(fltr)

    return result