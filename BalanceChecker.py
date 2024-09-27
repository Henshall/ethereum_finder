# create a class called BalanceChecker to check the balance of an address

import requests
import json
import time

class BalanceChecker:
    def __init__(self, nodeURl):
        print("BalanceChecker instantiated")
        if nodeURl is None:
            self.nodeURl = "https://polygon-rpc.com"
        else:
            self.nodeURl = nodeURl

    def checkBalance(self, address):
        # check balance of address using polygon-rpc api
        # curl -X POST https://polygon-rpc.com -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x02DFB085289c541dcb36090E88bdA30e4727A61D", "latest"],"id":1}'
        url = self.nodeURl

        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "jsonrpc":"2.0",
            "method":"eth_getBalance",
            "params":[str(address), "latest"],
            "id":1
        }
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            # response = {'jsonrpc': '2.0', 'id': 1, 'result': '0x0'}
            # return result
            hexBalance = response.json().get('result')
            # convert hex to int
            # try to convert hex to int
            # print(response.json())
            balance = int(hexBalance, 16)
        except:
            print("balance not working - trying again in 5 seconds")
            time.sleep(5)
            balance = self.checkBalance(address)

        # print("Balance: " + str(balance))
        return balance
        

        
