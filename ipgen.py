import random 

ip=str(random.randint(0,255))
for i in range(3):
	t=random.randint(0,255)
	ip=ip+"."+ str(t)

print(ip)
