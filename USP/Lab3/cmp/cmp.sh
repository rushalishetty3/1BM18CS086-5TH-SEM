read -p "Enter first string: " string1
read -p "Enter second string: " string2

if [ "$string1" = "$string2" ]
then 
	echo $string1 " and " $string2 " are equal" 
else
	echo $string1 " and " $string2 " are not equal" 
fi
