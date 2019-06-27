class Invoice

    # Class method startes with self
    def self.print_out(num)
        return "Printed out Invoice #{num}"
    end

    def convert(ftype)
        return "Coverted to #{ftype.upcase!}"
    end
end


$stdout.puts Invoice.print_out(95123)

x = Invoice.new

$stdout.puts x.convert("pdf")
