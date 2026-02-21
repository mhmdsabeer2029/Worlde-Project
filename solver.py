from math import log2
import json
def get_pattern(guess, target):
    pattern = ['0'] * 5

    for i in range(5):
        if guess[i] == target[i]:
            pattern[i] = '2'

    for i in range(5):
        if pattern[i] != '2':
            for j in range(5):
              if pattern[j] == '0' and target[i] == guess[j]:
                pattern[j] = '1'
                break

    return int("".join(pattern), 3)

def get_index(eval):
  index = ['0'] * 5
  for i in range(5):
    if eval[i] == 'y':
      index[i] = '1'
    elif eval[i] == 'g':
      index[i] = '2'
  return int("".join(index), 3)

dic = []
sols = []
tree = {}
sorted_ents = []
with open('targets.json', 'r') as file:
    sols = json.load(file)
with open('dict.json', 'r') as file:
    dic = json.load(file)
with open('wordle_tree.json', 'r') as file:
    tree = json.load(file)
with open('wordle_entropy.json', 'r') as file:
    sorted_ents = json.load(file)
ents = dict(sorted_ents)
n = len(sols)

for round in range(1, 7):
  print(f"\n==== Round {round} ====\n")
  print(f"Remaining possible answers: {n}")
  print(f"Remaining entropy: {log2(n):.5f}\n")
  if n == 1:
    print(f"Solution: {sols[0]}")
    break
  print("Top suggestions:")

  for i in range(20):
    print(f"{i + 1}. {sorted_ents[i][0]}   entropy = {sorted_ents[i][1]:.5f}")
  print("\nEnter your guess: ", end="")
  guess = input().lower()
  print("Enter the evaluation: ", end="")
  result = input().lower()
  sols = tree[guess][get_index(result)][:]
  n = len(sols)

  for guess in dic:
    ents[guess] = 0.0
    tree[guess] = [[] for _ in range(243)]
    for sol in sols:
      tree[guess][get_pattern(guess, sol)].append(sol)
    for branch in tree[guess]:
      p = len(branch) / n
      if p != 0:
        ents[guess] += p * -log2(p)

  sorted_ents = sorted(ents.items(), key=lambda item: (item[1], item[0] in sols), reverse=True)