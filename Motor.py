import random
def fazer_pergunta(dados_da_pergunta):
    print(f"\n[{dados_da_pergunta['categoria'].upper()} - {dados_da_pergunta['dificuldade'].capitalize()}]")
    print(dados_da_pergunta['enunciado'])
    
    letras = ['a', 'b', 'c', 'd']
    for i, opcao in enumerate(dados_da_pergunta['opcoes']):
        print(f"{letras[i]}) {opcao}")
        
    conversao_indices = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    
    while True:
        resposta = input("\nSua resposta (A, B, C ou D): ").strip().lower()
        if resposta in conversao_indices:
            indice_escolhido = conversao_indices[resposta]
            break
        print("Opção inválida! Digite apenas A, B, C ou D.")

    if indice_escolhido == dados_da_pergunta['correta']:
        print("Resposta correta! 🎉")
        return True
    
    opcao_certa = dados_da_pergunta['opcoes'][dados_da_pergunta['correta']]
    print(f"Errado! A resposta correta era: {opcao_certa}")
    return False

def jogar(lista_perguntas):
    pontos = 0
    total = 0
    perguntas_aleatorias = lista_perguntas.copy()
    random.shuffle(perguntas_aleatorias)
    
    print("\n=== O JOGO VAI COMEÇAR ===")
    
    for pergunta in perguntas_aleatorias:
        total += 1
        if fazer_pergunta(pergunta):
            pontos += 1
        else:
            print("\nGame Over! Você errou a questão.")
            break
            
    print(f"\nPartida encerrada. Pontuação final: {pontos}")
  

def mostrar_resultado(pontos, total):
    print("\n==============================")
    print("         FIM DE JOGO!         ")
    print("==============================")
    print(f"Você acertou {pontos} de {total} perguntas.")
    
    if total > 0:
        aproveitamento = (pontos / total) * 100
        print(f"Desempenho: {aproveitamento:.1f}%")
