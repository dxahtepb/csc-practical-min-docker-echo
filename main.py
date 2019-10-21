import socket
import logging


PORT = 65432
BUFF_SIZE = 2048


def send_message(conn: socket.socket, msg: str, data: bytes):
    conn.sendall(bytes(msg, encoding='UTF-8') + data)


def serve_client(conn: socket.socket, addr: str):
    with conn:
        while True:
            data = conn.recv(BUFF_SIZE)
            LOG.info('%s %s', addr, data.decode().strip())
            if not data:
                break
            send_message(conn, 'Ok: ', data)


def run_server(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        while True:
            s.listen(1)
            conn, addr = s.accept()
            serve_client(conn, addr[0])


def create_logger():
    log = logging.getLogger('echo_server')
    log.setLevel(logging.INFO)
    file_handler = logging.FileHandler('/var/log/server.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    log.addHandler(file_handler)
    return log


if __name__ == '__main__':
    LOG = create_logger()
    run_server(PORT)
