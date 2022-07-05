import socket
from threading import Thread
import time
import termcolor


def main(thread_count, host, port_range):

    # Get program started time.
    start_time = time.perf_counter()

    # Store open ports.
    open_ports = []

    # The main program.
    def scanner():

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # If you need to scan all ports this is the option you need.
        if port_range == 'ALL':

            for i in range(65536):

                address = host, i
                result = server.connect_ex(address)

                if result == 0 and i not in open_ports:
                    open_ports.append(i)

        else:

            for i in range(port_range):

                address = host, i
                result = server.connect_ex(address)

                if result == 0 and i not in open_ports:
                    open_ports.append(i)

        server.close()

    # Store threads.
    count = []

    for i in range(thread_count):

        thread = Thread(target=scanner)
        count.append(thread)
        thread.daemon = True
        thread.start()

    for i in count:

        i.join()

    end_time = time.perf_counter()

    for i in open_ports:

        print(termcolor.colored(f'\n{i} port is open.', 'blue'))

    if open_ports == []:

        print(termcolor.colored('\nNo any open port discovered.', 'blue'))

    print(termcolor.colored(
        f'\nTotal time used : {end_time - start_time}', 'yellow'))
