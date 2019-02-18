my_string='Hello Python!'
print(my_string)
print("\nREVERSE OF STRING")
print(my_string[::-1])
last=my_string.index('!')
print("\n! USING INDEX")
print(my_string[last])

string="information"
print(string[2::2])

print("")
band="Metallica"
genre="Heavy Metal"
print("The band {} plays music of {} genre".format(band,genre))
print("{genre} is played by {band}".format(genre="Heavy Metal",band="Metallica"))
print("{} plays Heavy Metal".format("Metallica"))

result=10/3
print("the result is {r:1.2f}".format(r=result))
print("")

name="ABC"
post="Headmaster"
print(f"Hello Im {name} and I work as {post}")

x=[]
print("")
dicts={'Count3':3,'Count1':1,'Count2':2}
print(sorted(dicts.values()))
#print(dicts.sort())
print("The dictionary can not be sorted, even if it can display the sorted values or keys, theres no permanent change made in the dictionary")
print("")

d={'simple_key':'hello'}
print(d['simple_key'])

d={'k':{'k2':'hello'}}
print(d['k']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])