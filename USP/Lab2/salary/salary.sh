echo -n "Enter da: "
read da
echo -n "Enter hra: "
read hra
echo -n "Enter basic: "
read basic

total=`expr $da + $hra + $basic`

echo "Total salary: $total"

