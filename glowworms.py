from tkinter import Tk
import random
from time import sleep
import sys

# r = Tk()
# r.withdraw()

def copy_to_clipboard(text):
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(text)
	r.update()
	r.destroy()


def generate_glowworm_row(hanging_sign=False):
	symbols = [" ", ". ", "* ", "+ "]
	weights = [30 if hanging_sign else 60, 6, 3, 1]
	widths = {" ": 2, ". ": 1+2, "* ": 2+2, "+ ": 3+2}

	sign_width = 30 if hanging_sign else 45
	cum_width = 0
	output = ""

	while cum_width < sign_width:
		symbol = random.choices(symbols, weights)[0]
		if cum_width + widths[symbol] > sign_width:
			break
		output += symbol
		cum_width += widths[symbol]

	return output


if __name__ == "__main__":
	hanging_sign = len(sys.argv) > 1
	print("Hanging Sign" if hanging_sign else "Normal Sign")
	while(True):
		row = generate_glowworm_row(hanging_sign)
		print(row)
		copy_to_clipboard(row)
		sleep(0.1)
