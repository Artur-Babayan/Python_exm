# Python_exm
1. exam.py
import json:
  Мы импортируем модуль json, который позволит нам работать с JSON-файлами.
class Exam::
  Мы определяем класс Exam, который будет представлять экзамен.

def __init__(self, exam_file, result_file):
  Это конструктор класса Exam, который принимает два аргумента: exam_file (файл с вопросами экзамена) и result_file (файл, в который будут сохранены результаты).

self.exam_file = exam_file и self.result_file = result_file:
   Мы сохраняем переданные аргументы как атрибуты объекта класса, чтобы они были доступны в других методах.
   
def load_my_exam_data(self):
   Этот метод загружает данные экзамена из файла JSON (exam_file) и сохраняет их в атрибуте self.exam_data.
   
with open(self.exam_file, 'r', encoding='utf-8') as json_file:
   Мы открываем файл JSON для чтения.

self.exam_data = json.load(json_file): 
  Мы загружаем данные из файла JSON в атрибут self.exam_data с помощью функции json.load().
  
def take_my_exam(self):
  Этот метод выполняет экзамен, предлагая студенту ввести свое имя и фамилию, а затем предоставляет вопросы и записывает ответы студента.
  
student_name = input("Please input your name: ") и student_surname = input("Please input your surname: "): 
  Мы запрашиваем у студента имя и фамилию с помощью функции input() и сохраняем их в переменных student_name и student_surname.
  
user_answers = {}: 
  Мы создаем пустой словарь user_answers, который будет содержать ответы студента на вопросы экзамена.
  
for question_number, question_data in self.exam_data['exam_content'].items():
  Мы перебираем вопросы из атрибута exam_content в self.exam_data. question_number содержит номер вопроса, а question_data содержит данные о вопросе.
  Внутри этого цикла мы предоставляем студенту текст вопроса и варианты ответов, а затем запрашиваем ответ студента.
  
user_answer = input("Enter the letter of your answer (A/B/C/D): ").strip().lower(): 
  Мы запрашиваем ответ студента и преобразуем его в нижний регистр.
  Если введенный ответ не соответствует вариантам A, B, C или D, мы выводим сообщение об ошибке и продолжаем цикл.
  Мы записываем ответ студента в словарь user_answers, связывая его с номером вопроса.
  После ответа на все вопросы, мы создаем словарь result, который содержит имя студента, фамилию и ответы на вопросы.
  
Мы сохраняем результаты в файл JSON с помощью json.dump().

В блоке if __name__ == "__main__": 
  создается объект класса Exam, загружаются данные экзамена и выполняется экзамен



