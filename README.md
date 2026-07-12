# EazyVote v2.1.1

> **A desktop election management system built for St. George Public School, Kottapady — Academic Session 2024–2025**

---

## Overview

**EazyVote** is a secure, fast, and visually polished voting application designed for conducting internal student council elections within educational institutions. It runs entirely on-site using local hardware, connecting to a MySQL database to record and retrieve votes in real time.

Built with Python, it provides a smooth, GUI-driven experience for voters and administrators alike — from casting ballots to viewing final results.

---

## Features

- 🗳️ **Interactive Ballot UI** — Voters select candidates via clickable photo-buttons across two election posts (School Headboy & School Headgirl)
- 📊 **Real-Time Results Dashboard** — Generates and displays a live tabular view of vote counts with CSV export
- 🔒 **One-Vote-Per-Session Enforcement** — Candidate buttons are disabled after selection to prevent double voting
- 🗄️ **MySQL-Backed Storage** — All votes are persisted in a local MySQL database (`george`) in real time
- 📋 **CSV Report Export** — Results are automatically exported to `results.csv` on report generation
- ℹ️ **About & Terms & Conditions** — Built-in popups for legal and product information
-  **Vote Reset Utility** — Admin can reset all votes to zero without clearing candidate data
- 🔧 **DB Initializer Script** — One-shot script to create and seed the database from scratch

---

## Project Structure

```
Project EazyVote v2.1.1 for St George School/
│
├── stgeorge.py             # Main voting application (voter-facing ballot UI)
├── result.py               # Results viewer (admin-facing results & CSV export)
├── sqltable.py             # Database initializer (creates tables and seeds candidate data)
├── reset.py                # Utility to reset all vote counts to zero
│
├── Candidates/             # Candidate profile photos
│   ├── candidate1.jpg      # Alan Mathew
│   ├── candidate2.jpg      # Arjun Santhosh
│   ├── candidate3.jpg      # Jeevana M. S.
│   ├── candidate4.jpg      # Haripriya Rajeev
│   ├── candidate5.jpg      # Karthikey Lal
│   └── candidate6.jpg      # Vaiga S. Nair
│
├── continuebtn.jpg         # "Continue" button image asset
├── finishbtn.jpg           # "Finish" button image asset
├── nextbtn.jpg             # "Next" button image asset
├── quitbtn.jpg             # "Quit" button image asset
├── generbtn.jpg            # "Generate Results" button image asset
├── startscreen.jpg         # Voting app splash/start screen background
├── resstrtscrn.jpg         # Results app splash screen background
├── table.jpg               # Results table background image
│
├── results.csv             # Auto-generated CSV results report
│
├── Fonts/                  # Custom font files (Google Sans, IBM Plex Mono)
├── Legal/                  # Legal/copyright documents
├── Deployement/            # PyInstaller distributable builds
│
├── stgeorge.py.spec        # PyInstaller spec for main voting app
├── result.spec             # PyInstaller spec for results viewer
├── sqltable.spec           # PyInstaller spec for DB initializer
├── reset.spec              # PyInstaller spec for reset utility
│
└── logo.ico                # Application icon
```

---

## Candidates

| Serial No. | Name              | Class | Post             |
|:----------:|-------------------|:-----:|------------------|
| 1          | Alan Mathew       | X     | School Headboy   |
| 2          | Arjun Santhosh    | X     | School Headboy   |
| 3          | Jeevana M. S.     | X     | School Headgirl  |
| 4          | Haripriya Rajeev  | X     | School Headgirl  |
| 5          | Karthikey Lal     | X     | School Headboy   |
| 6          | Vaiga S. Nair     | X     | School Headgirl  |

> **Note:** Posts displayed are "School Headboy" and "School Headgirl". The ballot shows 3 candidates per post simultaneously. Voters choose one from each post.

---

## Tech Stack

