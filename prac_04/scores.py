"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()

    extract_subject_scores(score_values, subjects)


def extract_subject_scores(score_values, subjects):
    subject_scores = []
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        for score in score_values:
            subject_scores.append(score[i])
        output_scores(subject_scores)
        subject_scores.clear()
    return subject_scores


def output_scores(subject_scores):
    print(subject_scores)
    print("Max:", max(subject_scores))
    print("Min:", min(subject_scores))
    print("Average:", sum(subject_scores) / len(subject_scores))


main()
