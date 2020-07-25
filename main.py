import random
import openpyxl as xl

# initialize vers data sheel
wb = xl.load_workbook("Verbs.xlsx")
sheet = wb["verbs"]
cell_yo = sheet.cell(1, 2)
max_row = sheet.max_row
max_column = sheet.max_column


def quiz_creator():
    quiz_row = random.randint(2, max_row)
    quiz_column = random.randint(2, max_column)
    quiz_subject_cell = sheet.cell(1, quiz_column)
    quiz_verb_cell = sheet.cell(quiz_row, 1)
    quiz_answer_cell = sheet.cell(quiz_row, quiz_column)
    return quiz_subject_cell.value, quiz_verb_cell.value, quiz_answer_cell.value


while True:
    subject, verb, answer = quiz_creator()
    your_answer = input(f"[{subject}][{verb}] -> ").lower()
    if your_answer == "quit":
        break
    elif your_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong! Should be {answer}!")
