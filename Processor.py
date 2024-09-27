from BalanceChecker import BalanceChecker
from Logger import Logger
import sys
import time

class Processor:
    # constructor
    def __init__(self, strategy, nodeURl, counter):
        self.strategy = strategy
        #  check if strategy has attribute counter
        self.counter = int(counter)
        
        self.BalanceChecker = BalanceChecker(nodeURl)
        print("Processor instantiated")
        print("Strategies: " + str(strategy))
        print("Counter: " + str(counter))
        print("Node URL: " + str(nodeURl))
        # check to see if network is working
        self.testNetworkForBalance()

    def run(self):
        while True == True:
            #  get array of private keys
            privateKeyArray = self.strategy.process(self.counter)
            #  increase counter
            self.counter = self.counter + 1
            # print counter and test network every 1000 iterations
            if self.counter % 1000 == 0:
                logger = Logger(self.strategy, self.counter, "", balance = 0)
                logger.logCounter()
                self.testNetworkForBalance()
                print("Counter: " + str(self.counter))
                    
            #  check if counter should be reset
            self.resetCounterCheck()
            if self.resetCounterCheck() == True:
                print("Counter has reached its upper limit - exiting")
                sys.exit()
                exit()

            # check if all keys have a balance
            for privateKey in privateKeyArray:
                # print("Private Key: " + str(privateKey))
                # keys are the private keys
                # use the AddressGenerator to generate the public key and address
                address = self.strategy.AddressGenerator.generate_address_from_private_key(privateKey)
                # # check the balance of the address
                balance = self.BalanceChecker.checkBalance(address)
                # print("PrivateKey: " + str(privateKey))
                # print("Address: " + str(address))
                # print("Balance: " + str(balance))
                # if the balance is greater than 0, print the address, private key, and balance in log/log.txt
                # the name of the log must be the name of the strategy
                if balance > 0:
                    logger = Logger(self.strategy, self.counter, address, balance)
                    logger.logPrivateKey(privateKey)
                        
    def resetCounterCheck(self):
        resetCounter = self.strategy.resetProcess(self.counter)
        if resetCounter == True:
            #exit instead of resetting the counter.
            sys.exit()
        else:
            return False

    def testNetworkForBalance(self):
        balance = self.BalanceChecker.checkBalance("0x3f17f1962B36e491b30A40b2405849e597Ba5FB5")
        if balance > 741678397256152882:
            print("Network test passed - Network is working")
            return True
        else:
            #sleep for 5 seconds and this try this function again   
            print("Network is not working - trying again in 5 seconds")
            time.sleep(5)
            self.testNetworkForBalance()


        
           

        
            
