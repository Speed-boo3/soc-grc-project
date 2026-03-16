# Incident Response Playbook

This playbook covers the steps to follow when a security incident is detected. It is based on a simplified version of the NIST incident response lifecycle.

---

## The four phases

**1. Preparation**
Make sure monitoring is set up and log collection is running before anything happens. Everyone on the team should know their role.

**2. Detection and Analysis**
When an alert fires, the first job is to figure out if it is a real incident or a false positive.

Questions to ask:
- Which rule triggered the alert?
- What is the source IP or user?
- Has this happened before?
- Is it happening right now or is it historical?

**3. Containment, Eradication, and Recovery**
Once confirmed as a real incident, stop the spread, remove the threat, and bring systems back online.

**4. Post-Incident Activity**
Write a short report and update detection rules if needed.

---

## Playbook: SSH Brute Force

**Trigger:** RULE-001 fires – multiple failed SSH logins from one IP.

Steps:
1. Check the source IP in the logs.
2. Count the number of attempts and the time window.
3. If over 10 attempts in 5 minutes, block the IP at the firewall.
4. Check if any login succeeded after the failed attempts.
5. If a login succeeded, treat this as a full compromise – escalate.
6. If no login succeeded, document the IP and close the incident.
7. Add the IP to the blocklist and update threat intel.

---

## Playbook: Unauthorized Admin Access Attempt

**Trigger:** RULE-005 fires – request to /admin returned 403.

Steps:
1. Check if the IP has made other suspicious requests.
2. Review the user agent string for scanning tools.
3. If it looks like a scanner, block the IP and log it.
4. If it looks like an internal user, follow up with that user directly.

---

## Playbook: Segfault / Application Crash

**Trigger:** RULE-006 fires – kernel segfault detected.

Steps:
1. Identify which process crashed.
2. Check if the crash was triggered by a network request.
3. Pull core dump if available.
4. Check if the crash is repeatable – could indicate exploitation attempt.
5. Notify the system owner.

---

## Severity levels

| Level  | Description                              | Response time |
|--------|------------------------------------------|---------------|
| Low    | Informational, no immediate risk         | 24 hours      |
| Medium | Possible threat, needs investigation     | 4 hours       |
| High   | Active threat or confirmed breach        | 30 minutes    |

---

## Contacts

| Role              | Contact method        |
|-------------------|-----------------------|
| SOC Lead          | Internal Slack #soc   |
| System Owner      | Email                 |
| Management        | Phone (high only)     |
