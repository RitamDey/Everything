class Vehicle
  def initialize(name)
    @name = name
  end

  def start
    puts "Starting #{@name}"
    puts 'Vhrmmm!!!'
  end

  def stop
    puts "Stopping #{@name}"
    puts 'Khirrch!!!'
  end
end


class Ferrari < Vehicle
  attr_writer :model

  def initialize
    super 'Ferrari'
  end
end

vehicle = Vehicle.new('Train')
vehicle.start
vehicle.stop

obj = Ferrari.new
obj.model = gets('Enter a Ferrari model: ')
obj.start
obj.stop
