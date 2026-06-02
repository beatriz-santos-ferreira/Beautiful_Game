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