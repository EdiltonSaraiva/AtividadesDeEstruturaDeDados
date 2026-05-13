print("\n---CORREÇÃO DE PROVAS---\n")

gabarito = ["A ", "D", "D", "B", "C", "D", "A", "C", "B", "D"]
quantidade_questoes, quantidade_alunos = 10, 5

resultados = [int] * 5
nome_alunos = [str] * 5

marcadas_aluno1 = [str] * 10
marcadas_aluno2 = [str] * 10
marcadas_aluno3 = [str] * 10
marcadas_aluno4 = [str] * 10
marcadas_aluno5 = [str] * 10

provas = [str] * quantidade_questoes

for alunos in range(len(provas)):
    provas[alunos] = [str] * quantidade_alunos

for nomes in range(len(nome_alunos)):

    nome_alunos = input(f"Digite o nome do {nomes + 1}º aluno(a):\t")
    
    for numero_questao in range(len(marcadas_aluno1)):

            alternativa_marcada = input(f"Alternativa marcada pelo(a) aluno(a) na {numero_questao + 1}ª questão:\t")
            marcadas_aluno1[numero_questao] = alternativa_marcada
            