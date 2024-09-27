# import packages
from AddressGenerator import AddressGenerator
from Processor import Processor
from Strategies.FirstBillion import FirstBillion
from Strategies.LastBillion import LastBillion
from Strategies.NumberRepeat import NumberRepeat
from Strategies.Random import Random
from Strategies.AllBinary import AllBinary
from Strategies.MovingLeft import MovingLeft
from Strategies.Books import Books
from Strategies.NumberClimbing import NumberClimbing
from Strategies.WordCombos import WordCombos
from Logger import Logger
import sys
import argparse


# Get Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--nodeUrl', dest='nodeUrl', type=str, help='The URL of the node')
parser.add_argument('--strategyNumber', dest='strategyNumber', type=str, help='The URL of the node')
parser.add_argument('--count', dest='count', type=str, help='sets the counter')
# Assign Arguments To Variables
nodeURl = parser.parse_args().nodeUrl
strategyNumber = parser.parse_args().strategyNumber
count = parser.parse_args().count

if nodeURl is None:
    print("nodeUrl not provided, you can provide it using the --nodeUrl argument, using https://polygon-rpc.com as default")
    nodeURl = "https://polygon-rpc.com"

if strategyNumber is None:
    print("strategyNumber not provided, you can provide it using the --strategyNumber argument. using strategy number 0")
    strategyNumber = 0



# Variables
processNumber = int(strategyNumber)
strategy_classes = [
    FirstBillion,
    LastBillion,
    NumberRepeat,
    Random,
    AllBinary,
    MovingLeft,
    Books,
    NumberClimbing,
    WordCombos
]

chosenStrategy = strategy_classes[processNumber]()



if count is None:
    # set the counter from the log file
    logger = Logger(chosenStrategy, 0, "", 0)
    count = logger.getLastCounterBasedOnStrategyName(chosenStrategy.__class__.__name__)


# ask user to confirm  before continuing
print("Count: " + str(count))
print("strategyNumber: " + str(strategyNumber) + ", chosen strategy: " + str(chosenStrategy.__class__.__name__))
print("nodeURl: " + str(nodeURl))
print("Do you want to continue? (y/n)")
x = input()
if x != "y":
    sys.exit()


# Instantiate Processor class
# The processor will select a strategy and then run the process command
processor = Processor(chosenStrategy, nodeURl, count)
processor.run()
