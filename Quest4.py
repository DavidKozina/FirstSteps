maxPalindrome=0;
for x in range(100,999):
	for y in range(100,999):
		decimal=str(x*y);
		rev="";
		for s in decimal:
			rev=s+rev;
		if (decimal==rev)and(x*y>maxPalindrome):
			maxPalindrome=x*y;
print("The largest palindrome made from the product of two 3-digit numbers is: "+str(maxPalindrome));
input();			
