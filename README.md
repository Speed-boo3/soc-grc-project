<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:1a0000,60:0a0a1a,100:1a0000&height=200&section=header&text=SOC%20%2B%20GRC&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=42&desc=Security%20Operations%20%7C%20Governance%20%7C%20Risk%20%7C%20Compliance&descAlignY=66&descColor=888888&descSize=14"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=2500&pause=900&color=FF4444&center=true&vCenter=true&width=650&lines=Log+parsing+and+alert+detection+with+MITRE+ATT%26CK;Risk+scoring+with+likelihood+%C3%97+impact;ISO+27001+and+NIST+CSF+compliance+checking;Built+as+part+of+a+master+in+cybersecurity"/>

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

Six modules with live animations, real images, a scanner simulation, risk scoring tool and knowledge checklist. Built for students who want to understand how SOC and GRC work together.

---

## What is this

A project built as part of a master's in cybersecurity. It covers both Security Operations Center work and Governance, Risk and Compliance — and shows how the two feed each other in practice.

Most courses teach SOC and GRC as separate subjects. In the real world they are two sides of the same coin. The SOC detects what is happening. GRC makes sure the right controls exist to prevent it. This project shows both.

---

## The SOC side

```
soc/
├── log-parser/
│   ├── parser.py           <- reads logs, detects type, flags suspicious entries
│   └── generate_logs.py    <- generates realistic test log files
├── alert-rules/
│   ├── rules.yaml          <- detection rules mapped to MITRE ATT&CK
│   ├── alert_engine.py     <- runs logs against the rules
│   └── threat_intel.py     <- AbuseIPDB IP reputation lookup
├── brute-force-detector/
│   └── detector.py         <- sliding window brute force detection
├── dashboard/
│   └── dashboard.py        <- terminal overview of log stats
└── incident-response/
    └── playbook.md         <- step-by-step IR procedures per alert type
```

Run the full pipeline:

```bash
python soc/log-parser/generate_logs.py
python soc/log-parser/parser.py --file soc/log-parser/sample.log --output parsed.json
python soc/alert-rules/alert_engine.py --logs parsed.json --rules soc/alert-rules/rules.yaml
```

---

## The GRC side

```
grc/
├── risk-assessment/
│   ├── risk_matrix.py      <- likelihood x impact scoring engine
│   └── sample_risks.json   <- 6 example risks to get started
├── network-scan/
│   └── scanner.py          <- nmap wrapper that outputs risk register entries
├── policies/
│   └── security_policy.md  <- full security policy template
└── compliance/
    └── checklist.md        <- ISO 27001 and NIST CSF checklist
```

Score the example risks:

```bash
python grc/risk-assessment/risk_matrix.py --file grc/risk-assessment/sample_risks.json
```

---

## MITRE ATT&CK coverage

```
T1110      Brute Force              Credential Access
T1110.004  Credential Stuffing      Credential Access
T1078      Valid Accounts           Initial Access / Privilege Escalation
T1190      Exploit Public App       Initial Access
T1203      Client Exploitation      Execution
```

---

## The connection

When the SOC detects a brute force attack from a known malicious IP, that finding goes into the GRC risk register. The risk score rises. The security policy gets updated. The SOC gets a new detection rule. The compliance score improves. Then it starts again.

This loop is what real security operations look like.

---

## Quickstart

```bash
git clone https://github.com/Speed-boo3/soc-grc-project.git
cd soc-grc-project
pip install -r requirements.txt
```

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a0000,50:0a0a1a,100:0d1117&height=100&section=footer&text=Detect.%20Govern.%20Comply.&fontSize=16&fontColor=ff4444&animation=twinkling"/>
</div>
