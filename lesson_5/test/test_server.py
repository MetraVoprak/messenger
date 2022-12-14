import sys
import os
from socket import socket

sys.path.append(os.path.join(os.getcwd(), '..'))
import unittest
import lesson_5.chat.chat as chat


class TestServer(unittest.TestCase):
    def setUp(self):
        self.s = chat.get_server_socket('localhost', 7777)

    def tearDown(self):
        self.s.close()

    def test_server_socket_is_socket(self):
        self.assertIsInstance(self.s, socket)

    def test_server_socket_addr(self):
        self.assertEqual(self.s.getsockname(), ('127.0.0.1', 7777))


if __name__ == '__main__':
    unittest.main()
