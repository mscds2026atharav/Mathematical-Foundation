# %%
#1. Simulate Conditional Probability (Card Drawing)
import random

# Create a deck of 52 cards
deck = []

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for suit in suits:
    for rank in ranks:
        deck.append([rank, suit])

# Number of simulations
n = int(input("Enter number of simulations: "))

king = 0
face = 0
king_face = 0

for i in range(n):

    # Draw one random card
    card = random.choice(deck)

    # Check if the card is a King
    if card[0] == "K":
        king = king + 1

    # Check if the card is a face card
    if card[0] == "J" or card[0] == "Q" or card[0] == "K":
        face = face + 1

        # Check if it is also a King
        if card[0] == "K":
            king_face = king_face + 1

# Calculate probabilities
prob_king = king / n
prob_face = face / n
prob_king_given_face = king_face / face

# Theoretical probabilities
theory_king = 4 / 52
theory_face = 12 / 52
theory_king_given_face = 4 / 12

# Display results
print("\nSimulation Results")
print("P(A) = Probability of King =", prob_king)
print("P(B) = Probability of Face Card =", prob_face)
print("P(A|B) = Probability of King given Face Card =", prob_king_given_face)

print("\nTheoretical Values")
print("P(A) =", theory_king)
print("P(B) =", theory_face)
print("P(A|B) =", theory_king_given_face)

# %%
# 2. Conditional Probability (Dice Rolling)
import random

# Number of simulations
n = int(input("Enter number of simulations: "))

sum8 = 0
one3 = 0
both = 0

for i in range(n):

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Check if sum is 8
    if die1 + die2 == 8:
        sum8 = sum8 + 1

    # Check if at least one die is 3
    if die1 == 3 or die2 == 3:
        one3 = one3 + 1

    # Check if both events occur
    if (die1 + die2 == 8) and (die1 == 3 or die2 == 3):
        both = both + 1

# Calculate probabilities
probA = sum8 / n
probB = one3 / n
probA_given_B = both / one3

# Theoretical probabilities
theoryA = 5 / 36
theoryB = 11 / 36
theoryA_given_B = 2 / 11

# Display results
print("\nSimulation Results")
print("P(A) = Probability that sum is 8 =", probA)
print("P(B) = Probability that at least one die is 3 =", probB)
print("P(A|B) = Probability that sum is 8 given at least one die is 3 =", probA_given_B)

print("\nTheoretical Values")
print("P(A) =", theoryA)
print("P(B) =", theoryB)
print("P(A|B) =", theoryA_given_B)

# %%
# 3. Total Probability (Machine Fault Detection)
import random

# Number of items
n = 10000

defective = 0

A_defective = 0
B_defective = 0
C_defective = 0

for i in range(n):

    # Select machine
    r = random.random()

    if r < 0.30:
        machine = "A"
    elif r < 0.75:
        machine = "B"
    else:
        machine = "C"

    # Check if item is defective
    d = random.random()

    if machine == "A":
        if d < 0.02:
            defective = defective + 1
            A_defective = A_defective + 1

    elif machine == "B":
        if d < 0.03:
            defective = defective + 1
            B_defective = B_defective + 1

    else:
        if d < 0.04:
            defective = defective + 1
            C_defective = C_defective + 1

# Estimated probabilities
P_D = defective / n

P_A_given_D = A_defective / defective
P_B_given_D = B_defective / defective
P_C_given_D = C_defective / defective

# Theoretical probabilities
theory_P_D = (0.30 * 0.02) + (0.45 * 0.03) + (0.25 * 0.04)

theory_P_A_given_D = (0.30 * 0.02) / theory_P_D
theory_P_B_given_D = (0.45 * 0.03) / theory_P_D
theory_P_C_given_D = (0.25 * 0.04) / theory_P_D

# Display results
print("Simulation Results")
print("P(D) =", P_D)
print("P(A|D) =", P_A_given_D)
print("P(B|D) =", P_B_given_D)
print("P(C|D) =", P_C_given_D)

print("\nTheoretical Values")
print("P(D) =", theory_P_D)
print("P(A|D) =", theory_P_A_given_D)
print("P(B|D) =", theory_P_B_given_D)
print("P(C|D) =", theory_P_C_given_D)