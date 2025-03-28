# Proof of Concept (POC) Evaluation: LightDash vs. Metabase vs. Superset

1. Introduction

This document evaluates LightDash, Metabase, and Superset as potential data visualization tools for our organization. The evaluation is based on key criteria including access control, sharing and collaboration, data modeling capabilities, self-service features, high availability, and other relevant factors. Each tool was deployed using Docker and Docker Compose for consistency.

After thorough testing of Metabase and Superset, Metabase emerges as the most suitable BI tool for our requirements:

**Strengths:**
- Easiest report creation with intuitive UI
- Simple data modeling and access management
- Robust user invitation and management via SMTP
- Straightforward dashboard sharing
- Strong self-service capabilities for non-technical users
- Seamless ClickHouse integration via third-party driver
- Lightweight and quick to deploy

**Comparative Observations:**
- Superset: More complex, steeper learning curve
- Lightdash: Limited flexibility, less mature

The recommended tool is `metabase` due to the strengths listed above.

**Recommended Next Steps:**
1. Proceed with Metabase implementation
2. Configure ClickHouse connector
3. Set up SMTP for user management
4. Design initial dashboards and user access levels