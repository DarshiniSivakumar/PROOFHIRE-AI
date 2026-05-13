**ProofHire AI – AI-Powered Applicant Tracking System (ATS)**

ProofHire AI is a full-stack Applicant Tracking System that simulates modern recruitment workflows using AI-based evaluation, candidate management, live assessment monitoring, interview scheduling, and recruiter-candidate communication.

**Features**
*AI-Based Candidate Evaluation*
Automated scoring of candidates based on technical performance
Generates hiring recommendations (Highly Recommended / Strong Hire / Not Recommended)
Detects plagiarism risk, AI-generated responses, and malpractice behavior
Produces overall score and authenticity analysis

*Recruiter Dashboard*
Central ATS dashboard for managing hiring pipeline
-Displays:
Total candidates
Active assessments
Completed evaluations
Shortlisted and rejected candidates
High-risk candidates
Fully dynamic and backend-driven data flow
Real-time pipeline tracking (Not Attended → Attending → Evaluated → Decision)

*Candidate Management*
Add single candidates via recruiter dashboard
Bulk upload multiple candidates at once
-Candidate details include:
Name, Email, Role
Experience level
Assessment type
All modules use centralized candidate_id for consistency

*Live Assessment & Monitoring*
Simulated real-time candidate assessment system
Tracks:
Tab switching and clipboard activity
Session status updates
Malpractice events (mocked MVP logic)
Recruiter live monitoring panel for ongoing assessments

*Interview Scheduling System*
Recruiters can schedule interviews from candidate profiles
Stores:
Candidate reference (candidate_id)
Date & time
Mode (Online/Offline)
Notes
Supports interview lifecycle tracking

*Messaging System*
Recruiter ↔ Candidate communication module
Conversations linked via candidate_id
Displays candidate name, role, and latest message preview

**Tech Stack**
Frontend: React (Vite), Tailwind CSS, Axios, React Router
Backend: FastAPI (Python), Pydantic, REST APIs, in-memory session management (MVP)

**System Architecture**
React Frontend → FastAPI Backend → AI Evaluation Engine → Session Manager → Database

**Modules**
Recruiter Dashboard
Candidate Pipeline
Candidate Profiles
Live Assessments
Interview Scheduling
Messaging System
Bulk Upload System

**Limitations (MVP)**
No authentication system
WebSocket replaced with polling/in-memory logic
Webcam monitoring is simulated
SQLite used instead of production database

**Summary**
ProofHire AI is a simulation of an enterprise ATS system that integrates AI-based evaluation, recruitment workflow automation, live assessment tracking, and interview management into a unified platform.
