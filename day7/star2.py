from day7.instructions import Instructions
from utils import load_input

steps = load_input()

instructions = Instructions(steps, workers=5)
instructions.get_step_order()
print(instructions.seconds_spent)
