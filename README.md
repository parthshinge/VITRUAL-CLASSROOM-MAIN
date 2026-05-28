# AWS-hosted Virtual Classroom and Learning Platform

## Project Overview

This project is a **cloud-native virtual classroom** web application built using the Flask framework and hosted on AWS. It demonstrates the integration of core AWS services (EC2, S3, and RDS) to provide a secure, scalable, and responsive platform for digital learning.

Students can register, log in, and access course materials, while administrators can upload and manage content. The project emphasizes modern cloud deployment practices and full-stack development.

---

## Folder Structure

```
AWS-hosted-Virtual-Classroom-and-Learning-Platform/
├── Documentation/
│   └── Final document.pdf
├── static/
├── templates/
│   ├── content.html
│   ├── home.html
│   ├── login.html
│   └── register.html
├── app.py
├── README.md
├── requirements.txt
└── tempCodeRunnerFile.py
```

---

## Technologies Used

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Database:** MySQL (AWS RDS)  
- **Cloud Services:** AWS EC2, S3, RDS  
- **Other Tools:** Git & GitHub, MySQL Workbench, boto3

---

## Screen Shots

### Home Page:
![Home Page](https://drive.google.com/uc?export=view&id=1sBl4w-NyDVD9nvIy2aV10P1J9HCEyS1l)

### Registration Page:
![Registration Page](https://drive.google.com/uc?export=view&id=16kp8Leto7fludFmGJny8gs14olkp8QS_)

### Login Page:
![Login Page](https://drive.google.com/uc?export=view&id=1F2yvH4nqio_dg8v8D1vc1Q8sknttmOb9)

### Content Page:
![Content Page](https://drive.google.com/uc?export=view&id=1r4wsKWqOZUvhrvEG2axeuZrGIdHhnYtO)


---

## System Architecture

1. **Frontend:** HTML/CSS/JS served via Flask templates
2. **Backend:** Flask APIs managing user and file routes
3. **Storage:** PDFs stored in S3
4. **Database:** User and file metadata stored in RDS (MySQL)
5. **Deployment:** Flask app hosted on EC2 

---

## Project Workflow

1. **Create and Configure AWS Services:**
   - AWS Account, S3 Bucket, RDS MySQL, EC2 Instance
2. **Develop Flask App:**
   - Build register/login routes
   - Create templates: `home.html`, `register.html`, `login.html`, `content.html`
   - Connect to S3 using `boto3` and to RDS using `pymysql`
3. **Deploy Application:**
   - SSH into EC2, clone GitHub repo, install dependencies
   - Run Flask app using evelopment server
4. **Push Code to GitHub**

---

## 👨‍🏫 User Scenarios

### Student Registration and Login
- Registers via web form, logs in, accesses course content stored on S3.

### Admin Uploads Content
- Uploads PDFs or videos to S3 with metadata stored in RDS.

### Student Downloads Content
- Clicks a file link to download directly from S3.
  
---

## ✅ Conclusion

This project showcases how web applications can be effectively deployed and scaled using AWS. With Flask at its core and AWS services powering the backend, it provides a modern, secure, and user-friendly experience for online learning platforms.

---

## 🔗 Demo and Source Code

- 🎥 [Demo Video](https://drive.google.com/file/d/1LB_YXHSry8S5PD3ijs0IP8p0HA5zYZA6/view?usp=drive_link)  
- 🧾 [GitHub Repository](https://github.com/parthshinge/VITRUAL-CLASSROOM-MAIN.git)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- AWS Account with access to EC2, S3, and RDS
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/parthshinge/VITRUAL-CLASSROOM-MAIN.git
   cd VITRUAL-CLASSROOM-MAIN
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS credentials:**
   - Set up your AWS credentials in `~/.aws/credentials` or as environment variables
   - Update the AWS configuration in `app.py` with your specific S3 bucket, RDS endpoint, and credentials

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   - Open your browser and navigate to `http://localhost:5000`

### AWS Setup Guide

1. **Create S3 Bucket:**
   - Go to AWS S3 console
   - Create a new bucket for storing course content
   - Configure bucket policy for public read access if needed

2. **Create RDS MySQL Instance:**
   - Go to AWS RDS console
   - Create a MySQL database instance
   - Note the endpoint, username, and password
   - Create the required database schema

3. **Launch EC2 Instance:**
   - Go to AWS EC2 console
   - Launch an instance (Ubuntu/Amazon Linux recommended)
   - Configure security groups to allow HTTP (port 80) and SSH (port 22)
   - SSH into the instance and deploy the application

---

## 📝 Configuration

Update the following in `app.py`:
- S3 bucket name
- RDS database credentials
- AWS region
- Flask secret key

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is open source and available for educational purposes.
