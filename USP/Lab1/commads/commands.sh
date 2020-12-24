pwd
ls
ls -l
mkdir unix
echo "unix dir created"
cd unix
cat > abc.txt
cat abc.txt
echo "abc.txt created"
touch xyz.txt
echo "xyz.txt created"
cp xyz.txt abc.txt
echo "abc copied to xyz" 
cat xyz.txt
rm abc.txt 
rm xyz.txt
echo "deleted abc and xyz"
cd ..
rmdir unix
echo "deleted unix dir"
echo $HOME