echo -n "Enter number: "
read n

flag=0

for i in $(seq 2 $((n / 2)))
do
	if [ $((n % i)) -eq 0 ]
	then
		flag=1
		break
	fi
done

if [ $flag -eq 0 ]
then
	echo "Prime"
else
	echo "Not Prime"
fi
