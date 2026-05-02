import os
from datetime import datetime

def get_input(prompt, required=True):
    while True:
        user_input = input(prompt).strip()
        if not user_input and required:
            print("This field is required. Please enter a value.")
        else:
            return user_input

def format_filename(title):
    return title.lower().replace(" ", "_").replace("/", "-") + ".md"

def generate_markdown(title, summary, tools, steps, role, frequency):
    now = datetime.now().strftime("%Y-%m-%d")
    return f"""# SOP: {title}

**Date Created:** {now}

**Summary:**
{summary}

**Tools Used:**
{tools}

**Steps:**
{steps}

**Responsible Role:**
{role}

**Frequency:**
{frequency}
"""

def main():
    print("\n--- Remote Team SOP Generator ---\n")

    title = get_input("Enter SOP Title: ")
    summary = get_input("Enter a short summary of the task: ")
    tools = get_input("List tools or systems used (comma-separated): ")

    print("\nEnter the step-by-step instructions. Type 'done' when finished:")
    steps_list = []
    while True:
        step = input(f"Step {len(steps_list) + 1}: ").strip()
        if step.lower() == 'done':
            break
        if step:
            steps_list.append(f"{len(steps_list) + 1}. {step}")

    steps = "\n".join(steps_list)
    role = get_input("Enter the role responsible for this task: ")
    frequency = get_input("How often is this task performed? (e.g., Daily, Weekly): ")

    content = generate_markdown(title, summary, tools, steps, role, frequency)
    filename = format_filename(title)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"\n✅ SOP saved as '{filename}' in the current folder.")

if __name__ == "__main__":
    main()