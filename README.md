# SOC & GRC Project

This is a project I built as part of my master's in cybersecurity. It covers two areas: Security Operations Center (SOC) work and Governance, Risk, and Compliance (GRC). The goal was to tie together the practical and the theoretical sides of security into one place.

It is not meant to be a production tool. Think of it as a learning project that shows how these concepts work in practice.

---

## What is in here

The project is split into two main folders: `soc/` and `grc/`.

**SOC side:**
- A log parser that reads common log formats and pulls out useful information
- A set of detection rules written in YAML
- An incident response playbook
- A simple terminal dashboard that shows log stats

**GRC side:**
- A risk assessment tool using a basic risk matrix
- A sample security policy document
- A compliance checklist based on common frameworks

---

## How to run it

You need Python 3.8 or newer.

Install the dependencies:

```
pip install -r requirements.txt
```

Then you can run each part on its own. For example:

```
python soc/log-parser/parser.py --file sample.log
python soc/dashboard/dashboard.py
python grc/risk-assessment/risk_matrix.py
```

---

## Project structure

```
soc-grc-project/
├── soc/
│   ├── log-parser/
│   ├── alert-rules/
│   ├── incident-response/
│   └── dashboard/
├── grc/
│   ├── risk-assessment/
│   ├── policies/
│   └── compliance/
├── requirements.txt
└── README.md
```

---

## Why I built this

A lot of cybersecurity courses cover SOC and GRC separately. I wanted to see how they fit together. A SOC analyst deals with live threats, while GRC is about making sure the organization has the right policies and controls in place. They feed each other — good GRC makes the SOC's job easier.

---

## Notes

The sample log file used for testing is in `soc/log-parser/`. The detection rules in `alert-rules/rules.yaml` are written to match against parsed log output. The risk matrix uses likelihood and impact scores from 1 to 5.
