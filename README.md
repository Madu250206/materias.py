# 📘 Calculadora de Notas — Engenharia IMT 2025, segundo ano 

Um programa em Python que ajuda a calcular **quanto você precisa tirar nas provas** para alcançar a média desejada em cada disciplina do curso.  
Cada disciplina tem regras próprias de **peso de provas e trabalhos**, já configuradas no código.

---

## 🚀 Como rodar
1. Clone este repositório ou baixe o arquivo `materias.py`.
2. Certifique-se de ter **Python 3** instalado.
3. No terminal, dentro da pasta do projeto, rode:
   ```bash
   python materias.py
4. Escolha a disciplina no menu e informe suas notas já obtidas.
Disciplinas configuradas
🔹 Cálculo Diferencial e Integral II
    Trabalhos: média simples (20%)
    Provas: 4 provas (80%)
    P1 e P2 (peso 2 cada)
    P3 e P4 (peso 3 cada)

🔹 Fenômenos de Transporte (FT)
    Trabalhos: média simples (30%)
    Provas: 2 provas (70%)
    P1 (peso 2)
    P2 (peso 3)

🔹 Mecânica Geral
    Trabalhos: média simples (30%)
    Provas: 2 provas (70%)
    P1 (peso 2)
    P2 (peso 3)

🔹 Física II
    Trabalho: único (40%)
    Provas: 2 provas (60%)
    P1 (peso 2)
    P2 (peso 3)

🔹 Estruturas de Dados
    Trabalhos: 10 listas , peso 20%
    Provas: número definido pelo usuário, peso 80% (média simples)

🔹 Resistência dos Materiais
    Trabalhos: média simples (50%)
    Provas: 4 provas (50%)
    P1 e P2 (peso 2 cada)
    P3 e P4 (peso 3 cada)

🔹 Fundamentos de Circuitos Analógicos
    Trabalhos: média simples (30%)
    Provas: 2 provas (70%), mesmo peso

EXEMPLO DE USO 
    == Calcular nota necessária nas provas ==
    1) Cálculo
    2) Fenômenos de Transporte (FT)
    3) Mecânica Geral
    4) Física
    5) Estruturas de Dados
    6) Resistência dos Materiais
    7) Fundamentos de Circuitos Analógicos
    Escolha (1-7): 5
    Meta final desejada (0–10): 7
    --- Estruturas de Dados --- (Listas=20%, Provas=80%)
    Quantas listas ENTREGOU (0 a 10)? 9
    Quantas PROVAS existem no ano? 8
    Quantas PROVAS já tem nota? 6
    Nota da prova #1: 5.9
    Nota da prova #2: 7.6
    Nota da prova #3: 10
    Nota da prova #4: 4
    Nota da prova #5: 5.9
    Nota da prova #6: 7.5
    
    ======== RESULTADO ========
    Meta final: 7.00
    Trabalhos: 9.00  → contribui 1.80
    Provas já feitas contribuem: 4.09

    Precisa de média 0.55 nas 2 provas restantes (~0.55 em cada).
