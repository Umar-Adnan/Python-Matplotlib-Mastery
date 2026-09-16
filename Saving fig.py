import matplotlib.pyplot as plt

study_hours = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
exam_scores = [52, 55, 60, 62, 68, 74, 77, 81]

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, exam_scores, color='crimson')

plt.title("Study Hours vs. Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(color = "Grey", linestyle="-.", linewidth=0.51)
# SAVE BEFORE plt.show()
plt.savefig("study_vs_score.png", dpi=300, bbox_inches='tight')

# Display on screen
plt.show()