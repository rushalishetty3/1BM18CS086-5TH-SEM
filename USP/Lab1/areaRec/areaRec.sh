echo "Enter length and breadth: "
read l
read b
area=$(echo "scale=2;$l*$b"|bc)
echo "Area = "$area

