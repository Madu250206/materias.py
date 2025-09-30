from __future__ import annotations


def ler_float(msg: str, lo: float = 0.0, hi: float = 10.0) -> float:
    while True:
        try:
            v = float(input(msg).strip().replace(",", "."))
            if lo <= v <= hi:
                return v
            print(f"Digite um valor entre {lo} e {hi}.")
        except ValueError:
            print("Número inválido, tente novamente.")

def ler_int(msg: str, lo: int, hi: int) -> int:
    while True:
        s = input(msg).strip()
        if s.isdigit():
            v = int(s)
            if lo <= v <= hi:
                return v
        print(f"Digite um inteiro entre {lo} e {hi}.")

def media_trabalhos_simples() -> float:
    n = ler_int("Quantos trabalhos já fez? ", 0, 100)
    if n == 0:
        return 0.0
    notas = [ler_float(f"  Nota do trabalho {i+1}: ") for i in range(n)]
    return sum(notas) / n

def calcula_necessario(meta: float,
                       nota_trabalho: float,
                       peso_trabalho: float,
                       pesos_provas: list[float],
                       notas_provas: list[float | None]) -> tuple[float, float, float, float, int]:
    if len(pesos_provas) != len(notas_provas):
        raise ValueError("Tamanhos diferentes entre pesos_provas e notas_provas.")
    peso_total_provas = sum(pesos_provas)
    peso_provas_global = 1.0 - peso_trabalho

    contrib_trab = nota_trabalho * peso_trabalho

    soma_feitas = 0.0
    peso_feito = 0.0
    faltam = 0
    for nota, w in zip(notas_provas, pesos_provas):
        if nota is None:
            faltam += 1
        else:
            soma_feitas += nota * w
            peso_feito += w

    contrib_provas_feitas = (soma_feitas / peso_total_provas) * peso_provas_global if peso_feito > 0 else 0.0
    peso_restante_interno = peso_total_provas - peso_feito

    if peso_restante_interno <= 1e-9:
        necessario = 0.0
    else:
        necessario = (meta - (contrib_trab + contrib_provas_feitas)) * (
            peso_total_provas / (peso_provas_global * peso_restante_interno)
        )

    return (nota_trabalho, contrib_trab, contrib_provas_feitas, necessario, faltam)

def imprime_resultado(meta: float,
                      m_trab: float,
                      c_trab: float,
                      c_provas: float,
                      necessario: float,
                      faltam_n: int):
    print("\n======== RESULTADO ========")
    print(f"Meta final: {meta:.2f}")
    print(f"Trabalhos: {m_trab:.2f}  → contribui {c_trab:.2f}")
    print(f"Provas já feitas contribuem: {c_provas:.2f}")

    if faltam_n == 0:
        media_final = c_trab + c_provas
        print(f"\nMÉDIA FINAL = {media_final:.2f}")
        print("✅ Meta atingida!" if media_final >= meta - 1e-9 else "❌ Meta não atingida.")
        return

    if necessario <= 0:
        print("\n✅ Você já atingiu a meta; nas provas restantes pode tirar 0,00.")
    elif necessario <= 10:
        if faltam_n == 1:
            print(f"\n➡️  Precisa tirar **{necessario:.2f}** na prova restante.")
        else:
            print(f"\n➡️  Precisa de **média {necessario:.2f}** nas {faltam_n} provas restantes (~{necessario:.2f} em cada).")
    else:
        print(f"\n❌ Mesmo com 10, não atinge a meta (precisaria de {necessario:.2f}).")

# -------------------- disciplinas --------------------

def calculo(meta: float):
    print("\n--- Cálculo --- (Trab=20%, Provas=80%; pesos provas: 2,2,3,3)")
    peso_trab = 0.20
    pesos_provas = [2, 2, 3, 3]

    m_trab = media_trabalhos_simples()

    notas_provas: list[float | None] = []
    for i, w in enumerate(pesos_provas, 1):
        tem = input(f"Já tem nota da Prova {i} (peso {w})? (s/n) ").strip().lower()
        if tem == "s":
            notas_provas.append(ler_float(f"  Nota P{i}: "))
        else:
            notas_provas.append(None)

    m, c_trab, c_provas, necessario, faltam = calcula_necessario(
        meta, m_trab, peso_trab, pesos_provas, notas_provas
    )
    imprime_resultado(meta, m, c_trab, c_provas, necessario, faltam)

def ft(meta: float):
    print("\n--- Fenômenos de Transporte --- (Trab=30%, Provas=70%; pesos provas: 2,3)")
    peso_trab = 0.30
    pesos_provas = [2, 3]

    m_trab = media_trabalhos_simples()

    notas_provas: list[float | None] = []
    for i, w in enumerate(pesos_provas, 1):
        tem = input(f"Já tem nota da Prova {i} (peso {w})? (s/n) ").strip().lower()
        if tem == "s":
            notas_provas.append(ler_float(f"  Nota P{i}: "))
        else:
            notas_provas.append(None)

    m, c_trab, c_provas, necessario, faltam = calcula_necessario(
        meta, m_trab, peso_trab, pesos_provas, notas_provas
    )
    imprime_resultado(meta, m, c_trab, c_provas, necessario, faltam)

