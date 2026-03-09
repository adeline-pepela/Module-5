# Telecom Churn Prediction Deployment System

A production-ready, **database-driven** machine learning deployment for predicting customer churn in the telecommunication industry using FastAPI backend, SQLAlchemy ORM, and modern web frontend.

## 🎯 Key Features

### ✅ Dynamic Database System (NEW)
- **Real Data**: Loads 8,453 customers from GitHub CSV into SQLite/PostgreSQL
- **Live Predictions**: All predictions saved to database with timestamps
- **Intervention Tracking**: Track retention campaigns and outcomes
- **Model Governance**: Version control, performance monitoring, audit trails

### Executive Dashboard
- **KPI Cards**: Real-time metrics for total customers, churn rate, at-risk customers, revenue at risk, prevention rate, and campaign efficiency
- **Trend Visualizations**: Monthly churn trends, risk distribution, and segment analysis
- **Dynamic Updates**: Auto-refreshing dashboards with live data

### Risk Segmentation Panel
- **Customer Risk Buckets**: Ultra High (>80%), High (60-80%), Medium (40-60%), Low (<40%)
- **Advanced Filters**: Filter by segment (SOHO/SME/VSE), revenue range, account manager, geography, and risk level
- **Actionable Insights**: Prioritized customer lists for retention teams

### Customer Detail View
- **Comprehensive Profile**: Customer ID, segment, revenue, ARPU, subscriber counts, risk score
- **Explainability**: Top 3 churn drivers with SHAP-based feature importance
- **Trust Building**: Transparent model predictions with clear reasoning

### Real-Time Prediction
- **Single Customer Scoring**: Instant churn probability calculation
- **Batch Processing**: CSV upload for bulk predictions
- **Risk Assessment**: Automatic risk level assignment with recommended actions

### Model Monitoring
- **Performance Tracking**: F1 score, recall, precision, PR-AUC metrics
- **Drift Detection**: Automated alerts for data/model drift
- **Governance**: Model version, retrain dates, feature counts, sampling strategy

## 📁 Project Structure

```
deployment/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── dashboard.py      # Dashboard endpoints
│   │   │   ├── prediction.py     # Prediction endpoints
│   │   │   └── monitoring.py     # Monitoring endpoints
│   │   ├── models/
│   │   │   └── schemas.py        # Pydantic models
│   │   ├── services/
│   │   │   └── predictor.py      # ML model service
│   │   └── __init__.py
│   └── main.py                   # FastAPI application
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css        # Styling
│   │   └── js/
│   │       └── app.js            # Frontend logic
│   └── templates/
│       └── index.html            # Main dashboard
├── data/                         # Data storage
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Quick Start (Database Setup)

### Option 1: Automated Setup (Recommended)
```bash
cd deployment
python setup_database.py
```

This will:
1. Install all dependencies
2. Create database and load 8,453 customers from CSV
3. Generate predictions for all customers
4. Initialize model metrics

### Option 2: Manual Setup

1. **Install dependencies**
```bash
cd deployment/backend
pip install -r requirements.txt
```

2. **Load customer data**
```bash
cd app
python -m database.load_data
```

3. **Generate predictions**
```bash
python -m database.generate_predictions
```

4. **Start server**
```bash
cd ..
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

5. **Access dashboard**
```
http://localhost:8000
```

## 📊 Database Schema

### Tables

**customers** - Master customer data (8,453 records)
- PID, segment, revenue, ARPU, subscribers, churn status
- Loaded from: https://raw.githubusercontent.com/adeline-pepela/Dissertation/main/data/dataset.csv

**predictions** - ML predictions with timestamps
- churn_probability, risk_level, top_drivers, model_version
- Automatically generated for all customers

**interventions** - Retention action tracking
- assigned_manager, intervention_type, customer_response, retention_outcome
- Supports A/B testing and ROI measurement

**model_metrics** - Performance monitoring
- f1_score, recall, precision, training_date, is_active
- Current: F1=0.1286, Recall=0.3818, Precision=0.0773

## 🚀 Installation (Legacy)

### Prerequisites
- Python 3.8+
- pip package manager
- Trained ML model file (best_model.pkl)

### Setup Steps

