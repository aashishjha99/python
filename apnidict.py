mydict = { "Mango" : 'AAM' ,"Apple":'Sev',"Pineapple": 'ananas',"Home":'Ghar'}

print("words whose meaning is available")
print(mydict.keys())
print("give the word to search")
word = input()
print("the searcheed word is", word," meaning is",mydict[word])