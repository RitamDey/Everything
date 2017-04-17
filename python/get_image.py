from urllib.request import urlopen


def get(url, file_name):
    obj = urlopen(url)
    image = open(file_name, "wb+")
    image.write(obj.read())
    image.close()
    

if __name__ == "__main__":
    get("https://scontent-sit4-1.cdninstagram.com/t51.2885-15/s750x750/sh0.08/e35/17932653_666050983578710_3935914691548676096_n.jpg", "image.jpeg")
