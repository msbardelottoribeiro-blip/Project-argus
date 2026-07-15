import urllib.request
import json

class UNOchaConnector:
    def __init__(self):
        # API real da ONU para rastrear fluxos de financiamento humanitário global
        self.api_url = "https://unocha.org"
        print("[Argus API] Connecting to UN OCHA Financial Tracking Service...")

    def get_realtime_flows(self):
        try:
            # Faz a requisição direta para os servidores da ONU
            req = urllib.request.Request(self.api_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
                # Filtra e exibe os dados brutos recebidos da ONU
                print("[Argus API] Data successfully retrieved from UN servers!")
                return json.dumps(data, indent=4)
        except Exception as e:
            return f"[Error] Could not connect to UN API: {str(e)}"

if __name__ == "__main__":
    connector = UNOchaConnector()
    # Imprime os primeiros fluxos de dinheiro registrados pela ONU no terminal
    print(connector.get_realtime_flows())
