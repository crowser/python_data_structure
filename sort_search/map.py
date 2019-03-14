#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size      #key
        self.data = [None] * self.size       #value

    def put(self, key, data):
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.nextslotfunction(hashvalue, self.size, key)
                if self.slots[nextslot] == None:
                    self.slots[nextslot] == key
                    self.data[nextslot] == data
                elif self.slots[nextslot] == key:
                    self.data[nextslot] = data

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def nextslotfunction(self, hashvalue, size, key):
        nextslot = self.rehash(hashvalue, size)
        while self.slots[nextslot] != None and self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot, size)
        return nextslot

    def printmap(self):
        for i, j in zip(self.slots, self.data):
            if i != None:
                print("{" + "{}:{}".format(i, j) + "}")

    def get(self, key):
        startslot = self.hashfunction(key, self.size)
        data = None
        found = False
        position = startslot

        if self.slots[startslot] == key:
            stop = True
            found = True
            data = self.data[startslot]
        else:
            position = self.rehash(startslot, self.size)
            while not found:
                if self.slots[position] == key:
                    found = True
                else:
                    position = self.rehash(position, self.size)
                if position == startslot:
                    break
            data = self.data[position]

        return data







mymap = HashTable()

mymap.put(1, 'world')
print(mymap.get(2))