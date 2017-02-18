from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer


# Instantiate a dummy authorizer for managing virtual hosts
authorizer = DummyAuthorizer()

# Define a new user having r/w permission
authorizer.add_user('stux', 'thisistux', input("Enter the absolute path:"), perm='elradfmwM')

# Instantiate FTP handler class
handler = FTPHandler
handler.authorizer = authorizer

# Define a customized banner
handler.banner = "FTP server running..."

# Instantiate FTP server class and listen on 0.0.0.0:2121
address = ('0.0.0.0', '2121')
server = FTPServer(address, handler)

# Set connection limits
server.max_cons = 3

# Start FTP Server
server.serve_forever()

