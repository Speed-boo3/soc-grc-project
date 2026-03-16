import json
import argparse
import os
from collections import Counter


def load_logs(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def count_by_type(entries):
    return Counter(e.get("type", "unknown") for e in entries)


def count_suspicious(entries):
    return [e for e in entries if e.get("suspicious")]


def top_ips(entries, n=5):
    ips = [e.get("ip") for e in entries if e.get("ip")]
    return Counter(ips).most_common(n)


def top_status_codes(entries, n=5):
    codes = [e.get("status") for e in entries if e.get("status")]
    return Counter(codes).most_common(n)


def bar(value, max_value, width=30):
    filled = int((value / max_value) * width) if max_value else 0
    return "█" * filled + "░" * (width - filled)


def print_dashboard(entries):
    os.system("clear")
    total = len(entries)
    suspicious = count_suspicious(entries)
    by_type = count_by_type(entries)
    ips = top_ips(entries)
    codes = top_status_codes(entries)

    print("=" * 55)
    print("           SOC LOG DASHBOARD")
    print("=" * 55)
    print(f"\n  Total entries   : {total}")
    print(f"  Suspicious      : {len(suspicious)}  {'⚠' * min(len(suspicious), 5)}")

    print("\n  Log types:")
    max_count = max(by_type.values(), default=1)
    for t, c in by_type.items():
        print(f"    {t:<12} {bar(c, max_count, 20)} {c}")

    if ips:
        print("\n  Top source IPs:")
        max_ip = max(c for _, c in ips)
        for ip, c in ips:
            print(f"    {ip:<18} {bar(c, max_ip, 15)} {c}")

    if codes:
        print("\n  Top HTTP status codes:")
        max_code = max(c for _, c in codes)
        for code, c in codes:
            print(f"    {code:<6} {bar(c, max_code, 15)} {c}")

    if suspicious:
        print("\n  Recent suspicious events:")
        for e in suspicious[-5:]:
            msg = e.get("message") or e.get("request") or e.get("raw", "")
            print(f"    [{e.get('type')}] {msg[:60]}")

    print("\n" + "=" * 55)


def main():
    parser = argparse.ArgumentParser(description="Terminal dashboard for parsed log data")
    parser.add_argument("--logs", required=True, help="Path to parsed JSON log file")
    args = parser.parse_args()

    entries = load_logs(args.logs)
    print_dashboard(entries)


if __name__ == "__main__":
    main()
