import optparse
import os
import socket
import time


def parse_args() :
    usage = """
    usage: %prog [options] poetry-file
    This is the Slow Poetry Server, blocking edition.
    Run it like this:
    python slowpoetry.py <path-to-poetry-file>
    If you are in the base directory of the twisted-intro package,
    you could run it like this:
    python blocking-server/slowpoetry.py poetry/ecstasy.txt
    to serve up John Donne's Ecstasy, which I know you want to do.
    """
    parser = optparse.OptionParser(usage)

    help_port = "The port to listen on. Default to a random avaliable"
    parser.add_option('--port', type='int', help=help_port)

    help_iface = "The interface to listen on. Default is localhost."
    parser.add_option('--iface', help=help_iface, default='localhost')

    help_delay = "The number of seconds between sending bytes."
    parser.add_option('--delay', type='float', help=help_delay, default=.7)

    help_bytes = "The number of bytes to send at a time."
    parser.add_option('--num-bytes', type='int', help=help_bytes, default=10)

    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error('Provide exactly one poetry file.')

    poetry_file = args[0]

    if not os.path.exists(args[0]):
        parser.error("No such file: %s" %poetry_file)

    return options, poetry_file


def send_poetry(sock, poetry_file, num_bytes, delay):
    """ Send some poetry slowly down the socket """
    
    with open(poetry_file) as inputf:
        while True:
            bytes_to_sent = inputf.read(num_bytes)

            if not bytes_to_sent:
                sock.close()
                return

            print("Sending %d bytes" %len(bytes_to_sent))

            try:
                sock.sendall(bytes_to_sent.encode('utf-8'))  # this is a blocking call
            except socket.error:
                sock.close()
                return
            
            time.sleep(delay)


def serve(listen_socket, poetry_file, num_bytes, delay):
    while True:
        sock, addr = listen_socket.accept()

        print("Somebody at %s wants poetry!" %(addr,))

        send_poetry(sock, poetry_file, num_bytes, delay)


def main():
    options, poetry_file = parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((options.iface, options.port or 0))

    sock.listen(5)

    print("Serving %s on port %s" %(poetry_file, sock.getsockname()[1]))

    serve(sock, poetry_file, options.num_bytes, options.delay)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nClosing...")

