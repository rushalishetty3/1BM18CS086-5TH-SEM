echo -n "Enter number: "
read n

if [ $(expr $n % 2) -eq 0 ]
then
	echo "Even number"
else
	echo "Odd number"
fi
