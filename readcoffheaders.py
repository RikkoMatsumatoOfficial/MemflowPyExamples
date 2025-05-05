from memflow import *

class COFFHeader(Structure):
    _fields_ = [
        ("_pad0x0", c_byte * 6),
        ("sections", c_short),
        ("timestamp", c_uint32),
    ]

def Main():
    inventory = Inventory()
    os = inventory.create_os("native")
    process = os.process_from_name("cmd.exe")
    module = process.module_by_name("cmd.exe")
    header = process.read(module.base + 0x40, COFFHeader)
    print(header)

if __name__ == "__main__":
    Main()