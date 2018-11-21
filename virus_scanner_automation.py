it's uncomplited my bed is calling me(: good night, and tomorrow insh'allah.
note some of this modules will be used in the future.

import queue
import schedule
import json
import requests
import time
import os


class small_App:
    url = "https://www.virustotal.com/vtapi/v2/file/scan"
    parms = {"apikey": "24bf827e6c628091f13d7c752ab819a4e17fa5f690a576667aae49c3ebb34583"}

    def __init__(self, dir):
        self.dir = dir

    def scan(self):
        counter = 0
        files = []
        for root, dirs, files_itter in os.walk(self.dir):
            for filename in files_itter:
                if int(os.path.getsize(filename)) < 20884868:
                    files.append(filename)
                    if len(files) > 3:
                        break
        while counter < len(files):
            files_carry = {"file": (files[counter], open(files[counter], "rb"))}
            response = requests.post(small_App.url, files=files_carry, params=small_App.parms)
            analayze = response.json()
            resource = analayze["resource"]
            parms_scan {small_App.parms["apikey"], "resource": resource}
            response_analyze = requests.get(url, params=parms_scan)
            print(analayze)
            print(response.json())
            with open("data_file.txt" + str(counter), "w") as response_file:
                json.dump(response_analyze.json(), response_file)
                response_file.close()
            counter += 1


apps = small_App("/home/aero/Music")

apps.scan()
