aclNum = int(input("cual es el numero de IPv4 de su ACL? "))
if aclNum >= 1 and aclNum <= 99:
	print("Esto es una IPv4 ACL estandar.")
elif aclNum >=100 and aclNum <= 199:
	print("Esta es una IPv4 ACL extendida.")
else:
	print("No es ninguna de las dos, ni extendida ni estandar IPv4 ACL.")
