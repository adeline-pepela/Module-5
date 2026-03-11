# 🪟 Windows Deployment Guide

## Complete Guide for Running on Windows

---

## 📋 Prerequisites

### 1. Install Docker Desktop for Windows

**Download:**
- Go to: https://docs.docker.com/desktop/install/windows-install/
- Download Docker Desktop for Windows
- Run the installer

**System Requirements:**
- Windows 10 64-bit: Pro, Enterprise, or Education (Build 19041 or higher)
- OR Windows 11 64-bit
- WSL 2 feature enabled
- 4GB RAM minimum

**Installation Steps:**
1. Double-click `Docker Desktop Installer.exe`
2. Follow installation wizard
3. Restart computer when prompted
4. Start Docker Desktop from Start menu
5. Wait for Docker to start (whale icon in system tray)

**Verify Installation:**
```cmd
docker --version
docker-compose --version
```

### 2. Install Git for Windows (if not installed)

**Download:**
- Go to: https://git-scm.com/download/win
- Download and install

**Verify:**
```cmd
git --version
```

---

## 🚀 Method 1: One-Command Deployment (Easiest)

### Step 1: Open Command Prompt or PowerShell
- Press `Win + R`
- Type `cmd` or `powershell`
- Press Enter

### Step 2: Clone Repository
```cmd
git clone https://github.com/adeline-pepela/Module-5.git
cd "Module-5\Predictive and Optimization Analytics\POA-Project\Churn-main\deployment"
```

### Step 3: Run Deployment Script
```cmd
scripts\deploy.bat
```

**That's it!** The script will:
- ✅ Check Docker installation
- ✅ Build the container
- ✅ Start the application
- ✅ Initialize database
- ✅ Open in browser

### Step 4: Access Application
The script will automatically open your browser, or manually go to:
```
http://localhost:8000
```

---

## 🔧 Method 2: Manual Docker Deployment

### Step 1: Clone Repository
```cmd
git clone https://github.com/adeline-pepela/Module-5.git
cd "Module-5\Predictive and Optimization Analytics\POA-Project\Churn-main\deployment"
```

### Step 2: Build Docker Image
```cmd
docker-compose build
```
*This takes 5-10 minutes on first run*

### Step 3: Start Application
```cmd
docker-compose up -d
```

### Step 4: Verify Running
```cmd
docker ps
```
You should see `churn-prediction-app` running

### Step 5: Access Application
Open browser and go to:
```
http://localhost:8000
```

---

## 🐍 Method 3: Manual Python Setup (Without Docker)

### Prerequisites
- Python 3.8 or higher
- pip

### Step 1: Clone Repository
```cmd
git clone https://github.com/adeline-pepela/Module-5.git
cd "Module-5\Predictive and Optimization Analytics\POA-Project\Churn-main\deployment"
```

### Step 2: Create Virtual Environment
```cmd
python -m venv venv
```

### Step 3: Activate Virtual Environment
```cmd
venv\Scripts\activate
```
*Your prompt should now show (venv)*

### Step 4: Install Dependencies
```cmd
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Setup Database
```cmd
cd backend

python -c "from app.database.database import engine, Base; from app.database.models import *; Base.metadata.create_all(bind=engine); print('Tables created')"

python -m app.database.load_data
python -m app.database.generate_predictions
python -m app.database.save_model_comparison
python -m app.database.save_feature_importance
```

### Step 6: Start Application
```cmd
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Step 7: Access Application
Open browser:
```
http://localhost:8000
```

---

## 🔍 Verification

### Check if Application is Running

**Using Browser:**
Go to: http://localhost:8000

**Using Command Prompt:**
```cmd
curl http://localhost:8000/api/dashboard/metrics
```

**Expected Response:**
```json
{
  "total_customers": 8436,
  "current_churn_rate": 0.0646,
  "predicted_at_risk": 7,
  "revenue_at_risk": 1224.34
}
```

---

## 🛠️ Useful Commands (Windows)

### Docker Commands

**View Running Containers:**
```cmd
docker ps
```

**View Logs:**
```cmd
docker logs -f churn-prediction-app
```

**Stop Application:**
```cmd
docker-compose down
```

**Restart Application:**
```cmd
docker-compose restart
```

**Rebuild and Restart:**
```cmd
docker-compose up -d --build
```

**Check Container Stats:**
```cmd
docker stats churn-prediction-app
```

### Python Commands (Manual Setup)

**Activate Virtual Environment:**
```cmd
venv\Scripts\activate
```

**Deactivate Virtual Environment:**
```cmd
deactivate
```

