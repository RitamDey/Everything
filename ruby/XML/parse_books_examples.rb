require 'nokogiri'


doc = Nokogiri.XML(File.read('example.xml'))

titles = doc.search('title')
authors = doc.search('author')
prices = doc.search('price')

for item in titles.zip(authors, prices)
    puts("#{item[0].content} by #{item[1].content} costs #{item[2].content}")
end
