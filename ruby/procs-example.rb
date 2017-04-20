people_one = [54, 21, 45, 76, 12, 11, 67, 5]
people_two = [21, 54, 65, 32, 65, 87, 21, 12]


over = Proc.new { |age| age > 30 }

group_one = people_one.select(&over)  # A way to call procs
group_two = people_two.select(&over)

puts group_one, "", group_two.reverse!
