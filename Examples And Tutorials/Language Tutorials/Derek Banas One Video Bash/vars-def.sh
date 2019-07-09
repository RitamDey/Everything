myName="Derek"

declare -r NUM1=5  # Creates a constant

num2=4

add=$((NUM1+num2))
sub=$((NUM1-num2))
mul=$((NUM1*num2))
div=$((NUM1/num2))

echo "5 + 4 = $add"  # Sting interpol
echo "5 - 4 = $sub" 
echo "5 + 4 = $mul" 
echo "5 + 4 = $div" 


echo $((5**2))
echo $((5%4))


rand=5
let rand+=4
echo "$rand"
echo "rand++ = $((rand++))"
echo "++rand = $((++rand))"
echo "rand-- = $((rand--))"
echo "--rand = $((--rand))"


num7=1.2
num8=3.4
num9=$(python3.6 -c "print($num7+$num8)")
echo $num9


cat << END
This text
prints on 
many lines
END