1. **Clone the repository**
```bash
cd deployment
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Copy your trained model**
```bash
# Place your best_model.pkl in the models directory
cp ../models/best_model.pkl ./models/
```

5. **Run the application**
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

6. **Access the dashboard**
```
Open browser: http://localhost:8000
```

## 📊 API Documentation (Database-Driven)

### Dashboard Endpoints (Dynamic Data)

#### Get Dashboard Metrics (From Database)
```http
GET /api/dashboard/metrics
```
Returns:
- Total customers (live count)
- Churn rate (calculated from actual data)
- At-risk customers (from predictions table)
- Revenue at risk (aggregated from customer revenue)
- Prevention rate (from model_metrics)
- Campaign efficiency (from model_metrics)

#### Get At-Risk Customers (Filtered Query)
```http
GET /api/dashboard/customers/at-risk?risk_level=High&segment=SME&limit=100
```
Filters:
- risk_level: Ultra High, High, Medium, Low
- segment: SOHO, SME, VSE
- limit: Max results

Returns customers with predictions from database

#### Get Customer Detail (With Predictions)
```http
GET /api/dashboard/customer/{customer_id}
```
Returns:
- Customer profile from database
- Latest prediction with top drivers
- Intervention history

### Intervention Endpoints (NEW)

#### Create Intervention
```http
POST /api/interventions
Content-Type: application/json

{
  "customer_id": "PID123",
  "assigned_manager": "John Doe",
  "intervention_type": "Personalized Offer",
  "offer_type": "20% Discount",
  "notes": "High-value customer retention"
}
```

#### Update Intervention Outcome
```http
PUT /api/interventions/{intervention_id}
Content-Type: application/json

{
  "customer_response": "Accepted",
  "retention_outcome": "Retained",
  "notes": "Customer renewed contract"
}
```

#### Get Customer Interventions
```http
GET /api/interventions/{customer_id}
```
Returns all interventions for a customer

### Prediction Endpoints (Saves to Database)

#### Single Customer Prediction
```http
POST /api/prediction/predict
Content-Type: application/json

{
  "customer_id": "CUST1001",
  "segment": "SME",
  "active_subscribers": 50,
  "suspended_subscribers": 5,
  "total_subscribers": 55,
  "arpu": 15000,
  "average_mobile_revenue": 750000,
  "average_fix_revenue": 75000
}
```

#### Batch Prediction
```http
POST /api/prediction/predict-batch
Content-Type: multipart/form-data

file: customers.csv
```

### Monitoring Endpoints

#### Get Model Metrics
```http
GET /api/monitoring/model-metrics
```
Returns current model performance metrics

#### Get Performance Trend
```http
GET /api/monitoring/performance-trend?months=6
```
Returns historical performance data

## 🎨 Frontend Usage

### Navigation
- **Dashboard**: Executive KPIs and trends
- **Risk Analysis**: Customer segmentation and filtering
- **Prediction**: Real-time and batch scoring
- **Monitoring**: Model performance tracking

### Making Predictions

1. Navigate to **Prediction** tab
2. Fill in customer details
3. Click **Predict Churn**
4. View results with:
   - Churn probability
   - Risk level
   - Top churn drivers
   - Recommended action

### Batch Processing

1. Prepare CSV file with columns:
   - customer_id, segment, active_subscribers, suspended_subscribers, total_subscribers, arpu, average_mobile_revenue, average_fix_revenue
2. Upload file in **Batch Prediction** section
3. Download results as CSV

## 🔧 Configuration

### Database Configuration

**SQLite (Default)**
```python
DATABASE_URL = "sqlite:///./churn_prediction.db"
```

**PostgreSQL (Production)**
```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/churn_db"
```

### Data Source
```python
CSV_URL = "https://raw.githubusercontent.com/adeline-pepela/Dissertation/main/data/dataset.csv"
```

### Model Path
Update model path in `backend/app/services/predictor.py`:
```python
def __init__(self, model_path: str = "../models/best_model.pkl"):
```

### Feature Names
Ensure feature names match your training pipeline in `predictor.py`:
```python
def _get_feature_names(self) -> List[str]:
    return [
        'Active subscribers', 'Not Active subscribers', ...
    ]
