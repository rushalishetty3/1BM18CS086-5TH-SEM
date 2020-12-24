echo "Enter two numbers: "
read a
read b

echo "1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n"
echo -n "Enter your choice: "
read ch

case "$ch" in
	1) sum=$(echo "$a+$b"|bc)
		echo "\nSum= "$sum ;;
	2) diff=$(echo "$a-$b"|bc)
		echo "\nDiff= "$diff ;;
	3) prod=$(echo "$a*$b"|bc)
		echo "\nProduct= "$prod ;;
	4) quot=$(echo "$a/$b"|bc)
		echo "\nQuotient= "$quot ;;
	*) echo "Wrong option" ;;
esac
