echo -n "Enter n: "
read n

a=0
b=1

echo "Fibonacci series: "

while [ $n -gt 0 ] 
do
	echo $a" "
	c=$((a + b))
	a=$((b))
	b=$((c))
	n=$((n - 1))
done

