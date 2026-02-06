# Customer Churn Prediction for Telecommunication Industries

## Application of Machine Learning Techniques in Customer Churn Prediction

**Author:** Adeline Makokha  
**Adm No:** 191199  
**Course:** DSA 8301 Dissertation

---

## 📊 Project Overview

This research project develops advanced machine learning models to predict customer churn in the telecommunication industry, addressing the critical business challenge of customer retention through data-driven approaches.

### 🎯 Research Objectives
- Apply multiple ML algorithms for churn prediction
- Address class imbalance in telecom churn data
- Optimize model performance through advanced techniques
- Provide actionable business insights for customer retention

## 🔬 Methodology

### Data
- **Dataset:** Safaricom PLC customer data (8,453 records)
- **Features:** 14 variables including demographics, usage patterns, and revenue metrics
- **Target:** Binary churn classification (6.49% churn rate)

### Models Implemented
1. **Basic Models:** Logistic Regression, Decision Trees, Random Forest, SVM, Naive Bayes, KNN
2. **Advanced Models:** XGBoost, LightGBM, CatBoost, Deep Learning
3. **Ensemble Methods:** Voting Classifiers, Stacking, EasyEnsemble
4. **Imbalanced Learning:** SMOTE, ADASYN, Cost-sensitive learning

### Key Techniques
- **Class Balancing:** SMOTE, ADASYN, BorderlineSMOTE
- **Feature Engineering:** Revenue ratios, interaction terms, log transformations
- **Threshold Optimization:** F1-score and cost-sensitive thresholds
- **Hyperparameter Tuning:** Grid search with cross-validation

## 📁 Repository Structure

```
Dissertation/
├── README.md                           # Project documentation
├── data/
│   └── dataset.csv                     # Customer churn dataset
├── notebook/
│   └── Adeline Makokha Dissertation Seminar 3.ipynb  # Research presentation
├── visuals/                            # Generated plots and results
│   ├── *.png                          # Visualization files
│   ├── *.pdf                          # PDF reports
│   └── *.csv                          # Results summaries
└── modeling notebooks:
    ├── modeling.ipynb                  # Basic ML pipeline
    ├── modeling_1.ipynb               # Advanced imbalanced learning
    ├── modeling_2.ipynb               # Baseline with original features
    ├── modeling_3.ipynb               # State-of-the-art techniques
    └── modeling_final.ipynb           # Ultimate optimization
```

## 🚀 Key Results

### Performance Achievements
- **Best F1-Score:** 0.15+ (significant improvement over baseline)
- **Precision:** 15-25% (efficient targeting)
- **Recall:** 25-40% (churn detection rate)
- **ROI:** Positive return on retention campaigns

### Business Impact
- **Churn Prevention:** 25-40% of actual churners identified
- **Campaign Efficiency:** 15-25% precision reduces false alarms
- **Cost Savings:** Proactive retention vs. reactive acquisition
- **Customer Targeting:** 200-400 customers per campaign period

## 🛠️ Technical Implementation

### Requirements
```python
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
imbalanced-learn>=0.8.0
xgboost>=1.5.0
lightgbm>=3.3.0
catboost>=1.0.0
tensorflow>=2.8.0
matplotlib>=3.5.0
seaborn>=0.11.0
```

### Usage
1. **Basic Pipeline:** Run `modeling.ipynb` for standard ML approach
2. **Advanced Techniques:** Use `modeling_1.ipynb` for imbalanced learning
3. **Baseline Comparison:** Execute `modeling_2.ipynb` for original features
4. **State-of-the-art:** Run `modeling_3.ipynb` for cutting-edge methods
5. **Ultimate Optimization:** Use `modeling_final.ipynb` for best performance

## 📈 Model Evolution

| Stage | Approach | Best F1-Score | Key Innovation |
|-------|----------|---------------|----------------|
| Baseline | Standard ML | ~0.05 | Traditional algorithms |
| Advanced | Imbalanced Learning | ~0.13 | SMOTE + Ensemble methods |
| Optimized | Threshold Tuning | ~0.15+ | Cost-sensitive optimization |

## 🎓 Research Contributions

### Academic Impact
- **Methodological Framework:** Complete pipeline for imbalanced churn prediction
- **Comparative Analysis:** Comprehensive evaluation of 10+ algorithms
- **Threshold Optimization:** Novel approach to business-driven model tuning
- **Feature Engineering:** Domain-specific telecom feature creation

### Practical Value
- **Production-Ready Models:** Robust preprocessing and deployment pipeline
- **Business Integration:** ROI analysis and intervention strategies
- **Scalable Framework:** Adaptable to other telecom operators
- **Cost-Effective Solutions:** Positive ROI projections

## 📊 Visualizations

The project generates comprehensive visualizations including:
- Model performance comparisons
- Precision-Recall curves
- Feature importance analysis
- Business impact dashboards
- ROI projections

## 🔍 Key Findings

1. **Class Imbalance:** Major challenge requiring specialized techniques
2. **Ensemble Methods:** Superior performance over individual algorithms
3. **Threshold Optimization:** Critical for business value maximization
4. **Feature Engineering:** Significant impact on model performance
5. **Cost-Sensitive Learning:** Essential for practical deployment

## 📝 Publications & Presentations

- **Dissertation Seminar 3:** Comprehensive research presentation
- **Technical Reports:** Detailed methodology and results documentation
- **Business Case Studies:** ROI analysis and implementation strategies

## 🤝 Contributing

This research project is part of academic work. For questions or collaboration:
- **Email:** [Contact through institution]
- **LinkedIn:** [Professional profile]
- **Research Gate:** [Academic profile]

## 📄 License

This project is for academic and research purposes. Please cite appropriately if using any methodologies or findings.

## 🙏 Acknowledgments

- **Supervisor:** [Supervisor name]
- **Institution:** [University name]
- **Data Source:** Safaricom PLC (simulated data)
- **Technical Support:** Open-source ML community

---

**Last Updated:** January 2026  
**Status:** Active Research Project  
**Version:** 1.0