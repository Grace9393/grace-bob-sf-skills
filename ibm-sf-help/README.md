# IBM Salesforce Help Skill

This skill provides access to Salesforce Help Center documentation through a local SQLite database.

## Quick Start

### Download the Database

The Salesforce Help database (`docs.sqlite`) is not stored in this repository due to its size.

**Download it here:** https://ibm.box.com/s/t0y8c3km19y55nz29n4tv9kb932wvc4t

Place the downloaded `docs.sqlite` file in this directory (`skills/ibm-sf-help/`).

### Verify Installation

Once downloaded, verify the database is working:

```bash
cd skills/ibm-sf-help
sqlite3 -readonly docs.sqlite "SELECT COUNT(*) FROM help_articles_fts;"
```

You should see a count of articles in the database.

## Rebuilding the Database

If you need to rebuild the database from scratch (e.g., to get the latest Salesforce Help content), see the instructions in `src/README.md`.
