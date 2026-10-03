# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
clause-risk-classifier

Checker:
playbook-compliance-checker

## Coordination Protocol
- **Primary Agent**: b2b-contract-indemnity-risk-auditor
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
