read -p "Enter lower limit : " x
if [ $x -le 1 ]
then
    echo "Enter Lower Limit greater than 1"
    exit
fi
read -p "Enter upper limit : " y

echo "\nPrime Numbers : "

while [ $x -le $y ]
do

LIMIT=$((x-1))
a=2

while [ $a -le $LIMIT ] 
        do
                check=$(echo `expr $x % $a`)
                if [ $check -eq 0 ]
                then
                        break
                fi
	a=$(( a + 1 ))
        done

if [ $a -gt $LIMIT ]
then
        echo "$x"
fi
x=$((x+1))
done
