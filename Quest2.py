fibo=[1,2];
sum=0;
while (fibo[-1]+fibo[-2]<4000000):
	fibo+=[fibo[-1]+fibo[-2]];
for i in fibo:
	sum+=i;
print("\nThe sum of fibo values bellow 4 000 000 is: "+str(sum));
input();
