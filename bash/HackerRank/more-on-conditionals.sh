# Given three integers (X, Y, and Z) representing the three sides 
# of a triangle, identify whether the triangle is 
# Scalene, Isosceles, or Equilateral.


read x 
read y 
read z


if [[ ($x -eq $y) && ($y -eq $z) ]]; then
    echo "EQUILATERAL"
elif [[ ($x -eq $y) || ($y -eq $z) || ($x -eq $z) ]]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
