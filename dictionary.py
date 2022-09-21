# task-16 dictionary

#creating dict():
a= dict()
print(type(a))
#inserting values into dict:
a['name']='ratnakar'
a["age"]=24
print(a)
#access item in dict
print(a['name'])
#change item in dict
a['age']=16
print(a)
#removing items from dict
a.pop('age')

a.update({"age":24,"course":"python"})
print(a)