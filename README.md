# HB-GWO Feature Selection

This repository contains the implementation of the **Hybrid Butterfly-Grey Wolf Optimization (HB-GWO)** algorithm for feature selection in high-dimensional datasets.

## 📦 Features
- Hybrid global-local search via BOA and GWO
- Adaptive switching strategy
- Multi-classifier evaluation (Random Forest, SVM, XGBoost, MLP)
- Balanced metrics (F1, AUC-ROC)
- Sensitivity analysis and Optuna tuning
- Real-world scalability validation (e.g., RNA-seq with >100k features)

## 🛠️ Requirements
- Python 3.11
- NumPy
- scikit-learn
- matplotlib
- optuna
- pandas
- seaborn

## 🚀 Running the Code
```bash
python main.py
```

## 📊 Parameters
Key algorithm parameters (all customizable):

- **BOA**: `c=0.01`, `a=0.1`, `p=0.8`
- **GWO**: Dynamic A and C vectors
- **General**: Population=30, Iterations=200, λ=0.75, α=0.65

## 📂 Structure
- `main.py` – Main algorithm config and structure
- `README.md` – Documentation and setup guide

## 📜 License
MIT License

## 📫 Contact
For questions or collaborations, reach out to [mohammed-alysalem@eru.edu.eg](mailto:mohammed-alysalem@eru.edu.eg)
