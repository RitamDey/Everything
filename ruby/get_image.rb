require 'open-uri'  # Import the open-uri module from the standard lib


=begin
# Original code from StackOverflow: http://stackoverflow.com/questions/1074309/how-do-i-download-a-picture-using-ruby
	open(url) { |f|
		File.open(file_name, "wb+") do |file|
			file.puts f.read
		end
	}
=end

def get_pic(url, file_name)
	# Use the open method from the library and get the info
	# The open method takes url as argument and a optional executable code block
	# In this block we first use the File class's open method to open a image file fo writing
	# The open method need the file name and the file's opening permissions
	# We can also optionally pass a proc to the open method

	
	f = open(url)  # Opening the url and gets its contains
	fout = File.open(file_name, 'wb+')  # Open a new file with the file_name
	fout.puts f.read  # Put everything to the file after reading the retrived contents
	fout.close
end


if __FILE__ == $0
	get_pic("https://scontent-sit4-1.cdninstagram.com/t51.2885-15/s750x750/sh0.08/e35/17932653_666050983578710_3935914691548676096_n.jpg", "image.jpeg")
end
