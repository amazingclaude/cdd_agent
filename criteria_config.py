# criteria_config.py

RED_FLAG_DEFINITIONS = [
    {
        "id": "BRI_01",
        "scope": "Bribery/Things of Value",
        "name": "Investigations or Allegations of Bribery",
        "short_description": (
            "Any investigation or allegation that the entity, controlling owner "
            "or subsidiary engaged in bribery or corrupt payments."
        ),
        "inclusion_rules": [
            "Allegations or investigations of bribery involving public officials or state-owned entities.",
            "Allegations of commercial bribery or kickbacks to secure or retain business.",
            "Stories where third parties are accused of paying bribes on behalf of the entity."
        ],
        "exclusion_rules": [
            "Abstract discussion of corruption risk in the industry without linking to the entity.",
        ],
        "notes": [
            "Include regardless of how long ago the alleged conduct occurred.",
            "Include even if charges were not filed; record any known outcome of the investigation."
        ],
    },
    {
        "id": "BRI_02",
        "scope": "Bribery/Things of Value",
        "name": "Entity has Provided Things of Value to a Government Official or Organization",
        "short_description": (
            "The entity provided anything of value to government officials, political parties "
            "or state-related organizations, including state university and hospitals."
        ),
        "inclusion_rules": [
            "Payments, gifts, donations or sponsorships directed to government officials or their close associates.",
            "Benefits such as travel, hospitality, jobs, internships for relatives of officials, where linked to business advantage.",
        ],
        "exclusion_rules": [
            "If a source indicates that a thing of value was given with corrupt intent, then report this information as Investigations or Allegations of Bribery instead.",
        ],
        "notes": [
            "if it is clearly a bribery activity, not just donation/sponsorship, use BRI_01 instead.",
        ],
    },
    {
        "id": "CRI_01",
        "scope": "Criminal Behavior",
        "name": "Investigations or Allegations of Criminal Behavior",
        "short_description": (
            "Investigations or allegations that the entity or related persons engaged in criminal conduct "
            "relevant to financial crime or integrity risk."
        ),
        "inclusion_rules": [
            "Investigations, charges or credible allegations of fraud, embezzlement, money laundering or similar offences.",
            "Criminal probes into misconduct occurring in the course of the entity’s business activities.",
        ],
        "exclusion_rules": [
            "Minor, clearly unrelated criminal issues of employees in their purely private life.",
        ],
        "notes": [
            "Include ongoing investigations and historical cases; note final outcomes if known.",
        ],
    },
    {
        "id": "CRI_02",
        "scope": "Criminal Behavior",
        "name": "Investigations or Allegations of Anticompetitive Behavior",
        "short_description": (
            "Investigations or allegations of anti-competitive practices, such as cartels, price-fixing or abuse of dominance."
        ),
        "inclusion_rules": [
            "Regulatory or antitrust investigations into collusion, bid-rigging or market allocation.",
            "Fines or settlements for competition law breaches related to the entity’s business.",
        ],
        "exclusion_rules": [
            "High-level commentary that the market is concentrated, without specific allegation against the entity.",
        ],
        "notes": [
            "Capture both formal enforcement actions and credible media reports of anticompetitive conduct.",
        ],
    },
]
