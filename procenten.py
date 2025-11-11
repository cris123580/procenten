"""Procenten - eenvoudige Nederlandstalige CLI

Beschikbare acties:
- Bereken x% van y
- Bereken welk percentage a is van b
- Verhoog of verlaag een bedrag met een percentage
- Bereken procentuele verandering (van oud naar nieuw)

Deze tool is bedoeld voor educatief gebruik en eenvoudige berekeningen.
"""

def parse_number(prompt: str) -> float:
    """Lees een getal in van de gebruiker. Vervang komma door punt en valideren."""
    while True:
        s = input(prompt).strip()
        s = s.replace(',', '.')
        try:
            return float(s)
        except ValueError:
            print("Ongeldige invoer. Voer een getal in (bijv. 12.5 of 12,5). Probeer opnieuw.")


def percent_of(x: float, y: float) -> float:
    """Bereken x% van y."""
    return x / 100.0 * y


def percent_of_total(a: float, b: float) -> float:
    """Bereken welk percentage a is van b. Als b == 0, retourneer None."""
    if b == 0:
        return None
    return a / b * 100.0


def change_by_percent(value: float, pct: float, increase: bool = True) -> float:
    """Verhoog of verlaag value met pct procent."""
    factor = 1 + (pct / 100.0) if increase else 1 - (pct / 100.0)
    return value * factor


def percent_change(old: float, new: float) -> float:
    """Bereken procentuele verandering van old naar new. Als old == 0, retourneer None."""
    if old == 0:
        return None
    return (new - old) / old * 100.0


def find_total_from_part_pct(part: float, pct: float) -> float:
    """Gegeven: deel en percentage (deel = pct% van totaal). Zoek totaal."""
    if pct == 0:
        return None
    return part * 100.0 / pct


def original_before_change(new_value: float, pct: float, increase: bool = True) -> float:
    """Gegeven nieuwe waarde na verhoging/verlaging met pct%, bereken oorspronkelijke waarde."""
    factor = 1 + pct / 100.0 if increase else 1 - pct / 100.0
    if factor == 0:
        return None
    return new_value / factor


def apply_compound_percents(value: float, percents: list[float]) -> float:
    """Pas achtereenvolgens meerdere procenten toe op een waarde.

    percents: lijst met procenten (positief = verhoging, negatief = verlaging)
    Retourneert de eindwaarde.
    """
    result = value
    for p in percents:
        result = change_by_percent(result, p, increase=(p >= 0))
    return result


def show_overview() -> None:
    """Toont een beknopt overzicht van procentbegrippen en voorbeeldvragen met uitleg."""
    print()
    print("Procenten in 1 overzicht:\n(procent = per honderd = 1/100 = 0,01)")
    print()
    # Voorbeeld 1
    a1 = 13
    b1 = 365
    r1 = percent_of(a1, b1)
    print(f"Vraag: hoeveel is {a1}% van {b1}?\nAntwoord: {a1/100} x {b1} = {r1}")
    print()
    # Voorbeeld 2
    a2 = 121
    b2 = 412
    r2 = percent_of_total(a2, b2)
    print(f"Vraag: hoeveel % is {a2} van {b2}?\nAntwoord: {a2} : {b2} = {r2} (dus {r2}% )")
    print()
    # Voorbeeld 3 verhogen
    v3 = 576
    p3 = 17
    r3 = change_by_percent(v3, p3, increase=True)
    print(f"Vraag: {v3} neemt toe met {p3}%; hoeveel heb je nu?\nAntwoord: 1 + {p3/100} = {1 + p3/100} ; {1 + p3/100} x {v3} = {r3}")
    print()
    # Voorbeeld 4 verlagen
    v4 = 576
    p4 = 17
    r4 = change_by_percent(v4, p4, increase=False)
    print(f"Vraag: {v4} neemt af met {p4}%; hoeveel heb je nu?\nAntwoord: 1 - {p4/100} = {1 - p4/100} ; {1 - p4/100} x {v4} = {r4}")
    print()
    # Voorbeeld 5 procentuele toename
    old5 = 326
    new5 = 413
    r5 = percent_change(old5, new5)
    print(f"Vraag: {old5} is toegenomen naar {new5}; met hoeveel procent is het toegenomen?\nAntwoord: {new5} : {old5} = {new5/old5} -> {new5/old5} is {new5/old5 - 1} meer dan 1, dus {r5}%")
    print()
    # Voorbeeld 6 procentuele afname
    old6 = 413
    new6 = 326
    r6 = percent_change(old6, new6)
    print(f"Vraag: {old6} is afgenomen naar {new6}; met hoeveel procent is het afgenomen?\nAntwoord: {new6} : {old6} = {new6/old6} -> {1 - new6/old6} minder dan 1, dus {abs(r6)}% afname")
    print()
    # Voorbeeld 7: terugrekenen (oud = nieuw / factor)
    new7 = 654
    p7 = 17
    orig_inc = original_before_change(new7, p7, increase=True)
    orig_dec = original_before_change(new7, p7, increase=False)
    print(f"Vraag: neemt toe met {p7}% en is nu {new7}; wat was het eerst?\nAntwoord (toename): {new7} : {1 + p7/100} = {orig_inc}")
    print(f"Vraag: neemt af met {p7}% en is nu {new7}; wat was het eerst?\nAntwoord (afname): {new7} : {1 - p7/100} = {orig_dec}")
    print()
    print("Dit overzicht toont de kortste rekenwijzen: gebruik 0,01 * waarde voor procenten of vermenigvuldig met 1 ± pct/100 voor toename/afname.")


