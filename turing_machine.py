X_B = {
  ('B', 's1'): ('X', 'R', 's2'),
  ('B', 's2'): ('B', 'L', 's3'),
  ('X', 's3'): ('B', 'R', 's4'),
  ('B', 's4'): ('B', 'L', 's1')
}

def simulate(instructions):
  '''
    Setup intial state
    loop:
      lookup next instruction
      apply that instruction
  '''

  tape = ['B', 'B']
  head = 0
  state = 's1'

  for i in range(8):  # Should be inifinte

    print(tape)

    # print(state.rjust(4) + ': ' + ''.join(tape))
    # print('      ' + ' ' * head + '^')

    key = (tape[head], state)
    new_symbol, head_direction, new_state = instructions[key] # Which is exactly what we need to move
    # Apply/Run command
    tape[head] = new_symbol
    head += 1 if head_direction == 'R' else -1
    state = new_state


simulate(X_B)