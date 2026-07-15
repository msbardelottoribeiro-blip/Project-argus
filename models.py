from datetime import datetime

class ContractModel:
    def __init__(self, contract_id, buyer, supplier, value_usd, destination_country, description):
        self.contract_id = contract_id
        self.buyer = buyer                          # Ex: UNOPS, UNICEF
        self.supplier = supplier                    # Ex: Monega Enterprises
        self.value_usd = float(value_usd)           # Valor em dólares
        self.destination_country = destination_country # País de destino
        self.description = description              # O que foi comprado
        self.processed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.risk_score = 0.0                       # Termômetro de risco da IA (0 a 10)
        self.risk_flags = []                        # Motivos do alerta vermelho

    def calculate_basic_risk(self):
        """
        Regras iniciais automáticas que simulam o olho do auditor.
        Isso serve de guia para os desenvolvedores implementarem Machine Learning.
        """
        # Alerta 1: Contratos sem descrição clara em zonas de crise
        if len(self.description) < 15:
            self.risk_score += 3.0
            self.risk_flags.append("SHORT_DESCRIPTION_HIGH_RISK")

        # Alerta 2: Valores muito redondos ou suspeitosamente altos
        if self.value_usd > 1000000.00:
            self.risk_score += 2.5
            self.risk_flags.append("HIGH_VALUE_TRANSACTION")
            
        return self.risk_score

    def to_json(self):
        return {
            "contract_id": self.contract_id,
            "buyer": self.buyer,
            "supplier": self.supplier,
            "value_usd": self.value_usd,
            "destination_country": self.destination_country,
            "processed_at": self.processed_at,
            "risk_score": self.risk_score,
            "flags": self.risk_flags
        }

if __name__ == "__main__":
    # Testando o modelo com o caso do Uzbequistão que você encontrou!
    test_contract = ContractModel(
        contract_id="UN-UZB-2026-001",
        buyer="UNOPS",
        supplier="Monega Enterprises Private Limited",
        value_usd=1250000.00, # Exemplo de valor alto
        destination_country="Uzbekistan",
        description="Medical supply" # Descrição curta suspeita
    )
    
    test_contract.calculate_basic_risk()
    print("[Argus Model Test] Contract Processed Successfully:")
    print(test_contract.to_json())
