echo -n "Enter the number of cpu cores: "
read cpus

for((cpu=0; cpu< $cpus; ++cpu))
do
    cpupower -c $cpu frequency-info
done
