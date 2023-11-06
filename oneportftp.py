#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script Name: oneportftp.py
Description: OnePortFTP is a simple FTP server designed for use with a single passive port.
Author: 9xh4kv
Author Email: 9xh4kv@gmail.com
"""
import argparse
import sys
import warnings

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def start_server(user, password, port, passive_port):
    banner ="""
 _       _  _       ___     _ ___ _ 
/ \ ._  |_ |_) _  ._ |     |_  | |_)
\_/ | | |_ |  (_) |  |     |   | |  
"""
    warnings.filterwarnings("ignore", category=RuntimeWarning, module="pyftpdlib.authorizers")
    authorizer = DummyAuthorizer()

    if user and password:
        authorizer.add_user(user, password, ".", perm="elradfmw")
        print(banner)
        print(f"Username: {user} \nPassword: {password}")
    elif user and not password:
        print(f"Error: Please set a password for '{user}' user or remove flag to enable anonymous login.\n\n")
        parser.print_help()
        sys.exit(1)
    else:
        user_response = input("No user account specified.\nEnable anonymous login with write/read permissions? [Y/N]")
        if user_response.lower() == "y":
            print(banner)
            authorizer.add_anonymous("/", perm="elradfmw") # remove anonymous write permissions here
            print("No user account set. \n\033[91mWARNING:\033[97m \033[4mAnonymous login\033[0m with \033[91mwrite/read\033[97m permission is \033[91menabled\033[97m.")
        else:
            print("Server not started.\n\n")
            parser.print_help()
            sys.exit(0)
    print("\033[91mWARNING:\033[97m This is a development server. Do \033[91mNOT\033[97m use it in a production deployment.")
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = (passive_port, passive_port)

    # Create and start the FTP server
    server = FTPServer(("0.0.0.0", port), handler)
    try:
        server.serve_forever()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start an FTP server with an optional passive port.")
    parser.add_argument("-u", "--user", type=str, default=None, help="User for FTP server (default: None)")
    parser.add_argument("-p", "--password", type=str, default=None, help="Password for FTP server (default: None)")
    parser.add_argument("-l", "--port", type=int, default=21, help="Listening port for FTP server (default: 21)")
    parser.add_argument("-P", "--passive-port", type=int, default=1620, help="Passive port for FTP server (default: 1620)")
    args = parser.parse_args()

    start_server(args.user, args.password, args.port, args.passive_port)

