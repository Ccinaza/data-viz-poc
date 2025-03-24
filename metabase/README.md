# Metabase POC Setup Guide

## Overview

This project is a Proof of Concept (POC) for evaluating Metabase as a BI tool. It includes a PostgreSQL database for Metabase, ClickHouse for data storage, and MailHog for email testing.The goal of this POC is to assess Metabase’s ability to handle:

- Report creation and ease of use
- Data model management and access control
- Data governance features
- Sharing and self-service capabilities
- High availability (multi-node) setups
- Connection to ClickHouse
- User management via SMTP (email invites)

### Prerequisites
Ensure you have the following installed before proceeding:
- Docker and Docker Compose
- Make (for automation)

### Setup Guide

1. Clone the Repository
```bash
git clone https://github.com/Ccinaza/data-viz-poc.git
cd data-viz-poc/metabase
```

2. Configure Environment Variables
```text
Copy the `.env` file to .env and update it with the correct values:
Update the `.env` file to match your SMTP settings and database connection details.
```
3. Start the Services
Run the following command to start all services:
```bash
make start
```
4. Access Metabase
Once running, open the following URL in your browser to set up Metabase: http://localhost:3000

5. Verify Email Sending (SMTP via MailHog)
MailHog is used to simulate email sending. Access it at:
http://localhost:8025


#### ClickHouse Integration

Metabase requires a ClickHouse JDBC driver to connect to ClickHouse. This has been set up using a custom plugin:
- The `plugins` directory contains the ClickHouse driver.
- The `docker-compose.yml` file mounts this plugin for Metabase to use.

6. Verifying ClickHouse Connection

- Navigate to Admin > Databases in Metabase.
- Add a new database connection.
- Select ClickHouse from the list.
- Enter the database credentials specified in the .env file.
- Click Test Connection to confirm it works.

#### Managing Users with SMTP
Metabase allows user invitations via email, which requires an SMTP server.

#### SMTP Configuration
For testing, MailHog can be used as a local SMTP server: 

Access MailHog’s web UI at: http://localhost:8025

This will capture all outgoing emails for debugging.

#### Inviting Users
- Go to Admin > People in Metabase.
- Click Invite User and enter their email.
- The user will receive an invite (captured in MailHog for testing).
- They can accept the invite and set up their account.

#### Stopping the Services
This will stop and remove all running containers.

#### Data Persistence
- The docker-compose.yml file ensures data persistence using Docker volumes.
- Data in ClickHouse and Metabase will be retained across container restarts.

#### Troubleshooting

**Common Issues:**
- Metabase doesn’t start? Check logs: docker logs metabase
- Emails not being sent? Check SMTP settings in .env. If using MailHog, confirm it’s running at http://localhost:8025
- ClickHouse connection fails? Ensure ClickHouse is running: docker ps
- Verify credentials in Admin > Databases

#### Conclusion

This POC validates Metabase’s capability as a BI tool within a Dockerized environment. Users can replicate this setup easily and test various features like user management, ClickHouse integration, and report generation.