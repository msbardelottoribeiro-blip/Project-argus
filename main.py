import time
from scraper import ArgusScraper
from models import ContractModel

def run_argus_pipeline():
    print("=" * 60)
    print("         PROJECT ARGUS - GLOBAL AI AUDIT SYSTEM INITIALIZED        ")
    print("=" * 60)
    
    # Passo 1: Inicializa o robô que busca os dados na ONU
    print("\n[STEP 1] Starting Data Ingestion Pipeline...")
    scraper = ArgusScraper()
    time.sleep(1) # Simula o tempo de processamento
    
    # Passo 2: Simula os dados brutos capturados pelo robô (Caso Uzbequistão)
    print("\n[STEP 2] Simulating Data Extraction from UN Contract Platform...")
    raw_data = {
        "id": "UN-UZB-2026-999",
        "buyer": "UNOPS",
        "supplier": "Monega Enterprises Private Limited",
        "value": 2450000.00,
        "country": "Uzbekistan",
        "desc": "Medical equipment"
    }
    print(f"-> Found contract from supplier: {raw_data['supplier']}")
    time.sleep(1)

    # Passo 3: Passa os dados brutos pelo molde da IA para calcular o risco
    print("\n[STEP 3] Running Predictive Auditing & Risk Scoring Model...")
    contract_analysis = ContractModel(
        contract_id=raw_data["id"],
        buyer=raw_data["buyer"],
        supplier=raw_data["supplier"],
        value_usd=raw_data["value"],
        destination_country=raw_data["country"],
        description=raw_data["desc"]
    )
    
    # Executa a lógica de pontuação de fraudes
    risk_score = contract_analysis.calculate_basic_risk()
    time.sleep(1)
    
    # Passo 4: Exibe o veredito do relatório na tela
    print("\n[STEP 4] Analysis Complete. Reviewing Flags...")
    print("-" * 60)
    print(f"Contract ID: {contract_analysis.contract_id}")
    print(f"Supplier:    {contract_analysis.supplier}")
    print(f"Risk Score:  {risk_score}/10.0")
    print(f"Risk Flags:  {contract_analysis.risk_flags}")
    print("-" * 60)
    
    if risk_score >= 5.0:
        print("🚨 ALERT: High risk of funding leakage! Sending to Public Dashboard.")
    else:
        print("CLEAN: Low risk detected.")
    print("=" * 60)

if __name__ == "__main__":
    run_argus_pipeline()