**Stop Application:**
Press `Ctrl + C` in the terminal

---

## 🆘 Troubleshooting

### Issue 1: Docker Desktop Not Starting

**Solution:**
1. Open Docker Desktop from Start menu
2. Wait for whale icon in system tray
3. Right-click whale icon → Check if "Docker Desktop is running"
4. If not, restart Docker Desktop

### Issue 2: WSL 2 Not Installed

**Error Message:**
```
WSL 2 installation is incomplete
```

**Solution:**
1. Open PowerShell as Administrator
2. Run:
```powershell
wsl --install
```
3. Restart computer
4. Start Docker Desktop again

### Issue 3: Port 8000 Already in Use

**Find Process Using Port:**
```cmd
netstat -ano | findstr :8000
```

**Kill Process:**
```cmd
taskkill /PID <PID_NUMBER> /F
```

**Or Change Port:**
Edit `docker-compose.yml`:
```yaml
ports:
  - "9000:8000"  # Use port 9000 instead
```

### Issue 4: Docker Build Fails

**Solution:**
```cmd
docker-compose down -v
docker system prune -a
docker-compose build --no-cache
docker-compose up -d
```

### Issue 5: Python Not Found

**Solution:**
1. Download Python from: https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart Command Prompt
4. Verify: `python --version`

### Issue 6: Permission Denied

**Solution:**
Run Command Prompt or PowerShell as Administrator:
1. Right-click on Command Prompt/PowerShell
2. Select "Run as administrator"

### Issue 7: Git Not Found

**Solution:**
1. Download Git from: https://git-scm.com/download/win
2. Install with default settings
3. Restart Command Prompt
4. Verify: `git --version`

---

## 📱 Access from Other Devices

### Find Your Windows IP Address
```cmd
ipconfig
```
Look for "IPv4 Address" under your active network adapter

### Access from Another Device
Replace `YOUR_IP` with your Windows IP:
```
http://YOUR_IP:8000
```

Example:
```
http://192.168.1.100:8000
```

---

## 🎯 Quick Reference

### Fastest Method (Recommended)
```cmd
# 1. Clone
git clone https://github.com/adeline-pepela/Module-5.git

# 2. Navigate
cd "Module-5\Predictive and Optimization Analytics\POA-Project\Churn-main\deployment"

# 3. Deploy
scripts\deploy.bat

# 4. Access
# Browser opens automatically or go to: http://localhost:8000
```

### Stop Application
```cmd
docker-compose down
```

### Restart Application
```cmd
docker-compose restart
```

### View Logs
```cmd
docker logs -f churn-prediction-app
```

---

## 📊 What You'll See

### Dashboard Features
- 6 KPI cards
- 4 risk buckets
- 4 interactive charts
- 7 navigation pages

### Pages
1. Overview - Dashboard with metrics
2. Customers - Search and filter 8,436 customers
3. Risk Analysis - Risk distribution
4. Predict - Single and bulk predictions
5. Interventions - Retention campaigns
6. Model Governance - Model tracking
7. Model Evaluation - Performance metrics

---

## 💡 Tips for Windows Users

1. **Use PowerShell** - More features than Command Prompt
2. **Run as Administrator** - Avoids permission issues
3. **Keep Docker Desktop Running** - Required for containers
4. **Check Firewall** - May need to allow Docker
5. **Use WSL 2** - Better performance than Hyper-V
6. **Close Antivirus Temporarily** - If build fails

---

## 📞 Need Help?

### Check Status
```cmd
docker ps
docker logs churn-prediction-app
```

### Test API
```cmd
curl http://localhost:8000/api/dashboard/metrics
```

### Restart Everything
```cmd
docker-compose down
docker-compose up -d
```

---

## ✅ Success Checklist

- [ ] Docker Desktop installed and running
- [ ] Git installed
- [ ] Repository cloned
- [ ] Deployment script executed
- [ ] Container running (docker ps)
- [ ] Application accessible (http://localhost:8000)
- [ ] API responding (test endpoint)
- [ ] Dashboard loading

---

## 🎉 You're Done!

Your application should now be running at:
**http://localhost:8000**

**Time to Deploy:** 5-10 minutes  
**Prerequisites:** Docker Desktop + Git

---

**For Questions:**
- Check logs: `docker logs churn-prediction-app`
- View documentation: `deployment\docs\`
- Test API: http://localhost:8000/docs

**Author:** Adeline Makokha  
**Adm No:** 191199  
**Course:** DSA 8502 Predictive and Optimization Analytics
