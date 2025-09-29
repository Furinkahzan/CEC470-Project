

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
}

# ============================
# MAIN MENU
# ============================
# 1) Configure cache parameters
#    - Change CacheSize, BlockSize, Associativity, etc.
#    - Store updated values in SimConfig
#
# 2) Choose simulation type  (go to Simulation Type Submenu)
#
# 3) Load memory trace / access pattern
#    - Choose synthetic (sequential, random, stride)
#    - Or load from a trace file
#
# 4) Run simulation
#    - Use current SimConfig + chosen simulation type + memory trace
#    - Call the cache simulator logic
#
# 5) View statistics
#    - Print results (total accesses, hits, misses, hit rate, miss rate)
#    - Optionally save to file
#
# 6) Exit program
#
# ============================
# SIMULATION TYPE SUBMENU
# ============================
# 1) Direct-Mapped
#    - Sets Associativity = 1 automatically
#
# 2) Fully Associative
#    - Sets Number of Sets = 1
#    - Associativity = total blocks
#
# 3) Set-Associative
#    - User chooses N-way (e.g., 2-way, 4-way)
#
# 4) LRU Policy
#    - Set ReplacementPolicy = "LRU"
#
# 5) FIFO Policy
#    - Set ReplacementPolicy = "FIFO"
#
# 6) Random Policy
#    - Set ReplacementPolicy = "Random"
#
# 7) Back to Main Menu
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
        
        case 1:
        case 2:
        case 3:
    
        case 4:
        case 5:
        case 6:
            exit()
        case _:
            print("Invalid option")
    
    


def selectionMenu():
    
    print("What would you like to simulate?")
    print("1)Direct-Mapped")
    print("2)Fully Associative")
    print("3)LRU")
    print("4)FIFO")
    print("5)Set-Associative mapping")
    print("6)exit")
    choice = input ("enter your choice:")
    return choice



def simulator():
    






main();