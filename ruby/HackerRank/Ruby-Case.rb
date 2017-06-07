def identify_class(obj)
    case obj.class.to_s
        when "Hacker", "Submission", "TestCase", "Contest"
            puts "It's a #{obj.class}!"
        else
            puts "It's an unknown model"
        end
end
