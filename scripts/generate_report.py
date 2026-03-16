import os
import random
from datetime import datetime, timedelta


def random_trend(base, variance, days):
    values = []
    current = base
    for _ in range(days):
        current += random.randint(-variance, variance)
        current = max(0, current)
        values.append(current)
    return values


def last_n_days(n):
    today = datetime.today()
    return [(today - timedelta(days=n - i - 1)).strftime("%b %d") for i in range(n)]


def quoted_labels(labels):
    return ", ".join('"' + l + '"' for l in labels)


def make_bar_chart(title, x_labels, values, y_axis_label="Count"):
    return (
        "```mermaid\n"
        "xychart-beta\n"
        '    title "' + title + '"\n'
        "    x-axis [" + quoted_labels(x_labels) + "]\n"
        '    y-axis "' + y_axis_label + '"\n'
        "    bar [" + ", ".join(str(v) for v in values) + "]\n"
        "```"
    )


def make_line_chart(title, x_labels, values, y_axis_label="Count"):
    return (
        "```mermaid\n"
        "xychart-beta\n"
        '    title "' + title + '"\n'
        "    x-axis [" + quoted_labels(x_labels) + "]\n"
        '    y-axis "' + y_axis_label + '"\n'
        "    line [" + ", ".join(str(v) for v in values) + "]\n"
        "```"
    )


def make_pie_chart(title, labels, values):
    slices = "\n".join('    "' + l + '" : ' + str(v) for l, v in zip(labels, values))
    return (
        "```mermaid\n"
        "pie title " + title + "\n"
        + slices + "\n"
        "```"
    )


def generate_soc_data(days=7):
    labels = last_n_days(days)
    return {
        "labels": labels,
        "alerts_total": random_trend(40, 10, days),
        "alerts_high": random_trend(5, 3, days),
        "false_positives": random_trend(15, 5, days),
        "incidents_closed": random_trend(8, 3, days),
        "log_volume_k": random_trend(120, 20, days),
        "alert_types": {
            "Brute Force": random.randint(10, 30),
            "Unauthorized Access": random.randint(5, 20),
            "Malware": random.randint(2, 10),
            "Policy Violation": random.randint(8, 25),
            "Other": random.randint(5, 15),
        }
    }


def generate_grc_data():
    categories = ["Access Control", "Network", "Endpoints", "Logging", "IR", "Data"]
    scores = [random.randint(55, 100) for _ in categories]
    risks = {
        "Critical": random.randint(0, 3),
        "High": random.randint(2, 8),
        "Medium": random.randint(5, 15),
        "Low": random.randint(10, 25),
    }
    return {"categories": categories, "scores": scores, "risks": risks}


def build_report(date_str, soc, grc):
    labels = soc["labels"]

    total_alerts = sum(soc["alerts_total"])
    high_alerts = sum(soc["alerts_high"])
    closed = sum(soc["incidents_closed"])
    fp = sum(soc["false_positives"])
    avg_compliance = round(sum(grc["scores"]) / len(grc["scores"]))
    total_risks = sum(grc["risks"].values())
    critical_risks = grc["risks"]["Critical"]

    bar_alerts = make_bar_chart("Total Alerts per Day", labels, soc["alerts_total"], "Alerts")
    line_high = make_line_chart("High Severity Alerts", labels, soc["alerts_high"], "Alerts")
    bar_logs = make_bar_chart("Log Volume per Day (thousands)", labels, soc["log_volume_k"], "Log entries (k)")
    pie_types = make_pie_chart(
        "Alert Type Breakdown",
        list(soc["alert_types"].keys()),
        list(soc["alert_types"].values())
    )
    bar_compliance = make_bar_chart(
        "Compliance Score by Category",
        grc["categories"],
        grc["scores"],
        "Score (0-100)"
    )
    pie_risks = make_pie_chart(
        "Open Risks by Severity",
        list(grc["risks"].keys()),
        list(grc["risks"].values())
    )

    report = """# Security Report — {date}

This report is auto-generated as part of the SOC & GRC project. It covers the last 7 days of simulated security activity.

---

## Quick summary

| Area | Value |
|------|-------|
| Total alerts (7 days) | {total_alerts} |
| High severity alerts | {high_alerts} |
| Incidents closed | {closed} |
| False positives | {fp} |
| Avg compliance score | {avg_compliance}% |
| Open risks | {total_risks} |
| Critical risks | {critical_risks} |

---

## SOC — Alerts and Activity

### Total alerts per day

{bar_alerts}

### High severity alerts

{line_high}

### Log volume per day

{bar_logs}

### Alert breakdown by type

{pie_types}

---

## GRC — Compliance and Risk

### Compliance score by category

Scores are based on a self-assessment against the compliance checklist. 100 means all controls are in place.

{bar_compliance}

### Open risks by severity

{pie_risks}

---

## Notes

This data is simulated for demonstration purposes. In a real environment these numbers would come from a SIEM or log aggregation tool.

The compliance scores are updated each run to reflect a changing environment. A drop in score should trigger a review of that control area.
""".format(
        date=date_str,
        total_alerts=total_alerts,
        high_alerts=high_alerts,
        closed=closed,
        fp=fp,
        avg_compliance=avg_compliance,
        total_risks=total_risks,
        critical_risks=critical_risks,
        bar_alerts=bar_alerts,
        line_high=line_high,
        bar_logs=bar_logs,
        pie_types=pie_types,
        bar_compliance=bar_compliance,
        pie_risks=pie_risks,
    )
    return report


def main():
    today = datetime.today().strftime("%Y-%m-%d")
    soc = generate_soc_data(days=7)
    grc = generate_grc_data()
    report = build_report(today, soc, grc)

    output_dir = os.path.join("reports", today)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "README.md")

    with open(output_path, "w") as f:
        f.write(report)

    print("Report written to " + output_path)

    index_path = os.path.join("reports", "README.md")
    existing = []
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            existing = f.readlines()

    entry = "- [" + today + "](./" + today + "/README.md)\n"
    if entry not in existing:
        existing.append(entry)

    entries = sorted([l for l in existing if l.startswith("- [")], reverse=True)

    with open(index_path, "w") as f:
        f.write("# All Reports\n\n")
        f.writelines(entries)

    print("Index updated.")


if __name__ == "__main__":
    main()
