def generate_correct_bracket_sequences(n, opened_brackets_quantity, bracket_sequence, closing_brackets):
    if len(bracket_sequence) == 2 * n:
        result.append(''.join(bracket_sequence))
        return
    if opened_brackets_quantity < n:
        closing_brackets.append(')')
        bracket_sequence.append('(')
        generate_correct_bracket_sequences(n, opened_brackets_quantity + 1, bracket_sequence, closing_brackets)
        closing_brackets.pop()
        bracket_sequence.pop()
        closing_brackets.append(']')
        bracket_sequence.append('[')
        generate_correct_bracket_sequences(n, opened_brackets_quantity + 1, bracket_sequence, closing_brackets)
        closing_brackets.pop()
        bracket_sequence.pop()
    if len(closing_brackets) > 0:
        bracket = closing_brackets.pop()
        bracket_sequence.append(bracket)
        generate_correct_bracket_sequences(n, opened_brackets_quantity, bracket_sequence, closing_brackets)
        closing_brackets.append(bracket)
        bracket_sequence.pop()


n = int(input())
if n % 2 == 0:
    result = []
    generate_correct_bracket_sequences(n // 2, 0, [], [])
    print(*result, sep='\n')
