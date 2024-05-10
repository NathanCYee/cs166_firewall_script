# CS 166 Firewall Rules Updater

This is a python 3 script to update UFW and iptable rules to block IPs detected by Modern Honey Network (MHN). 

To extract data on the MHN server:
```bash
mongoexport --db mnemosyne --collection session > session.json
```

transfer the session.json file to the server which you want to update the firewall on.

To run:
```bash
sudo python3 get_ip.py /path/to/session.json
```