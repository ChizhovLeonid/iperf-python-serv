# iperf-python-serv
Run iperf server when get POST json
# command curl to start
`curl -X POST -d "{\"loginauth\":\"secretkey\", \"command\":\"start\"}" -H "Content-Type:application/json" 0.0.0.0:5000/iperf-command-start`
# command curl to stop
`curl -X POST -d "{\"loginauth\":\"secretkey\", \"command\":\"stop\"}" -H "Content-Type:application/json" 0.0.0.0:5000/iperf-command-stop`
