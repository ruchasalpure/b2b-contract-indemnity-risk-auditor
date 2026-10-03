from crewai import Agent

b2b_contract_indemnity_risk_auditor = Agent(
    role="B2B Contract Indemnity Risk Auditor",
    goal="Deliver high-precision autonomous B2B Contract Indemnity Risk Auditor operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
