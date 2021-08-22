aka-viz
==============
## File Structure
```

```



python=3.8
https://chrome.google.com/webstore/detail/json-viewer-pro/eifflpmocdbdmepbjaopkkhbfmdgijcc?utm_source=chrome-ntp-icon


conda create --name akaswap python=3.8
conda activate akaswap

`
sudo vim /lib/systemd/system/test-py.service
`

```
[Unit]
Description=Test Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/home/alanhc/miniconda3/envs/akaswap/bin/python /home/alanhc/workspace/aka-viz/api-test.py

StandardInput=tty-force

[Install]
WantedBy=multi-user.target
```
[Unit]
Description=Dummy Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/alanhc/workspace/aka-viz/test.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target



sudo systemctl daemon-reload

sudo systemctl enable test-py.service