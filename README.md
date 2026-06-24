# NICU Vitals Monitor (CS3500 Project)

A Neonatal Intensive Care Unit (NICU) vitals monitor simulator with a Tkinter GUI, validated clinician input forms, and a unit + black-box test suite. Built as a CS3500 software-engineering group project.

## What it does

The system simulates a live neonatal patient inside an incubator and surfaces real-time vital signs with color-coded threshold alerts, so clinicians can see at a glance whether a reading has drifted out of the safe range they configured.

- **Simulated patient & environment**
  - `Baby` generates heart rate (HR), blood pressure (BP), and temperature, updating once per second with small random drift.
  - `IncEnviornment` generates incubator humidity and oxygen levels, also updating once per second.
- **Clinician-validated thresholds**
  - `trainedUserInput.py` is a Tkinter entry form that collects the safe ranges (min/max HR, systolic/diastolic BP, temperature, humidity, oxygen) and rejects out-of-range or non-numeric input before launching the monitor.
- **Live monitoring UI**
  - `vitalsUI.py` renders the "Neonatal Intensive Care Unit Monitor" window, displays each vital, and recolors the indicator ovals **green** (in range) or **red** (out of range) every second using the `checkBabyVitals` / `checkIncVitals` helpers.
- **Testing**
  - `UnitTest.py` — randomized and fixed-case `unittest` suites covering the threshold-checking helpers.
  - `blackboxtesting.py` — black-box tests that drive the entry form in a background thread with random inputs and assert the acceptance/rejection logic.

## Project structure

```
babyAndEnviornment.py    # Baby + IncEnviornment simulators (vital-sign generators)
vitalsUI.py              # Tkinter monitoring window + threshold-checking helpers
trainedUserInput.py      # Tkinter entry form for clinician-configured safe ranges
UnitTest.py              # Unit tests for vitals threshold logic
blackboxtesting.py       # Black-box tests for the input validation + UI flow
.gitignore
old code/                # Earlier iterations of the UI and input handlers
__pycache__/             # Python bytecode cache (gitignored)
```

## Requirements

- Python 3.9+
- Tkinter (bundled with most Python installs; on Debian/Ubuntu: `sudo apt install python3-tk`)

No third-party packages are required — everything uses the Python standard library.

## Usage

```bash
python trainedUserInput.py
```

1. Enter the safe vital ranges in the form (temperature, HR min/max, BP min/max, humidity, oxygen).
2. Click **Submit**. If any value is missing, non-numeric, or physiologically implausible for a neonate, a dialog warns which field is at fault.
3. Once accepted, the monitoring window opens and begins updating live.

To run the unit and black-box tests:

```bash
python UnitTest.py
python blackboxtesting.py
```

## Safe-range reference (validated by the input form)

| Vital | Acceptable range |
| --- | --- |
| Temperature | 35–40 °C |
| Heart rate (min) | 50–120 bpm |
| Heart rate (max) | 100–180 bpm |
| Blood pressure (min, diastolic) | 50–100 |
| Blood pressure (max, systolic) | 100–150 |
| Humidity | 20–95 % |
| Oxygen | 15–30 % |

## Notes

This is a class project and a simulator only — it does **not** connect to any real medical device or patient data. All vital signs are randomly generated for demonstration purposes.
