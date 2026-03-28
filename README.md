<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:1a0505,100:0a0a1a&height=200&section=header&text=SOC%20%2B%20GRC&fontSize=72&fontColor=ffffff&animation=fadeIn&fontAlignY=42&desc=Security%20Operations%20%7C%20Governance%20%7C%20Risk%20%7C%20Compliance&descAlignY=66&descColor=666666&descSize=15&fontStyle=bold"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=2500&pause=1000&color=FF4444&center=true&vCenter=true&width=700&lines=Log+parsing+and+MITRE+ATT%26CK+detection+engineering;Risk+scoring+with+likelihood+%C3%97+impact;ISO+27001+and+NIST+CSF+compliance+checking;The+feedback+loop+between+detection+and+governance"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.8+-0d1117?style=flat-square&logo=python&logoColor=00ff41)
![Tests](https://img.shields.io/badge/tests-24%20passing-0d1117?style=flat-square&logo=pytest&logoColor=00ff41)
![License](https://img.shields.io/badge/license-MIT-0d1117?style=flat-square)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-0d1117?style=flat-square&logoColor=ff4444)

</div>

---

## Interactive learning site

<div align="center">

[![Open the interactive guide](https://img.shields.io/badge/Interactive%20Guide-SOC%20%2B%20GRC%20from%20scratch-ff4444?style=for-the-badge&labelColor=0d1117)](https://speed-boo3.github.io/soc-grc-project/explain/)

</div>

An interactive portfolio site with live animations, real images, scanner simulation, risk scoring tool, AI analyst and self-assessment checklist. Built to show how SOC and GRC work together in practice.

---

## What this project is

Built as part of a master's in cybersecurity. It covers two areas that most courses teach separately and never connect: Security Operations Center work and Governance, Risk and Compliance.

The SOC detects threats in real time. GRC makes sure the right controls exist to prevent them. In practice they feed each other continuously — a SOC alert raises a GRC risk score, a GRC policy creates a new SOC detection rule, a compliance gap becomes a detection engineering task. This project builds both sides and demonstrates the loop between them.

---

## The SOC side

The SOC tools form a pipeline. Raw log files go in. Structured, MITRE-tagged alerts come out.

```
python soc/log-parser/generate_logs.py
python soc/log-parser/parser.py --file soc/log-parser/sample.log --output parsed.json
python soc/alert-rules/alert_engine.py --logs parsed.json --rules soc/alert-rules/rules.yaml
```

Output:

```
3 alert(s) triggered:

[HIGH] Brute Force Detected (RULE-001)
  MITRE ATT&CK : T1110 - Brute Force (Credential Access)
  Log entry    : Source IP 45.33.32.156 had 9 failed login attempts

[MEDIUM] Sudo Authentication Failure (RULE-003)
  MITRE ATT&CK : T1078 - Valid Accounts (Privilege Escalation)
  Log entry    : pam_unix(sudo:auth): authentication failure uid=1003

[MEDIUM] Segfault Detected (RULE-006)
  MITRE ATT&CK : T1203 - Exploitation for Client Execution (Execution)
  Log entry    : program[4821]: segfault at 0x0 ip 00007f error 4
```

### What is built

**Log parser** reads raw logs and classifies every line by type — SSH auth, Apache access, syslog. Flags suspicious entries and outputs structured JSON.

**Alert engine** runs YAML detection rules against the parsed output. Every rule maps to a MITRE ATT&CK technique so every alert tells you not just what happened but what the attacker is trying to accomplish.

**Brute force detector** uses a sliding time window to count failed logins per IP. A burst of 9 attempts in 60 seconds is treated differently to 9 attempts spread over a week — because attack rate matters more than total count.

**Threat intelligence** checks source IPs against AbuseIPDB. A 97% abuse confidence score changes a suspicious login into a confirmed targeted attack from a known threat actor. Context changes response priority.

**Dashboard** gives a terminal overview of log volume by type, top source IPs and recent suspicious events.

**IR playbook** provides step-by-step response procedures for each alert type based on NIST SP 800-61.

### MITRE ATT&CK coverage

| ID | Technique | Tactic | Rule |
|---|---|---|---|
| T1110 | Brute Force | Credential Access | RULE-001 |
| T1110.004 | Credential Stuffing | Credential Access | RULE-004 |
| T1078 | Valid Accounts | Initial Access | RULE-002 |
| T1078 | Valid Accounts | Privilege Escalation | RULE-003 |
| T1190 | Exploit Public Application | Initial Access | RULE-005 |
| T1203 | Exploitation for Client Execution | Execution | RULE-006 |

---

## The GRC side

GRC is the strategic layer. It answers the questions the SOC cannot: are our controls correct? Can we prove they work? What are our biggest risks right now?

```
python grc/risk-assessment/risk_matrix.py --file grc/risk-assessment/sample_risks.json
```

Output:

```
Risk Assessment Report
======================================================================
ID         Risk                            Score   Level      Owner
----------------------------------------------------------------------
RISK-002   Phishing attack                  20     Critical   Security Team
RISK-001   Unpatched systems                20     Critical   IT Operations
RISK-005   SQL injection data breach        15     High       Dev Team
RISK-003   Insider threat                   10     High       HR / Security
RISK-004   DDoS attack                       9     Medium     Network Team
RISK-006   Lost or stolen laptop             6     Medium     IT Operations
```

### What is built

**Risk matrix** scores risks by likelihood x impact. Both run 1 to 5. The result tells you what to fix first when you cannot fix everything at once.

**Network scanner** wraps nmap and converts risky open ports into structured risk register entries automatically. Checks whether the network matches what the security policy says it should — the gap between them is where audit findings come from.

**Security policy** is a complete template covering access control, patch management, incident response, data handling and physical security.

**Compliance checklist** covers ISO 27001 and NIST CSF controls in one document. Score your coverage and see exactly which controls are missing.

**Report generator** runs every Monday, Wednesday and Friday via GitHub Actions. Produces a markdown report with compliance scores and risk distribution. Results are in `reports/`.

---

## The loop between them

This is the most important part of the project. SOC and GRC are not separate teams doing separate things.

When the SOC detects a brute force attack, that finding goes into the GRC risk register. The likelihood score rises. The risk level escalates. The security policy is reviewed and updated — SSH key authentication becomes mandatory, password auth is disabled. The SOC then gets a new detection rule: any password-based SSH attempt is now a policy violation. The next weekly GRC report shows the Access Control compliance score improving. Then it starts again.

Every detection improves governance. Every policy creates new rules. This is what mature security operations actually looks like.

---

## Project structure

```
soc-grc-project/
├── soc/
│   ├── log-parser/
│   │   ├── parser.py               <- reads and classifies log lines
│   │   └── generate_logs.py        <- generates realistic test logs daily
│   ├── alert-rules/
│   │   ├── rules.yaml              <- 6 detection rules with MITRE mapping
│   │   ├── alert_engine.py         <- runs logs against the rules
│   │   └── threat_intel.py         <- AbuseIPDB IP reputation lookup
│   ├── brute-force-detector/
│   │   └── detector.py             <- sliding window brute force detection
│   ├── dashboard/
│   │   └── dashboard.py            <- terminal overview
│   └── incident-response/
│       └── playbook.md             <- IR procedures per alert type
├── grc/
│   ├── risk-assessment/
│   │   ├── risk_matrix.py          <- likelihood x impact scoring
│   │   └── sample_risks.json       <- 6 example risks
│   ├── network-scan/
│   │   └── scanner.py              <- nmap wrapper with risk output
│   ├── policies/
│   │   └── security_policy.md      <- full policy template
│   └── compliance/
│       └── checklist.md            <- ISO 27001 and NIST CSF checklist
├── scripts/
│   └── generate_report.py          <- weekly report generator
├── reports/                        <- generated compliance reports
├── explain/
│   └── index.html                  <- interactive learning site
├── .github/workflows/
│   ├── daily-scan.yml              <- runs every morning at 07:00 UTC
│   └── weekly-report.yml           <- Mon, Wed, Fri at 08:00 UTC
└── requirements.txt
```

---

## Quickstart

```bash
git clone https://github.com/Speed-boo3/soc-grc-project.git
cd soc-grc-project
pip install -r requirements.txt
```

Run the full SOC pipeline:

```bash
python soc/log-parser/generate_logs.py
python soc/log-parser/parser.py --file soc/log-parser/sample.log --output parsed.json
python soc/alert-rules/alert_engine.py --logs parsed.json --rules soc/alert-rules/rules.yaml
```

Score the GRC risks:

```bash
python grc/risk-assessment/risk_matrix.py --file grc/risk-assessment/sample_risks.json
```

Run the tests:

```bash
pytest tests/ -v
```

---

## Learn more

- [MITRE ATT&CK](https://attack.mitre.org) — technique and tactic library
- [NIST SP 800-61](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) — incident handling guide
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) — international security management standard
- [NIST CSF](https://www.nist.gov/cyberframework) — five-function security lifecycle
- [AbuseIPDB](https://www.abuseipdb.com) — IP reputation database

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a0505,50:0a0a1a,100:0d1117&height=100&section=footer&text=Detect.%20Govern.%20Comply.&fontSize=16&fontColor=ff4444&animation=twinkling"/>
</div>
