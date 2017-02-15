i=1;
n=600851475143;
maxPF=0;
while (i<=n):
	i+=1;
	if (n%i==0):
		n=n//i;
		maxPF=max(maxPF,i);
		i=1;	
print("Greatest prime factors of number 600851475143 is: "+str(maxPF));
input();
