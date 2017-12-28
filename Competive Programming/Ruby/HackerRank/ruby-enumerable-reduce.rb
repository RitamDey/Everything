def sum_terms(n)
  # First we need to call reduce with a default value of 0 for
  # the right sum to be calculated
  return (1..n).reduce(0) { |res, n| res+((n**2)+1) }
end
