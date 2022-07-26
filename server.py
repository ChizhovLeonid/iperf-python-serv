#!/usr/bin/env python3
import json
from pickle import NONE
from flask import Flask, request, jsonify 
import subprocess

app = Flask('iperf3-server')

@app.route('/', methods=['GET'])
def fuck():
    return ''

@app.route('/iperf-command-start', methods=['POST'])
def iperf_command_start():
    request_data = request.get_json()

    loginauth = 'secretkey' #enter here you secret combination, it need to security, also need edit curl post command
    command = 'start' #its a alias command, need too

    if request_data:
        if (('loginauth' in request_data) and ('command' in request_data)):
            if ((loginauth == request_data['loginauth']) and (command == request_data['command'])):
                cmd = "iperf3 -s -D" #command to run
                subprocess.run(cmd, shell=True)
    return NONE

@app.route('/iperf-command-stop', methods=['POST'])
def iperf_command_stop():
    request_data = request.get_json()

    loginauth = 'secretkey' #enter here you secret combination, it need to security, also need edit curl post command
    command = 'stop' #its a alias command, need too

    if request_data:
        if (('loginauth' in request_data) and ('command' in request_data)):
            if ((loginauth == request_data['loginauth']) and (command == request_data['command'])):
                cmd = "pkill iperf3" #command to run
                subprocess.run(cmd, shell=True)
    return NONE

app.run(host='0.0.0.0', port='5000') #enter you ip addres and port
