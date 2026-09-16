import matplotlib.pyplot as plt
study_hours = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
exam_scores = [52, 55, 60, 62, 68, 74, 77, 81, 85, 88, 92, 95]

plt.scatter(
    study_hours,
    exam_scores,
    color = "Blue",
    marker= "^",
    label = "Student Data"
)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Relation between hours studied and Exam Score")
plt.legend()
plt.grid(color = "Grey", linestyle = "--")
plt.show()