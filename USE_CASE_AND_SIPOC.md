# 📘 Use Case and SIPOC

How a process owner uses the SOP Generator to document a fixed process, written as a use case with main and exception flows, plus a SIPOC showing where the SOP process starts and who receives the output. Every system response below comes from a test run of `sop_generator.py`.

## 📝 Use Case UC-01: Create an SOP

| Item | Detail |
|---|---|
| Primary Actor | Process owner (the person who fixed or changed the process) |
| Stakeholders | Staff who perform the task, new hires in training, supervisors, QA reviewers |
| Trigger | A process gets fixed or changed, and the new steps need to be written down |
| Preconditions | Python 3 installed. Process owner knows the steps, tools, responsible role, and frequency. Script runs from the folder where the SOP should be saved |
| Postconditions | A Markdown SOP with title, creation date, summary, tools, numbered steps, responsible role, and frequency is saved in the working folder. No existing SOP is changed |

### Main Flow

| Step | Actor Action | System Response |
|---|---|---|
| 1 | Runs `python sop_generator.py` | Shows the SOP Generator header and asks for the SOP title |
| 2 | Enters the title | Asks for a short summary |
| 3 | Enters the summary | Asks for tools or systems used |
| 4 | Enters the tools, separated by commas | Asks for step 1 |
| 5 | Enters each step, one per line | Numbers each step and asks for the next one |
| 6 | Types `done` | Asks for the responsible role |
| 7 | Enters the role | Asks how often the task is performed |
| 8 | Enters the frequency | Adds the creation date, formats the SOP, saves the file, and shows the file name |

### Exception Flows

| ID | Condition | System Response | Returns To |
|---|---|---|---|
| E1 | Title, summary, tools, role, or frequency left blank | "This field is required. Please enter a value." and asks again | Same step |
| E2 | `done` typed before any step | "At least one step is required." and asks for step 1 again | Step 5 |
| E3 | Blank line entered during steps | Skips the line. Step number stays the same | Step 5 |
| E4 | Title contains punctuation or symbols | File name keeps letters and numbers only. "Weekly Case Tracker Reconciliation!" saves as `weekly_case_tracker_reconciliation.md` | Step 8 |
| E5 | An SOP with the same file name already exists | Saves as `_2`, `_3`, and so on. The existing SOP stays untouched | Step 8 |
| E6 | Script stopped before the last prompt | Nothing gets saved. No partial SOP file | Start over at Step 1 |

### Business Rules

| ID | Rule |
|---|---|
| BR-01 | Every field is required |
| BR-02 | An SOP needs at least one step |
| BR-03 | Steps are numbered in the order entered |
| BR-04 | Every SOP carries the date created |
| BR-05 | A new SOP never overwrites an existing one |

### Out of Scope

- Editing an existing SOP
- Version history, approval, or review dates
- Steps longer than one line
- Choosing a save folder from inside the script

## 🔁 SIPOC

| Suppliers | Inputs | Process | Outputs | Customers |
|---|---|---|---|---|
| Process owner | SOP title | 1. Capture SOP details | Markdown SOP file | Staff who perform the task |
| Subject matter experts | Task summary | 2. Enter steps in order | Same format across every SOP | New hires in training |
| Team lead | Tools and systems used | 3. Check required fields | Creation date on every SOP | Supervisors |
| | Step-by-step instructions | 4. Number, date, and format the SOP | Responsible role and frequency on record | QA reviewers and auditors |
| | Responsible role | 5. Save without overwriting | | |
| | Frequency | | | |

**Process start:** a fixed or changed process needs written steps.
**Process end:** the SOP file is saved and ready to share.

See [`examples/weekly_case_tracker_reconciliation.md`](examples/weekly_case_tracker_reconciliation.md) for an SOP produced by the main flow.
