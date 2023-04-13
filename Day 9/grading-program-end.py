# Yechim
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Yuqoridagi kodni o'zgartirmang 👆

#TODO-1: student_grades deb nomlangan boʻsh lugʻat yarating.

student_grades = {}

#TODO-2: Baholarni student_grades ga qo'shish uchun pastga kodingizni yozing.👇

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Ajoyib"
  elif score > 80:
    student_grades[student] = "Namunali"
  elif score > 70:
    student_grades[student] = "Qoniqarli"
  else:
    student_grades[student] = "Qoniqarsiz"  
    
# 🚨 Pastdagi kodni o'zgartirmang 👆
print(student_grades)
