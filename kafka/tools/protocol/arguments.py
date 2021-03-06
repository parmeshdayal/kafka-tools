# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import argparse


def set_up_arguments():
    # Configure basic arguments
    aparser = argparse.ArgumentParser(prog='kafka-protocol', description='CLI tool for sending Kafka protocol requests to a broker')
    aparser.add_argument('-b', '--broker', help='Kafka broker hostname to connect to', default='localhost')
    aparser.add_argument('-p', '--port', help="Port number on the Kafka broker to connect to", type=int, default=9092)
    aparser.add_argument('-t', '--tls', help="Enable TLS for the broker connection", action='store_true')

    # Parse the args that were passed
    args = aparser.parse_args()
    return args
