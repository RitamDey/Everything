from pycurl import Curl
from io import BytesIO


buffer = BytesIO()  # A buffer where cURL will write out data
curl_obj = Curl()  # The actual cURL object

# Setting some basic options for the underlying cURL
curl_obj.setopt(curl_obj.URL, 'http://httpbin.org/ip')
curl_obj.setopt(curl_obj.WRITEDATA, buffer)

# Perform operation and close
curl_obj.perform()
curl_obj.close()


# Decode the response and write it out to stdout
print(buffer.getvalue().decode('utf-8'))
