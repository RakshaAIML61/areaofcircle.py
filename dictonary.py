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
for i in topics:
  print(i,topics)
    
{'animal': 'cat', 'bird': 'peacock'}
{'animal': 'bat', 'bird': 'peacock'}
{'animal': 'bat'}
animal {'animal': 'bat'}
