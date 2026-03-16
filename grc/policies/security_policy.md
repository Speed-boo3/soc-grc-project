# Information Security Policy

**Version:** 1.0  
**Last updated:** March 2024  
**Owner:** Security Team

---

## Purpose

This policy sets out the basic rules for keeping our systems and data secure. It applies to everyone who uses company systems, including employees, contractors, and students working on lab environments.

---

## Access Control

Accounts should only have access to what they need to do their job. Admin access should be given out sparingly and reviewed every three months.

Everyone should use a unique password for each account. Passwords should be at least 12 characters and not reused. Multi-factor authentication is required for any remote access.

Accounts that have not been used in 90 days should be disabled.

---

## Logging and Monitoring

All servers and network devices should send logs to a central location. Logs should be kept for at least 90 days.

The SOC team is responsible for reviewing alerts daily. Any alert rated "high" or above must be investigated within 30 minutes.

---

## Patch Management

Security patches rated critical must be applied within 7 days of release. Other patches should be applied within 30 days. Patch status should be tracked and reported monthly.

---

## Incident Response

All security incidents must be reported to the SOC team immediately. The team will follow the incident response playbook located in `soc/incident-response/playbook.md`.

A post-incident report must be written for all high and critical incidents within 5 business days.

---

## Data Handling

Sensitive data must be encrypted at rest and in transit. Sensitive data should not be stored on personal devices.

Data that is no longer needed should be securely deleted following the retention schedule.

---

## Physical Security

Workstations must be locked when unattended. Visitors must be escorted in secure areas. Clean desk policy applies – no sensitive documents left on desks overnight.

---

## Exceptions

Any exception to this policy must be documented and approved by the security team. Exceptions are reviewed every 6 months.

---

## Enforcement

Violations of this policy may result in disciplinary action. The security team has the right to monitor systems for compliance.
