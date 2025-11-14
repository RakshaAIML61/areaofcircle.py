#dictonary
topics= {
    "animal"   : "cat",
    "bird"     : "peacock"
     }
print(topics)
topics["animal"] = "bat"
print(topics)
del topics["bird"]
print(topics)
{'animal': 'cat', 'bird': 'peacock'}
{'animal': 'bat', 'bird': 'peacock'}
{'animal': 'bat'}
