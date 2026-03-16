# Security Compliance Checklist

This checklist is loosely based on common controls from ISO 27001 and NIST CSF. It is meant to give a starting point for a basic security review, not a full audit.

---

## Access Management

- [ ] All user accounts are documented and reviewed
- [ ] Admin accounts are separate from regular accounts
- [ ] MFA is enabled for remote access
- [ ] Shared accounts have been removed or disabled
- [ ] Terminated employee accounts are removed within 24 hours
- [ ] Password policy is enforced via technical controls

---

## Network Security

- [ ] Firewall rules are documented and reviewed
- [ ] Unused ports and services are disabled
- [ ] Network is segmented (at minimum, production separated from dev)
- [ ] Remote access uses a VPN or equivalent
- [ ] IDS/IPS is in place and generating alerts

---

## Endpoint Security

- [ ] Antivirus/EDR is installed and updated on all endpoints
- [ ] Full disk encryption is enabled on laptops
- [ ] Software inventory is maintained
- [ ] Patch levels are tracked and reported

---

## Logging and Monitoring

- [ ] Centralized log collection is set up
- [ ] Logs are retained for at least 90 days
- [ ] SOC team reviews alerts daily
- [ ] Log integrity is protected (write-once or SIEM)

---

## Incident Response

- [ ] Incident response plan exists and is documented
- [ ] IR plan has been tested in the last 12 months
- [ ] Staff know how to report an incident
- [ ] Contact list for escalation is up to date

---

## Data Protection

- [ ] Sensitive data is identified and classified
- [ ] Encryption is used for data at rest and in transit
- [ ] Backups are taken regularly and tested
- [ ] Data retention and deletion policy is in place

---

## Physical Security

- [ ] Server rooms are locked and access is logged
- [ ] Clean desk policy is enforced
- [ ] Visitor access is controlled and logged

---

## Awareness and Training

- [ ] All staff have completed security awareness training
- [ ] Phishing simulations are run at least once a year
- [ ] New starters receive security induction

---

## Scoring

Count the boxes checked and divide by the total to get a rough compliance percentage. This is not a substitute for a real audit, but it gives a useful snapshot.
