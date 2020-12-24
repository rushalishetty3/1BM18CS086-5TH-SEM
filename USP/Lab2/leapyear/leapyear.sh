echo -n "Enter year:"
read year

if [ $(expr $year % 4) -eq 0 ]
then
	if [ $(expr $year % 100) -eq 0 ] && [ $(expr $year % 400) -ne 0 ]
	then
		echo "Not a leap year"
	else
		echo "Leap year"
	fi
else
	echo "Not a leap year"
fi
