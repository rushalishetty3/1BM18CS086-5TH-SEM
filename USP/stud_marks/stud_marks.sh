echo "Enter three subject marks: "
read m1
read m2
read m3

total=$(echo "$m1+$m2+$m3"|bc)
avg=$(echo "$total/3"|bc)

echo "Total= "$total
echo "Average= "$avg

if [ $avg -gt 85 ]
then
	echo "Distinction" 
elif [ $avg -gt 50 ]
then
	echo "First Class"
elif [ $avg -gt 35 ]
then 
	echo "Second Class"
else
	echo "Fail"
fi
