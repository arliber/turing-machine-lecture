const X_B = {
  'B_s1': ['X', 'R', 's2'],
  'B_s2': ['B', 'L', 's3'],
  'X_s3': ['B', 'R', 's4'],
  'B_s4': ['B', 'L', 's1']
}

function simulate(instructions) {
  // Initial state
  let tape = ['B', 'B']
  let head = 0
  let state = 's1'

  for (let i = 0; i <= 8; i++) {
    console.log(`${state}: ${tape.join('')}`)
    console.log(`    ${' '.repeat(head)}^`)

    let key = `${tape[head]}_${state}`
    let [newSymbol, headDirection, newState] = instructions[key]
    tape[head] = newSymbol
    head += headDirection === 'R' ? 1 : -1
    state = newState
  }
}

simulate(X_B)
