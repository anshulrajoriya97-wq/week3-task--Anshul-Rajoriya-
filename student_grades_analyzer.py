# grades_analyzer.py
import pandas as pd

def analyze(csv_file="grades.csv", pass_mark=40):
    df = pd.read_csv(csv_file)
    subjects = df.columns.drop("Name")
    summary = {subj: (df[subj].mean(), df[subj].max(), df[subj].min()) for subj in subjects}
    df['Average'] = df[subjects].mean(axis=1)
    top3 = df.nlargest(3, 'Average')
    df['Pass/Fail'] = df[subjects].ge(pass_mark).all(axis=1).map({True: 'Pass', False: 'Fail'})
    return summary, top3[['Name', 'Average', 'Pass/Fail']]

if __name__ == "__main__":
    summaries, top3 = analyze("grades.csv")
    for subj, (avg, hi, lo) in summaries.items():
        print(f"{subj}: avg={avg:.2f}, high={hi}, low={lo}")
    print("\nTop 3 Students:")
    print(top3.to_string(index=False))
  
