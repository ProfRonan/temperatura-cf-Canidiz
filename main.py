"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    C = float(input("Qual a temperatura em graus Celsius?\n"))
    J = C * 9 / 5 + 32
    print(f"A temperatura em Fahrenheit é {J}.")


if __name__ == '__main__':
    main()
