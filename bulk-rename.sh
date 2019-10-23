for f in *; do mv $f "`echo $f | grep -oi "E[[:digit:]]\+" | awk '{ print toupper($0) }'`.mkv"; done