```

### API Base URL
Update in `frontend/static/js/app.js` if deploying to different host:
```javascript
const API_BASE = '/api';
```

## 📈 Data Flow

1. **CSV → Database**: `load_data.py` imports 8,453 customers
2. **Prediction → Database**: Each prediction saved with timestamp and drivers
3. **Dashboard → Database**: Real-time queries for metrics and customer lists
4. **Intervention → Database**: Track retention campaigns and measure ROI

## 🎯 Use Cases

### 1. Executive Dashboard
- View real-time churn metrics from database
- Monitor revenue at risk by segment
- Track model performance over time

### 2. Retention Team
- Filter high-risk customers by segment/manager
- Create intervention campaigns
- Track customer responses and outcomes

### 3. Data Science Team
- Monitor model drift
- Compare model versions
- Analyze feature importance trends

### 4. Business Intelligence
- Export prediction data for reporting
- Calculate campaign ROI
- Segment analysis and trends

## 📈 Model Performance

- **F1 Score**: 0.1286
- **Recall**: 0.3818 (38.18% Churn Prevention Rate)
- **Precision**: 0.0773
- **ROC-AUC**: 0.5510
- **PR-AUC**: 0.0786
- **Sampling Strategy**: SVMSMOTE
- **Features**: 22 (3 categorical + 19 numerical)

## 🔒 Security & Production

### Database Security
- Use PostgreSQL with SSL in production
- Implement row-level security
- Regular backups: `sqlite3 churn_prediction.db ".backup backup.db"`

### API Security

- Implement authentication/authorization for production
- Add rate limiting to API endpoints
- Validate and sanitize all inputs
- Use HTTPS in production
- Implement CORS properly for specific origins
- Add logging and monitoring

## 🚢 Production Deployment

### Database Migration
```bash
# Upgrade to PostgreSQL
export DATABASE_URL="postgresql://user:pass@host:5432/churn_db"
pip install psycopg2-binary
python -m database.load_data
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables
```bash
DATABASE_URL=postgresql://user:pass@host:5432/churn_db
MODEL_PATH=/app/models/best_model.pkl
API_HOST=0.0.0.0
API_PORT=8000
LOG_LEVEL=info
```

## 📚 Additional Documentation

- **DATABASE_GUIDE.md**: Comprehensive database setup and usage
- **ARCHITECTURE.md**: System architecture and design
- **QUICKSTART.md**: Quick start guide

## 🛠️ Maintenance

### Backup Database
```bash
sqlite3 churn_prediction.db ".backup backup_$(date +%Y%m%d).db"
```

### Update Model Metrics
```python
from app.database.models import ModelMetrics
metrics = db.query(ModelMetrics).filter_by(is_active=True).first()
metrics.f1_score = 0.15
db.commit()
```

### Clear Old Predictions
```python
from datetime import datetime, timedelta
old_date = datetime.utcnow() - timedelta(days=90)
db.query(Prediction).filter(Prediction.predicted_at < old_date).delete()
db.commit()
```

## 🐛 Troubleshooting

### Database Issues
- **Database locked**: Close other connections, use WAL mode
- **Missing data**: Run `python -m database.load_data` again
- **Slow queries**: Add indexes on frequently queried columns

### Prediction Issues
- **No predictions**: Run `python -m database.generate_predictions`
- **Model errors**: Check model file path and sklearn version
- **Feature mismatch**: Verify feature names match training data

## 📞 Support

For issues:
1. Check DATABASE_GUIDE.md
2. Verify CSV data accessibility
3. Review API docs at http://localhost:8000/docs
4. Check database logs

## 🎓 Project Context

**Course**: DSA 8502 Predictive and Optimization Analytics  
**Institution**: Strathmore University  
**Dataset**: 8,453 telecom business customers (24-month period)  
**Data Source**: https://raw.githubusercontent.com/adeline-pepela/Dissertation/main/data/dataset.csv

### Research Objectives
1. Apply ML techniques for churn prediction
2. Compare multiple algorithms (Logistic Regression, Random Forest, Gradient Boosting, EasyEnsemble)
3. Identify influential features for retention strategies
4. Demonstrate proactive decision-making framework

### Hypothesis
**H₁**: Customer behavior, demographics, and service patterns can effectively predict churn using ML models

## 📝 License

This project is part of the DSA 8502 Predictive and Optimization Analytics course.

## 👥 Author

**Adeline Makokha**  
Adm No: 191199  
Course: DSA 8502 Predictive and Optimization Analytics

## 🤝 Contributing

For improvements or bug fixes, please create an issue or pull request.

## 📞 Support

For questions or support, contact the development team.
