import os
import subprocess
import threading
import time
import pyudev
import requests

class rede:
    @staticmethod
    def check_internet_connection():
        try:
            response = requests.get("http://www.google.com", timeout=5)
            if response.status_code == 200:
                print("Conexão com a Internet está ativa.")
            else:
                print("Sem conexão com a Internet.")
        except requests.ConnectionError:
            print("Sem conexão com a Internet.")

    @staticmethod
    def check_proxy():
        '''
        Verifica as variáveis de ambiente se tem um http_proxy, e faz uma verificação de cabeçalhos HTTP para proxies transparentes.
        '''
        proxy = os.environ.get('HTTP_PROXY') or os.environ.get('http_proxy')
        if proxy:
            print(f"Proxy encontrado nas variaveis de ambiente: {proxy}")
        else:
            print("Nenhum proxy encontrado nas variaveis de ambiente.")

        # Verificar proxies transparentes por cabeçalhos HTTP
        try:
            response = requests.get("http://www.google.com", timeout=5)
            headers = response.headers
            if 'Via' in headers or 'X-Forwarded-For' in headers:
                print(f"Proxy transparente detectado: {headers}")
            else:
                print("Nenhum proxy transparente detectado pelos cabeçalhos HTTP.")
        except requests.ConnectionError:
            print("Sem conexão com a Internet.")

    @staticmethod
    def get_public_ip():
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            return response.text
        except requests.ConnectionError:
            print("Não foi possível obter o IP público.")
            return None

    @staticmethod
    def compare_ip_addresses():
        public_ip = rede.get_public_ip()
        if public_ip:
            print(f"IP público: {public_ip}")
            try:
                local_ip = subprocess.check_output(['hostname', '-I']).decode().strip()
                print(f"IP local: {local_ip}")
                if public_ip != local_ip:
                    print("Possível proxy transparente detectado: o IP público difere do IP local.")
                else:
                    print("Nenhum proxy transparente detectado: o IP público corresponde ao IP local.")
            except subprocess.CalledProcessError:
                print("Não foi possível obter o IP local.")

# TLS monitor e o cliente
class tls:
    @staticmethod
    def testar():
        try:
            result = subprocess.run('netstat -ano | find "4096"', capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                subprocess.run(["net", "start", "Tls Monitor"])
                subprocess.run(["net", "start", "Tls cli"], capture_output=False, shell=False)
        except subprocess.CalledProcessError as e:
            print(e.stderr)
        threading.Timer(200, tls.testar).start()

class pin_pad:
    @staticmethod
    def list_usb_devices():
        context = pyudev.Context()
        for device in context.list_devices(subsystem='usb', DEVTYPE='usb_device'):
            vendor_id = device.attributes.get('idVendor')
            product_id = device.attributes.get('idProduct')
            manufacturer = device.attributes.get('manufacturer')
            product = device.attributes.get('product')

            if vendor_id and product_id:
                vendor_id = vendor_id.decode() if vendor_id else "Unknown"
                product_id = product_id.decode() if product_id else "Unknown"
                manufacturer = manufacturer.decode() if manufacturer else "Unknown"
                product = product.decode() if product else "Unknown"

                if manufacturer == "GERTEC":
                    print("Localizado um dispositivo GERTEC")
                    
class dll:
    pass

if __name__ == "__main__":
    # Chamar a função pela primeira vez
    pin_pad.list_usb_devices()
    rede.check_internet_connection()
    rede.check_proxy()
    rede.compare_ip_addresses()
