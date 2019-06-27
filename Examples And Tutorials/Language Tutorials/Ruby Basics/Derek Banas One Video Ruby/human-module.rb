module Human
    attr_accessor :name, :height, :weight

    def run
        $stdout.puts self.name + " runs"
    end
end
