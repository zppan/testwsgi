#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import sys
import httplib
import urllib
import socket
import requests
import time
import json
import logging

logging.basicConfig(level=logging.INFO)

def application(environ, start_response):
    status = "200 OK"
    output = "hello zppan"

    response_headers = [("Content-type", "text/plain"),
            ("Content-Length", str(len(output)))]
    start_response(status, respone_headers)

    return [output]
