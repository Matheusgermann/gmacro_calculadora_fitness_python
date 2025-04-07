def calcular_tmb(genero, peso, altura, idade):
    if genero == "Masculino":
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    else:
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161

def calcular_tdee(tmb, nivel_atividade):
    if nivel_atividade == "Sedentário":
        return tmb * 1.2
    elif nivel_atividade == "Levemente ativo":
        return tmb * 1.375
    elif nivel_atividade == "Moderadamente ativo":
        return tmb * 1.55
    elif nivel_atividade == "Altamente ativo":
        return tmb * 1.725
    elif nivel_atividade == "Extremamente ativo":
        return tmb * 1.9

def calcular_calorias(tdee, objetivo):
    if objetivo == "Perder gordura":
        return tdee - (tdee * 0.2)
    elif objetivo == "Começar o processo de perda de gordura":
        return tdee - (tdee * 0.1)
    elif objetivo == "Manter peso":
        return tdee
    elif objetivo == "Começar o processo de ganho de massa muscular":
        return tdee + (tdee * 0.1)
    elif objetivo == "Ganhar massa muscular":
        return tdee + (tdee * 0.2)

def calcular_macronutrientes(peso, calorias):
    proteinas = peso * 2
    gorduras = peso * 1
    carboidratos = (calorias - (proteinas * 4) - (gorduras * 9)) / 4
    return proteinas, carboidratos, gorduras

def main():
    print("Projeto Gmacro")
    print("----------------")

    genero = input("Gênero Biológico (Masculino ou Feminino): ")
    idade = int(input("Idade (em anos): "))
    altura = int(input("Altura (em centimetros): "))
    peso = int(input("Peso (em kg): "))

    print("Objetivo:")
    print("1. Perder gordura")
    print("2. Começar o processo de perda de gordura")
    print("3. Manter peso")
    print("4. Começar o processo de ganho de massa muscular")
    print("5. Ganhar massa muscular")
    objetivo = ["Perder gordura", "Começar o processo de perda de gordura", "Manter peso", "Começar o processo de ganho de massa muscular", "Ganhar massa muscular"][int(input("Escolha o objetivo: ")) - 1]

    print("Nível de atividade Física:")
    print("1. Sedentário(pouca ou nenhuma atividade física no dia a dia)")
    print("2. Levemente ativo(atividade física leve, como caminhadas curtas ou exercícios leves 1 a 3 vezes por semana)")
    print("3. Moderadamente ativo(prática de exercícios moderados 3 a 5 dias por semana)")
    print("4. Altamente ativo(exercícios intensos 6 a 7 dias por semana)")
    print("5. Extremamente ativo(treinamento físico intenso diário e/ou trabalho físico pesado)")
    nivel_atividade = ["Sedentário", "Levemente ativo", "Moderadamente ativo", "Altamente ativo", "Extremamente ativo"][int(input("Escolha o nível de atividade: ")) - 1]

    tmb = calcular_tmb(genero, peso, altura, idade)
    tdee = calcular_tdee(tmb, nivel_atividade)
    calorias = calcular_calorias(tdee, objetivo)
    proteinas, carboidratos, gorduras = calcular_macronutrientes(peso, calorias)

    print("\nCom base nos dados informados, você deve consumir diariamente:")
    print(f"kcal: {calorias:.2f}")
    print(f"proteínas: {proteinas:.2f}g")
    print(f"carboidratos: {carboidratos:.2f}g")
    print(f"gorduras: {gorduras:.2f}g")

if __name__ == "__main__":
    main()