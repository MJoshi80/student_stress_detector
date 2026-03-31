import analyzer
import storage
from datetime import datetime

def show_menu():
    print("\n=============================")
    print("  Student Stress Detector 🎯")
    print("=============================")
    print("1. Log today's entry")
    print("2. Show this week's entries")
    print("3. Generate weekly summary")
    print("0. Exit")
    print("=============================")

def log_entry():
    statement=input("Enter how you're feeling today 😊:")
    date=datetime.now().strftime("%d/%m/%Y")
    day=datetime.now().strftime("%A")
    score,sentiment=analyzer.analyse(statement)
    storage.save_entry(date,day,statement,score,sentiment)
    print("✓ Entry saved!")
    print(f"Sentiment: {sentiment} ({score})")

def show_entries():
    entries = storage.get_entries()
    if len(entries) == 0:
        print("Oops! There aren't any entries yet 😅")
        return
    for entry in entries:
        print(f"📅 {entry['day']} {entry['date']}")
        print(f"📝 {entry['statement']}")
        print(f"💭 {entry['sentiment']} ({entry['score']})")
        print("-------------------")

def weekly_summary():
    entries = storage.get_entries()
    if len(entries) == 0:
        print("Oops! There aren't any entries yet 😅")
        return
    scores = [entry['score'] for entry in entries]
    average = sum(scores)/ len(scores)
    if average < -0.3 :
        sentiment = "Stressed"
    elif average >= -0.3 and average <= 0.3:
        sentiment = "Neutral"
    else:
        sentiment = "Positive"
    print("\n📅 Weekly Summary")
    print("==================")
    for entry in entries:
        print(f"{entry['day']} → {entry['sentiment']}")
    print("==================")
    print(f"Overall → {sentiment} ({round(average,2)})")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        log_entry()
    elif choice == "2":
        show_entries()
    elif choice == "3":
        weekly_summary()
    elif choice == "0":
        print("Goodbye! Take care 🌟")
        break
    else:
        print("Oops! Invalid choice 😅. Please try again!")