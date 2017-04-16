import requests


# Here we use get the image from the url and exposes the raw data as seen by the socket
obj = requests.get('http://www.funroundup.com/wp-content/uploads/2015/12/Poonam-Pandey-hot-and-sexy-wallpapers-in-bikini-fun-roundup3.jpg', stream=True)


# Open  a binary file for writing
with open('image.jpg', 'wb+') as fd:
    """
    Using Response.iter_content will handle a lot of what you would otherwise have to handle when using Response.raw directly. 
    When streaming a download, the above is the preferred and recommended way to retrieve the content. 
    Note that chunk_size can be freely adjusted to a number that may better fit your use cases.
    """
    for chunk in obj.iter_content(chunk_size=256):
        fd.write(chunk)

