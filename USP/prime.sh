read -p "Enter a number : " n

i=2
flag=0

while test $i -le `expr $n / 2`
do
if test `expr $n % $i` -eq 0
then
flag=1
fi

i=`expr $i + 1`
done 
if test $flag -eq 1
then
echo "The number is Not Prime"
else
echo "The number is Prime"
fi
