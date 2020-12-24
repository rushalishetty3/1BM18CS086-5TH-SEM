echo "Enter base and height: "
read b
read h
area=$(echo "0.5*$b*$h"|bc)
echo "Area = "$area
