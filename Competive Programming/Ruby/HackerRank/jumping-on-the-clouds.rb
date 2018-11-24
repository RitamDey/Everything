def jumpingOnClouds(cloud_array, num_clouds)
    pos = 0
    steps = 0

    while pos <= num_clouds - 1
        if cloud_array[pos+2] == 0
            steps += 1
            pos += 2
        elsif cloud_array[pos+1] == 0
            steps += 1
            pos += 1
        else
            break
        end
    end

    return steps
end

if __FILE__ == $0
    num_clouds = $stdin.gets().to_i()
    cloud_array = $stdin.gets().rstrip().split(' ').map(&:to_i)

    $stdout.puts(jumpingOnClouds(cloud_array, num_clouds))
end
