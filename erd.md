Simple Entity-Relationship diagram

Member (1) ----< Interaction >---- (1) Campaign

Member
- id (PK)
- name
- email

Campaign
- id (PK)
- name
- description

Interaction
- id (PK)
- member_id (FK)
- campaign_id (FK)
- date
- notes

