echo "No of parameters: "$#

if [ $# -eq 2 ]
then 
	count=$(grep -c "$1" $2)
	if [ $count -gt 0 ]
	then
		grep "$1" $2
	else
		echo "No match"
	fi
else
	echo "wrong no of parameters"
fi
