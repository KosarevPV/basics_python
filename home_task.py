import sys

import utils


for el in sys.argv[1:]:
    print(utils.currency_rates(el))
