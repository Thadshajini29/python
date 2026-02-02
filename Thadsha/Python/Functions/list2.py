# x = [
#     [10, 20, 30],
#     [70, 90, 25],
#     [40, 98, 26]
# ]

# # Access individual elements
# print(x[0][0])  # 10
# print(x[1][0])  # 70
# print(x[1][1])  # 90

# # Loop through the 2D list
# i = 0
# while i < 3:
#     j = 0
#     while j < 3:
#         print(x[i][j])
#         j += 1
#     i += 1

    
subjects = ["SFT", "BST", "ICT"]

students = [
    ["Thadsha", [40, 50, 60]],
    ["Kopi", [50, 70, 60]],
    ["Sumi", [60, 70, 30]],
    ["Kavi", [55, 65, 75]],
    ["Aathi", [45, 35, 25]]
]

# Print header
print(f"{'Student Name':<12} {'SFT':<6} {'BST':<6} {'ICT':<6} {'Total':>6} {'Average':>8} {'Result':>6}")

for student in students:
    name = student[0]
    scores = student[1]   # renamed to avoid conflict
    total = sum(scores)
    average = total / len(scores)

    # Grade logic
    if 75 <= average <= 100:
        result = 'A'
    elif 65 <= average < 75:
        result = 'B'
    elif 55 <= average < 65:
        result = 'C'
    elif 45 <= average < 55:
        result = 'S'
    elif 0 <= average < 45:
        result = 'F'
    else:
        result = "Correct Format"

    print(f"{name:<12} {scores[0]:<6} {scores[1]:<6} {scores[2]:<6} {total:>6} {average:>8.2f} {result:>6}")
