import random
import openpyxl as xl

reflection = {
    "yo": "me",
    "vos": "te",
    "el/ella/usted": "se",
    "nosotros/nosotras": "nos",
    "ellos/ellas/ustedes": "se"
}

suffix_ar = {
    "yo": "o",
    "vos": "ás",
    "el/ella/usted": "a",
    "nosotros/nosotras": "amos",
    "ellos/ellas/ustedes": "an"
}
suffix_er = {
    "yo": "o",
    "vos": "és",
    "el/ella/usted": "e",
    "nosotros/nosotras": "emos",
    "ellos/ellas/ustedes": "en"
}
suffix_ir = {
    "yo": "o",
    "vos": "ís",
    "el/ella/usted": "e",
    "nosotros/nosotras": "imos",
    "ellos/ellas/ustedes": "en"
}

# initialize vers data sheel
wb = xl.load_workbook("Verbs.xlsx")
sheet = wb["verbs"]
cell_yo = sheet.cell(1, 2)
max_row = sheet.max_row
max_column = sheet.max_column
print(f"total {max_row - 1} verbs to practise")


def get_reflect_verb(verb_reflect, sub):
    verb_reflect_formed = get_regular_verb_form(verb_reflect, sub)
    return f"{reflection[sub]} {verb_reflect_formed}"


def get_regular_verb_form(verb_regular, sub):
    suf = verb_regular[-2:]
    head = verb_regular[:-2]
    if suf == "ar":
        head += suffix_ar[sub]
    elif suf == "er":
        head += suffix_er[sub]
    elif suf == "ir":
        head += suffix_ir[sub]
    elif suf == "se":
        head = get_reflect_verb(head, sub)
    else:
        head = "unknown"
    return head


def quiz_creator():
    quiz_row = random.randint(2, max_row)
    quiz_column = random.randint(2, max_column)
    quiz_subject = sheet.cell(1, quiz_column).value
    quiz_verb = sheet.cell(quiz_row, 1).value
    quiz_answer = sheet.cell(quiz_row, quiz_column).value
    if quiz_answer is None:
        quiz_answer = get_regular_verb_form(quiz_verb, quiz_subject)
    return quiz_subject, quiz_verb, quiz_answer


while True:
    subject, verb, answer = quiz_creator()
    your_answer = input(f"[{subject}][{verb}] -> ").lower()
    if your_answer == "quit":
        break
    elif your_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong! Should be {answer}!")
