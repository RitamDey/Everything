from make_client import make_client
from tweepy import Stream
from tweepy.streaming import StreamListener
from sys import argv


class PrintStream(StreamListener):
    def on_status(self, status):
        # Hack Alert:
        # Twitter usually contains emonjis are utf-16 encoded and have surrogates
        # To bypass this encode the string first by ('utf-16', 'surrogatepass'),
        # then decode it using 'utf-16' codec
        # Found here:
        # http://stackoverflow.com/questions/38147259/how-to-work-with-surrogate-pairs-in-python
        print(str(status.user.name.encode('utf-16', 'surrogatepass').decode('utf-16')))
        print(str(status.text.encode('utf-16', 'surrogatepass').decode('utf-16')))


client = make_client(auth_client=True)
twitter_stream = Stream(auth=client, listener=PrintStream())
twitter_stream.filter(track=["trolls", "comrades" , "communists" ,"cpim"], async=True)

