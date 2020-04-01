from customer import customerList

cl = customerList()
print(cl.data)
cl.delete()
print(cl.data)


cl.delete(2)
#d = {'fname':'Testguy','lname':'test','email':'a@a.com','password':'123','subscribed':'1'}
cl.set('fname','test')
cl.set('lname','test')
cl.set('email','a@a.com')
cl.set('subscribed','True')
cl.set('password','12345')
cl.add()
#cl.add()

#print(cl.data)
#print(cl.data[0])
#cl.data[0]['email']) = 'b@b.com'
#print(cl.data[0]['email'])

cl.verifyNew()
