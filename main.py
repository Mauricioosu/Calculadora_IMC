"""
Calculadora de IMC
"""

def calcular_imc(altura_cm: float, peso_kg: float) -> float:
    """Calcula o IMC com base na altura (cm) e peso (kg)."""
    altura_metros = altura_cm / 100
    return peso_kg / (altura_metros ** 2)

def classificar_imc(imc: float) -> str:
    """Retorna a classificação do IMC."""
    if imc >= 40:
        return "Obesidade Grave"
    elif imc >= 30:
        return "Obesidade"
    elif imc >= 25:
        return "Sobrepeso"
    elif imc >= 18.5:
        return "Normal"
    else:
        return "Magreza"

def main():
    """Função principal para entrada e saída de dados."""
    try:
        altura = float(input("Qual sua altura (cm)? ").strip())
        peso = float(input("Qual seu peso (kg)? ").strip())
        
        if altura <= 0 or peso <= 0:
            print("Altura e peso devem ser valores positivos.")
            return
        
        imc = calcular_imc(altura, peso)
        classificacao = classificar_imc(imc)
        
        print(f"Seu IMC é: {imc:.2f} ({classificacao})")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
