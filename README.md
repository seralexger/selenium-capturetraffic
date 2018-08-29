# Selenium CaptureTraffic
I have built a simple class in python to capture http and https traffic with Selenium and Browsermob proxy.

## Getting Started


I develop in mac, if you develop in linux or windows you will have to replace the geckodriver with the one appropriate for your system. You can download from (https://github.com/mozilla/geckodriver/releases).
You must have java installed to be able to use it from the command line.

All the necesary libraries for run the project are in the requirements.txt.

### Use of the class

There is a simple practical example in capture_example.py.

```
from capturetraffic import CaptureTraffic


sniffer = CaptureTraffic()
data = sniffer.capture_traffic(self, url, wait_time = 30, save = False, save_path = 'data/xhr_re.json')
```

### Data scheme example

Inside entries there is an array with the requestas and its responses.

```
{
    "log": {
        "version": "1.2",
        "creator": {
            "name": "BrowserMob Proxy",
            "version": "2.1.4",
            "comment": ""
        },
        "pages": [
            {
                "id": "Page 0",
                "startedDateTime": "2018-08-29T21:24:10.862+02:00",
                "title": "Page 0",
                "pageTimings": {
                    "comment": ""
                },
                "comment": ""
            }
        ],
        "entries": []
        
    }
}
```



