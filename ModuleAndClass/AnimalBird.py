# calling Animal & Bird functions from Animal & Bird module

# Approach 1
import Animal
import Bird

# calling Animal module  functions
Animal.fly()
Animal.color()

# calling Bird module  functions
Bird.fly()
Bird.color()

# Approach 2
from Animal import *
from Bird import *  # latest import called hence Bird module function called so its better to use first Approach 1

fly()
color()

# Approach 3
from Bird import *
from Animal import *  # latest import called hence Animal module functions called so its better to use first Approach 1

fly()
color()

# Approach 4

from Animal import *   # import separately Animal module
fly()
color()


from Bird import *   # import separately Bird module
fly()
color()