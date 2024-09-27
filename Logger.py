from datetime import datetime

class Logger:
    # constructor
    def __init__(self, strategy, counter = 0, address = "", balance = 0):
        print("Logger instantiated")
        self.strategy = strategy
        self.counter = counter
        self.address = address
        self.balance = balance

    # log the private key, address, and balance
    # print the private key, address, and balance
    def logPrivateKey(self, privateKey):
       with open("log/" + str(self.strategy.__class__.__name__) + ".txt", "a") as f:
            # log counter and strategy name
            f.write("Date: " + str(datetime.now()) + "\n")
            f.write("Counter: " + str(self.counter) + "\n") 
            f.write("address key: " + str(self.address) + "\n")
            f.write("private key: " + str(privateKey) + "\n")
            f.write("balance: " + str(self.balance) + "\n")
            print("*******************************************")
            print("Date: " + str(datetime.now()))
            print("Counter: " + str(self.counter))
            print("balance found")
            print("address key: " + str(self.address))
            print("private key: " + str(privateKey))
            print("balance: " + str(self.balance))
            print("*******************************************")


    # adds the latest counter to the log/counter.txt file
    def logCounter(self):
        # log counter into log/counters file by date. ex. log/counters/2020-01-01.txt
        with open("log/counter.txt", "a") as f:
            # Get today's date
            today_date = datetime.today().strftime('%Y-%m-%d')
            
            # Log counter into counter.txt file in log folder with strategy name
            strategy_name = str(self.strategy.__class__.__name__)
            log_path = "counter/" + strategy_name + ".txt"
            new_line = f"{today_date}-{strategy_name}-Counter: {self.counter}\n"
            
            # Read the existing content
            try:
                with open(log_path, "r") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                lines = []
            
            # Check if strategy counter exists and update it
            updated = False
            for i, line in enumerate(lines):
                if line.startswith(f"{today_date}-{strategy_name}"):
                    lines[i] = new_line
                    updated = True
                    break
            
            # If the strategy counter does not exist, append a new line
            if not updated:
                lines.append(new_line)
            
            # Write the updated content back to the file
            with open(log_path, "w") as file:
                file.writelines(lines)


    def getLastCounterBasedOnStrategyName(self, strategy_name):
        # set the log path, and if the file does not exist, create it
        log_path = "counter/" + strategy_name + ".txt"
        try:
            with open(log_path, "x") as f:
                pass
        except FileExistsError:
            pass
        
        # get the last date for the strategy name and save it into a lastDate variable
        with open(log_path, "r") as f:
            lines = f.readlines()
            lastDate = None
            for line in lines:
                if strategy_name in line:
                    lastDate = line.split("-")[0]
                    break  # Assuming you want the last occurrence, you can stop at the first match

        # Use lastDate and strategy name to get the last counter
        if lastDate is not None:  # Check if lastDate has been set
            with open(log_path, "r") as f:
                lines = f.readlines()
                lastCounter = 0
                for line in lines:
                    if lastDate in line and strategy_name in line:
                        lastCounter = int(line.split(":")[1])
        else:
            # Handle the case where lastDate was not found
            print(f"No entries found for strategy {strategy_name}")
            return 0  # or any other default or error handling mechanism

        return lastCounter