def mecanica(meta: float):
    print("\n--- Mecânica Geral --- (Trab=30%, Provas=70%; pesos provas: 2,3)")
    peso_trab = 0.30
    pesos_provas = [2, 3]

    m_trab = media_trabalhos_simples()

    notas_provas: list[float | None] = []
    for i, w in enumerate(pesos_provas, 1):
        tem = input(f"Já tem nota da Prova {i} (peso {w})? (s/n) ").strip().lower()
        if tem == "s":
            notas_provas.append(ler_float(f"  Nota P{i}: "))
        else:
            notas_provas.append(None)

    m, c_trab, c_provas, necessario, faltam = calcula_necessario(
        meta, m_trab, peso_trab, pesos_provas, notas_provas
    )
    imprime_resultado(meta, m, c_trab, c_provas, necessario, faltam)

def fisica(meta: float):
    print("\n--- Física --- (Trab=40% [1 trabalho], Provas=60%; pesos provas: 2,3)")
    peso_trab = 0.40
    pesos_provas = [2, 3]

    nota_trab_unico = ler_float("Nota do trabalho (único) 0–10: ")

    notas_provas: list[float | None] = []
    for i, w in enumerate(pesos_provas, 1):
        tem = input(f"Já tem nota da Prova {i} (peso {w})? (s/n) ").strip().lower()
        if tem == "s":
            notas_provas.append(ler_float(f"  Nota P{i}: "))
        else:
            notas_provas.append(None)

    m, c_trab, c_provas, necessario, faltam = calcula_necessario(
        meta, nota_trab_unico, peso_trab, pesos_provas, notas_provas
    )
    imprime_resultado(meta, m, c_trab, c_provas, necessario, faltam)

def estruturas_dados(meta: float):
    print("\n--- Estruturas de Dados --- (Listas=20%, Provas=80%)")
    entregues = ler_int("Quantas listas ENTREGOU (0 a 10)? ", 0, 10)
    nota_trabalho = float(entregues)  

    total_provas = ler_int("Quantas PROVAS existem no ano? ", 1, 20)
    feitas = ler_int("Quantas PROVAS já tem nota? ", 0, total_provas)

    notas_provas: list[float | None] = []
    pesos_provas = [1.0] * total_provas

    soma_feitas = 0.0
    for i in range(1, feitas + 1):
        soma_feitas += ler_float(f"  Nota da prova #{i}: ")
        notas_provas.append(None)  

    
    notas_provas = []
    for i in range(1, total_provas + 1):
        if i <= feitas:
            nota = ler_float(f"Confirmando nota da prova #{i}: ")
            notas_provas.append(nota)
        else:
            notas_provas.append(None) 

    peso_trab = 0.20  
    m, c_trab, c_provas, necessario, faltam = calcula_necessario(
        meta, nota_trabalho, peso_trab, pesos_provas, notas_provas
    )
    imprime_resultado(meta, m, c_trab, c_provas, necessario, faltam)
def resmat(meta: float):
    print("\n--- Resistência dos Materiais --- (Trab=50%, Provas=50%; pesos provas: 2,2,3,3)")
    peso_trab = 0.50
    pesos_provas = [2, 2, 3, 3]

    m_trab = media_trabalhos_simples()

    notas_provas: list[float | None] = []
    for i, w in enumerate(pesos_provas, 1):
        tem = input(f"Já tem nota da Prova {i} (peso {w})? (s/n) ").strip().lower()
        if tem == "s":
            notas_provas.append(ler_float(f"  Nota P{i}: "))
        else:
            notas_provas.append(None)

    m, c_trab, c_provas, necessario, faltam = calcula_necessario(
        meta, m_trab, peso_trab, pesos_provas, notas_provas
    )
    imprime_resultado(meta, m, c_trab, c_provas, necessario, faltam)
def analogicos(meta: float):
    print("\n--- Fundamentos de Circuitos Analógicos --- (Trab=30%, Provas=70%; 2 provas com mesmo peso)")
    peso_trab = 0.30
    pesos_provas = [1, 1]  
    m_trab = media_trabalhos_simples()

    notas_provas: list[float | None] = []
    for i, w in enumerate(pesos_provas, 1):
        tem = input(f"Já tem nota da Prova {i}? (s/n) ").strip().lower()
        if tem == "s":
            notas_provas.append(ler_float(f"  Nota P{i}: "))
        else:
            notas_provas.append(None)

    m, c_trab, c_provas, necessario, faltam = calcula_necessario(
        meta, m_trab, peso_trab, pesos_provas, notas_provas
    )
    imprime_resultado(meta, m, c_trab, c_provas, necessario, faltam)


def main():
    print("== Calcular nota necessária nas provas ==")
    print("1) Cálculo")
    print("2) Fenômenos de Transporte (FT)")
    print("3) Mecânica Geral")
    print("4) Física")
    print("5) Estruturas de Dados")
    print("6) Resistência dos Materiais")
    print("7) Fundamentos de Circuitos Analógicos")

    op = input("Escolha (1-7): ").strip()
    meta = ler_float("Meta final desejada (0–10): ", 0.0, 10.0)

    if op == "1":
        calculo(meta)
    elif op == "2":
        ft(meta)
    elif op == "3":
        mecanica(meta)
    elif op == "4":
        fisica(meta)
    elif op == "5":
        estruturas_dados(meta)
    elif op == "6":
        resmat(meta)
    elif op == "7":                                # <-- novo
        analogicos(meta)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
