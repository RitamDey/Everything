class Tree
    def initialize(data)
        @data = data
        @left = nil
        @right = nil
    end
    
    def append(data)
        if data > @data
            if @right != nil
                @right.append(data)
            else
                @right = Tree.new(data)
            end
        else
            if @left != nil
                @left.append(data)
            else
                @left = Tree.new(data)
            end
        end
    end
    
    def height()
        if @left == nil && @right == nil
            return 1
        end
        
        left = right = 0
        
        if @left != nil
            left = @left.height()
        end
        
        if @right != nil
            right = @right.height()
        end
        
        return [left, right].max() + 1
    end
end



len = gets().chomp().to_i()
data = gets().chomp().split().map { |i| i.to_i() }

tree = Tree.new(data[0])

for v in data[1,len]
    tree.append(v)
end

puts(tree.height())
