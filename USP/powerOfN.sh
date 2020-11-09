echo -n "Enter number: "
read n
echo -n "Enter power: "
read pow

ans=1

for counter in $(seq 1 $pow)
do
	ans=$((ans \* n))
done

echo "Answer = "$ans