def main() -> None:
    print("Welkom bij Procenten (Nederlandstalige CLI)")
    while True:
        print()
        print("Kies een optie:")
        print("0) Overzicht / Theorie (met voorbeelden)")
        print("1) Hoeveel is x% van y? (x% * y)")
        print("2) Hoeveel % is a van b? (a / b * 100)")
        print("3) Gegeven deel en procent -> zoek totaal (deel = pct% van totaal)")
        print("4) Verhoog of verlaag een waarde met %")
        print("5) Gegeven nieuwe waarde na verandering -> zoek oorspronkelijke waarde")
        print("6) Procentuele verandering (van oud naar nieuw)")
        print("7) Samengestelde procenten (meerdere procenten achter elkaar)")
        print("8) Afsluiten")

        choice = input("Welke optie kies je? ").strip()

        match choice:
            case '0':
                show_overview()

            case '1':
                x = parse_number("Voer x (procent) in: ")
                y = parse_number("Voer y (totaal) in: ")
                result = percent_of(x, y)
                print(f"Berekening: {x}% = {x/100} ; {x/100} * {y} = {result}")
                print(f"Antwoord: {x}% van {y} is {result}")

            case '2':
                a = parse_number("Voer a (deel) in: ")
                b = parse_number("Voer b (totaal) in: ")
                pct = percent_of_total(a, b)
                if pct is None:
                    print("Kan niet delen door 0 (b is 0).")
                else:
                    print(f"Berekening: ( {a} / {b} ) * 100 = {pct}")
                    print(f"Antwoord: {a} is {pct}% van {b}")

            case '3':
                part = parse_number("Voer het deel (a) in: ")
                pct = parse_number("Voer het percentage (pct) in: ")
                total = find_total_from_part_pct(part, pct)
                if total is None:
                    print("Kan geen totaal berekenen met pct = 0.")
                else:
                    print(f"Berekening: totaal = deel * 100 / pct = {part} * 100 / {pct} = {total}")
                    print(f"Antwoord: totaal = {total}")

            case '4':
                value = parse_number("Voer de beginwaarde in: ")
                pct = parse_number("Voer het percentage in (bijv. 10 voor 10%): ")
                dir_choice = input("Wil je verhogen of verlagen? (v/verh / l/verl): ").strip().lower()
                increase = True if dir_choice.startswith('v') else False
                new_value = change_by_percent(value, pct, increase=increase)
                op = 'verhoogd' if increase else 'verlaagd'
                sign = '+' if increase else '-'
                print(f"Berekening: {value} {sign} {pct}% -> factor = {1 + (pct/100) if increase else 1 - (pct/100)} ; resultaat = {new_value}")
                print(f"Antwoord: waarde {op} met {pct}% = {new_value}")

            case '5':
                new_val = parse_number("Voer de nieuwe waarde (na verandering) in: ")
                pct = parse_number("Voer het percentage waarmee veranderd is (bijv. 10 voor 10%): ")
                dir_choice = input("Was het een verhoging of verlaging? (v/l): ").strip().lower()
                increase = True if dir_choice.startswith('v') else False
                orig = original_before_change(new_val, pct, increase=increase)
                if orig is None:
                    print("Kan originele waarde niet berekenen (factor is 0).")
                else:
                    print(f"Berekening: origineel = nieuw / factor = {new_val} / {1 + (pct/100) if increase else 1 - (pct/100)} = {orig}")
                    print(f"Antwoord: oorspronkelijke waarde = {orig}")

            case '6':
                old = parse_number("Voer de oude waarde in: ")
                new = parse_number("Voer de nieuwe waarde in: ")
                pc = percent_change(old, new)
                if pc is None:
                    print("Kan geen procentuele verandering berekenen wanneer de oude waarde 0 is.")
                else:
                    direction = 'toename' if new > old else 'afname' if new < old else 'geen verandering'
                    print(f"Berekening: ( {new} - {old} ) / {old} * 100 = {pc}%")
                    print(f"Antwoord: procentuele {direction}: {pc}%")

            case '7':
                start = parse_number("Voer beginwaarde in: ")
                raw = input("Voer procenten achtereenvolgens in, gescheiden door komma's (bijv. 10, -20, 5): ")
                parts = [p.strip().replace(',', '.') for p in raw.split(',') if p.strip()]
                try:
                    pvals = [float(p) for p in parts]
                except ValueError:
                    print("Ongeldige procentlijst; gebruik komma's en getallen (bijv. 10, -20).")
                    continue
                result = start
                print(f"Startwaarde: {start}")
                for p in pvals:
                    before = result
                    result = change_by_percent(result, p, increase=(p >= 0))
                    print(f"Toepassen {p}%: {before} -> {result}")
                print(f"Eindwaarde na samengestelde procenten: {result}")

            case '8' | 'q' | 'quit' | 'exit':
                print("Tot ziens!")
                break

            case _:
                print("Ongeldige optie. Kies 1-8.")


if __name__ == '__main__':
    main()