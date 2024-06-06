import os
import subprocess
import threading
import time
import usb.core
import pyudev

#tls monitor e o cliente
class tls:
    @staticmethod
    def testar():
        try:
            result = subprocess.run('netstat -ano | find "4096"', capture_output=True, 
                                        text=True, shell=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                
                subprocess.run([
                    "net",
                    "start",
                    "Tls Monitor"]
                )
                subprocess.run([
                    "net",
                    "start",
                    "Tls cli"
                ],
                capture_output=False,
                shell=False
                )
        except subprocess.CalledProcessError as e:
            print(e.stderr)
        threading.Timer(200, tls.testar).start()

class pin_pad:
    def list_usb_devices():
        context = pyudev.Context()

        print("Dispositivos USB encontrados:")
        for device in context.list_devices(subsystem='usb', DEVTYPE='usb_device'):
            vendor_id = device.attributes.get('idVendor')
            product_id = device.attributes.get('idProduct')
            product = device.attributes.get('product')
            manufacturer = device.attributes.get('manufacturer')
            bus_number = device.get('BUSNUM')
            device_number = device.get('DEVNUM')

            if vendor_id and product_id:
                print(f"Bus {bus_number:03} Device {device_number:03}: ID {vendor_id.decode()}:{product_id.decode()} {manufacturer.decode() if manufacturer else ''} {product.decode() if product else ''}")

class dll:
    pass

if __name__ == "__main__":
    # Chamar a função pela primeira vez
    pin_pad.list_usb_devices()