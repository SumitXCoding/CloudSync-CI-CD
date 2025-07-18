# 🌩️ CloudSync CI/CD

A GitHub Actions-based CI/CD pipeline that automates deployment from your GitHub repository to an AWS EC2 instance via Amazon S3.

---

## 🚀 Features

- 🔁 Auto-deployment on every push to `main`
- ☁️ Syncs your `deploy/` folder with an S3 bucket
- 🖥️ Pulls from S3 to your EC2 instance
- 🧩 Lightweight, flexible, and scalable

---

## 🛠️ Tech Stack

- **GitHub Actions** – Workflow automation
- **AWS S3** – Temporary storage bridge
- **AWS EC2** – Target deployment server

---

## 🧱 Architecture

This CI/CD pipeline automatically transfers files from your GitHub repo to EC2 via S3 using secure workflows.

```plaintext
                +------------------+
                |  Local Machine   |
                |  (Developer)     |
                +--------+---------+
                         |
                         | 1. git push
                         v
                +------------------+
                |   GitHub Repo    |
                +--------+---------+
                         |
                         | 2. GitHub Actions Triggered
                         v
            +-----------------------------+
            | GitHub Actions Workflow     |
            | (.github/workflows/s3sync)  |
            +-------------+---------------+
                          |
                          | 3. Sync ./deploy/ to S3 Bucket
                          v
               +---------------------+
               |     AWS S3 Bucket   |
               +----------+----------+
                          |
                          | 4. SSH into EC2 & Sync from S3
                          v
               +---------------------+
               |    AWS EC2 Server   |
               | (Deployed Project)  |
               +---------------------+
