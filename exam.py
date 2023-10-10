import json

class Exam:
    def __init__(self, exam_file, result_file):
        self.exam_file = exam_file
        self.result_file = result_file

    def load_my_exam_data(self):
        with open(self.exam_file, 'r', encoding='utf-8') as json_file:
            self.exam_data = json.load(json_file)

    def take_my_exam(self):
        student_name = input("Please input your name: ")
        student_surname = input("Please input your surname: ")

        user_answers = {}

        for question_number, question_data in self.exam_data['exam_content'].items():
            print(f"Question {question_number}: {question_data['question']}")
            print("Choice answer:")
            print(f"A: {question_data['a']}")
            print(f"B: {question_data['b']}")
            print(f"C: {question_data['c']}")
            print(f"D: {question_data['d']}")

            user_answer = input("Enter the letter of your answer (A/B/C/D): ").strip().lower()

            if user_answer not in ['a', 'b', 'c', 'd']:
                print("Incorrect answer option. Please enter A, B, C, or D.")
                continue

            user_answers[question_number] = {
                'question': question_data['question'],
                'selected_option': user_answer
            }

        result = {
            "student_name": student_name,
            "student_surname": student_surname,
            "user_answers": user_answers
        }

        with open(self.result_file, 'w', encoding='utf-8') as result_file:
            json.dump(result, result_file, ensure_ascii=False, indent=4)

        print("Your answers are saved in the 'results.json' file.")

if __name__ == "__main__":
    exam = Exam('exam.json', 'results.json')
    exam.load_my_exam_data()
    exam.take_my_exam()
