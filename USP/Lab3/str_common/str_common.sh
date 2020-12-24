echo "Enter first string: "
cat > file1.txt

echo "Enter first two: "
cat > file2.txt

echo "Common string: "

comm -12 file1.txt file2.txt
