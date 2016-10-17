for((cpu=0; cpu<4; ++cpu))
do
    cpupower -c $cpu frequency-info
done