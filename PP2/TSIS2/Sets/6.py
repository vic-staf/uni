#Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)