# Talent-Bridge
Personal Project

All endpoints should start with:
/api/v1

A. Authentication
POST	/auth/register	Register user
POST	/auth/login	Login user

B. Candidate
GET	/candidates/me	View profile
PUT	/candidates/me	Update profile
POST	/candidates/me/cv	Upload CV

C. Company
POST	/companies/me	Create company
GET	/companies/me	View company

D. Jobs
GET	/jobs	Search jobs
GET	/jobs/{id}	View job
POST	/jobs	Create job
PATCH	/jobs/{id}	Update or close job
POST	/jobs/{id}/save	Save job
DELETE	/jobs/{id}/save	Unsave job
GET	/me/saved-jobs	View saved jobs

E. Application
POST	/jobs/{id}/applications	Apply
GET	/me/applications	View applications
POST	/applications/{id}/withdraw	Withdraw
GET	/jobs/{id}/applications	Employer views applicants
PATCH	/applications/{id}/stage	Update application stage
POST	/applications/{id}/notes	Add private note
GET	/applications/{id}/cv	Download CV
GET	/jobs/{id}/funnel	View hiring statistics

F. Administration
PATCH	/admin/companies/{id}	Verify or reject company
DELETE	/admin/jobs/{id}	Remove fraudulent job
GET	/admin/stats	View platform statistics

G. General
GET	/health	Check API health

These endpoint groups are my assignment's required API specification

This are the thing i have install for this part am currently doing:
pip install fastapi uvicorn
pip install sqlalchemy psycopg2-binary
pip install alembic
pip install pydantic-settings
pip install python-jose[cryptography]
pip install pwdlib[argon2]
pip install python-multipart
pip install pytest httpx
pip install email-validator