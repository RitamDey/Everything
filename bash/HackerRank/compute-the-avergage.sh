read n
expr=0

for _ in $(seq 1 $n); do
    read tmp
    #expr=`echo "$expr + $tmp" | bc`
    # We need to use this method becuase the bc method is slower
    let expr=$expr+tmp
done

printf "%.3f\n" $( echo "$expr/$n" | bc -l )
