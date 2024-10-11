from dataclasses import dataclass
import openpyxl
import numpy as np
import numpy.typing as npt
import random

@dataclass
class Words:
    pronouns: npt.NDArray[np.str_]
    verbs: npt.NDArray[np.str_]
    verb_forms: npt.NDArray[np.str_]

def read_table(
    file_name: str = "words.xlsx",
    sheet_index: int = 0
) -> Words:
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook[workbook.sheetnames[sheet_index]]
    raw_data = np.array([np.array([value for value in row]) for row in sheet.values])
    return Words(
        pronouns=raw_data[0, 2:],
        verbs=raw_data[1:, 1],
        verb_forms=raw_data[1:, 2:],
    )

def play_round(words: Words):
    pronoun_idx = random.randint(0, words.pronouns.size - 1)
    verb_idx = random.randint(0, words.verbs.size - 1)
    print(f"{words.pronouns[pronoun_idx]} + {words.verbs[verb_idx]} = ?")
    print(">> ", end="")
    expected_answer: str = words.verb_forms[verb_idx, pronoun_idx]
    recieved_answer = input()
    if expected_answer.strip().lower() != recieved_answer.strip().lower():
        print(f"Wrong! Correct answer is {expected_answer}")
    else:
        print("Correct!")

def main():
    words = read_table()
    play_round(words)

if __name__ == "__main__":
    main()