| Component     | Technology                                     |
|---------------|------------------------------------------------|
| Language      | Python 3                                       |
| GUI Framework | Tkinter (with ttk)                             |
| Image Handling| Pillow (PIL)                                   |
| Database      | MySQL (via `mysql-connector-python`)           |
| Reporting     | `csv` module (built-in)                        |
| Build/Deploy  | PyInstaller (`.spec` files + standalone `.exe`)|
| Fonts         | Google Sans, IBM Plex Mono                     |

---

## Database Schema

The application uses a MySQL database named **`george`**.

### `candidate` table
| Column     | Type         | Description              |
|------------|--------------|--------------------------|
| Serial_No  | INT (UNIQUE) | Candidate identifier     |
| Name       | VARCHAR(30)  | Full name of candidate   |
| Class      | VARCHAR(4)   | Student's class          |
| Post       | VARCHAR(20)  | Election post contested  |

### `votes` table
| Column    | Type         | Description                         |
|-----------|--------------|-------------------------------------|
| Serial_No | INT (UNIQUE) | Matches candidate Serial_No         |
| Name      | VARCHAR(30)  | Candidate name (for readability)    |
| votes     | INT          | Running vote count (starts at 0)    |

---

## Prerequisites

Before running the application, ensure the following are installed:

- **Python 3.8+**
- **MySQL Server** (running locally on `localhost`, default port `3306`)
- The following Python packages:

```bash
pip install mysql-connector-python Pillow
```

> **MySQL Credentials (default):** `user=root`, `password=1234`, `host=localhost`
> You can change these in `stgeorge.py`, `result.py`, `sqltable.py`, and `reset.py` if needed.

---

## Setup & Usage

### Step 1 — Initialize the Database

Run this **once** before first use to create the database, tables, and seed candidate data:

```bash
python sqltable.py
```

### Step 2 — Run the Voting Application

Launch the voter-facing ballot interface:

```bash
python stgeorge.py
```

- The splash screen appears; click **Continue** to start voting.
- Candidates are displayed with their photos.
- Click a candidate image to vote for them. Buttons are **disabled** after selection.
- After voting for both posts, click **Finish**.
- A confirmation screen appears. Click **Quit** to return to start for the next voter.

### Step 3 — View Results (Admin Only)

After all voting is complete, run the results viewer:

```bash
python result.py
```

- Click **Generate Results** to display the live tally table.
- Results are simultaneously exported to **`results.csv`** in the project directory.

### Step 4 — Reset Votes (Optional)

To clear all vote counts (e.g., for a new election or testing):

```bash
python reset.py
```

> ⚠️ This resets all candidate vote counts to `0`. It does **not** delete candidate records.

---

## Running Pre-Built Executables

If you prefer to run EazyVote without a Python environment, navigate to the `Deployement/` or `dist/` folders for pre-compiled standalone `.exe` files built with PyInstaller.

> Make sure MySQL Server is still running locally before launching the executables.

---

## Building Executables (Optional)

To recompile the executables from source using PyInstaller:

```bash
pyinstaller stgeorge.py.spec
pyinstaller result.spec
pyinstaller sqltable.spec
pyinstaller reset.spec
```

Output will be placed in the `dist/` directory.

---

## Window Resolution

The application is designed and optimized for a **1366×768** display resolution. Using a different resolution may affect UI element positioning.

---

## Legal

- © 2024 EazyVote. All rights reserved.
- Developed by **Gregory Ajish** and **Lestlin Robins**.
- Unauthorized reproduction, distribution, or modification of this software is strictly prohibited.
- EazyVote v2.1.1 is protected by copyright laws and international treaties.
- See the `Legal/` folder for full terms and conditions documentation.

---

## Authors

| Name           | Role                    |
|----------------|-------------------------|
| Gregory Ajish  | Developer & Co-creator  |
| Lestlin Robins | Developer & Co-creator  |

---

*Last updated: 10th July 2024 — EazyVote v2.1.1*
