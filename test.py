import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('./modules/Greetings')
import GreetingsLib as Greetings

from GreetingsLib \
    import  \
        printHello as hello, \
        printGoodbye as goodbye
    
hello()
goodbye()
dir(Greetings)



