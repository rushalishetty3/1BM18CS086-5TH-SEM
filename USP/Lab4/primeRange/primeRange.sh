echo -n "Enter lower limit: "
read a

echo -n "Enter upper limit: "
read b

if [ $a -ge $b ]
then
	echo "Wrong limit"
else
	for i in $(seq $a $b)
	do
		flag=0
		for j in $(seq 2 $((i/2)))
		do
			if [ $((i%j)) -eq 0 ]
			then
				flag=1
				break
			fi
		done
		if [ $flag -eq 0 ]
		then
			echo $i
		fi
	done
fi
			
			
