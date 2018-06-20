read n
sum=0


# {start..end} expansion don't work with variable because
# BASH expands it as textual expansion
# without any syntax expansion
for x in $( seq 1 $n )
do
  read $tmp
  let sum+=tmp
done


printf "%.3f\n"  $( echo "$sum/$n" | bc -l )
