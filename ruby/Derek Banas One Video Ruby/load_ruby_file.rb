=begin

The `loads` statment is used to run other ruby scripts whithin a running ruby script.
One thing to note is that any code under `if __FILE__ == $0` will not run.

=end

load "add.rb"
