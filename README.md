# 🎨 WorkMood Studio

> Turn Microsoft 365 work communication into visual mood boards with AI

WorkMood Studio is an AI-powered creative app that analyzes emails and meeting transcripts to detect emotional context (stress, urgency, confidence) and translates those signals into a visual mood board. Built for **Agents League Hackathon 2026** – Creative Apps track with **Microsoft Work IQ**.

---

## 📌 Table of Contents
- [Problem Statement](#problem-statement)
- [Target Users](#target-users)
- [Solution](#solution)
- [Demo Flow (MVP)](#demo-flow-mvp)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Setup & Installation](#setup--installation)
- [Environment Variables](#environment-variables)
- [Running the App](#running-the-app)
- [Project Structure](#project-structure)
- [Work IQ Integration](#work-iq-integration)
- [Security](#security)
- [Submission Checklist](#submission-checklist)
- [Team](#team)
- [License](#license)

---

## ❓ Problem Statement

In many projects, the real emotional context in emails and meetings (especially stress/urgency) **never makes it into the creative brief**. As a result:

- Designers start with incomplete context
- Tone misalignment causes endless revisions
- Work "doesn't feel right" for the moment

---

## 👥 Target Users

- **Designers** – need quick tone alignment at kickoff
- **Creative Directors** – need visual direction from stakeholder communication
- **Remote Teams** – need to make emotional context visible

---

## 💡 Solution

WorkMood Studio ingests Microsoft 365 Work IQ data (meeting transcripts + email threads) and:

1. Extracts **mood keywords** and **sentiment signals** (stress, urgency, confidence, calm)
2. Generates a **mood board** with:
   - Mood keywords
   - Color palette (hex codes)
   - Image/style directions (photography/illustration, lighting, texture)
3. Allows **tone refinement** (calm ↔ urgent, playful ↔ serious)
4. **Exports** mood board as PNG/PDF

---

## 🎬 Demo Flow (MVP)
