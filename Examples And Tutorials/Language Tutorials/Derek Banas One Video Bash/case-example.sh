read -p "How old are you: " age


case $age in
    [0-4])
        echo "Too young"
    ;;
    5)
        echo "Kindergarden"
    ;;
    [6-9]|1[0-8])
        # This case checks if age in between 6-9 or 10-18
        grade=$((age-5))
        echo "Go to grade $grade"
    ;;
    *)
        echo "To old"
esac

