
import collections
# 4. Cache Access Logic
# - Function to process one memory access:
#     1. Decode address into tag and index
#     2. Check the set for a block with matching tag
#         - If found → HIT (update replacement metadata)
#         - If not found → MISS
#             - If empty block available → insert new block
#             - Else → call replacement policy to evict a block, then insert new one

# 5. Replacement Policies
# - LRU: evict least recently used block
# - FIFO: evict the oldest inserted block
# - Random: pick a random block

# 6. Statistics
# - Track total accesses
# - Track total hits
# - Track total misses
# - Compute hit rate and miss rate
# - (Optional) Classify compulsory vs conflict vs capacity misses

# 7. Memory Access Engine
# - Generate memory address sequences:
#     - Sequential pattern
#     - Stride pattern
#     - Random pattern
#     - (Optional) Load from a trace file

# 8. Experiment Runner
# - Run simulations with different cache parameters
# - Collect results (hit/miss rates)
# - Print or plot results in tables/graphs

# 9. Validation / Test Cases
# - Single-block cache test
# - Conflict miss test (addresses map to same index)
# - LRU correctness test
# - Compulsory miss detection test

Simconfig = {
# 1. Configuration / Parameters

     "CacheSize":30,#total syze of bytes
     "BlockSize":30,#bytes per block
     "SetNum":3,#number of sets
     "associativity":20,#blocks per set
     "Replacementpolicy":"LRU",
     "AddressWidth" :32,#Total address bites
     "random_seed":0#integer for reproducibility
     
}

class DataStructure:{
# 2. Data Structures
# - Represent cache as a list of sets
# - Each set contains blocks
# - Each block contains:
#     - valid bit
#     - tag
#     - metadata (timestamp or insertion order for replacement)
}


def adressAnalyze():{
# 3. Address Breakdown
# - Function to split an address into:
#     - tag
#     - index
#     - offset (optional, if modeling block size)
   def __init__(self,tag:float, index:float, offset:float):
        self.tag = tag
        self.index = index
        self.offset = offset

    @property
    def tag(self)-> float:
        return self.tag
            
    @property
    def index(self)-> float:
        return self.tag    
    
    @property
    def offset(self)-> float:
        return self.tag       
}


#

# ============================
# FLOW EXAMPLE
# ============================
# Main Menu -> Option 2 (Choose simulation type)
#    -> Simulation Type Submenu
#        -> User selects "Direct-Map

def main():
    
    choice = selectionMenu()
    match choice:
        
        case 1:## 1) Configure cache parameters
               #    - Change CacheSize, BlockSize, Associativity, etc.
               #    - Store updated values in SimConfig
            
        case 2:# 2) Choose simulation type  (go to Simulation Type Submenu)
            simulation_sub_menu()

        case 3:# 3) Load memory trace / access pattern
               #    - Choose synthetic (sequential, random, stride)
               #    - Or load from a trace file
    
        case 4:# 4) Run simulation
               #    - Use current SimConfig + chosen simulation type + memory trace
               #    - Call the cache simulator logic
               run_simulation()


        case 5:# 5) View statistics
               #    - Print results (total accesses, hits, misses, hit rate, miss rate)
               #    - Optionally save to file


        case 6:# 6) Exit program
            exit()

        case _:
            print("Invalid option")
    
    


def selectionMenu():
# ============================
# MAIN MENU
# ============================
    print("What would you like to do?")
    print("1)Configure cache parameters")
    print("2)Choose simulation type")
    print("3)Load memory trace")
    print("4)Run simulation")
    print("5)View statistics")
    print("6)exit")
    choice = input ("enter your choice:")
    return choice

def run_simulation_menu():
        choice = run_simulation_sub_menu()
    match choice:
        
        case 1:## 1) Direct Mapped
            
        case 2:# 2)Fuly associative
        case 3:# 3)set-associative
    
        case 4:# 4) LRU


        case 5:# 5) FIFO

        case 6:# 6) Random Policy
          
        case 7:# go back to main menu
            
        case _:
            print("Invalid option")
    
def run_simulation_sub_menu():
    # ============================
# SIMULATION TYPE SUBMENU
# ============================
# 1) Direct-Mapped
#    - Sets Associativity = 1 automatically
#
# 2) Fully Associative
#    - Sets Number of Sets = 1
#    - Associativity = total blocks
    print("What type of simulation would you like to run?")
    print("1)Direct mapped")
    print("2)Fully associative")
    print("3)Set-Assosiative")
    print("4)LRU")
    print("5)FIFO")
    print("6)Random Policy")
    print("7)Go back to the main menu")
    choice= input("enter choice:")
    return choice

def simulator():
    