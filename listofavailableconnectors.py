import memflow.memflow as memflow
import  os

def Main():
    inventory = memflow.Inventory()
    print(inventory.available_connectors())

if __name__ == "__main__":
    Main()