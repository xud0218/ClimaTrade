## **Installation**

### **Requirements**
- Python 3.8 or higher
- Required dependencies are listed in `requirements.txt`.

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ClimaTrade.git
   cd ClimaTrade

2. Install dependencies
   ```bash
   make install
   ```
## **Usage**

### **Run the Application**
To start the dashboard, run the following command:
```bash
make run
```
The app will be available at http://127.0.0.1:8050.

## **Project Structure**
ClimaTrade/
├── app/
│   ├── __init__.py
│   ├── routes.py             # Defines layout and callbacks
│   ├── visualizations.py     # Visualization functions
├── assets/
│   ├── icon/
│   │   └── weather-app.png   # App icon
├── data/
│   └── Central_Park_Weather.csv  # Historical weather data
├── models/
│   ├── gradient_boosting_model.pkl
│   ├── linear_regression_model.pkl
│   └── random_forest_model.pkl
├── utils/
│   ├── __init__.py
│   ├── evaluation.py         # Model evaluation utilities
│   ├── nowcasting.py         # Real-time weather data handling
│   └── preprocessing.py      # Data preprocessing functions
├── app.py                    # Main app entry point
├── Makefile                  # Make commands for setup and execution
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

ClimaTrade/
├── app/
│   ├── __init__.py
│   ├── routes.py             # Defines layout and callbacks
│   ├── visualizations.py     # Visualization functions
├── assets/
│   ├── icon/
│   │   └── weather-app.png   # App icon
├── data/
│   └── Central_Park_Weather.csv  # Historical weather data
├── models/
│   ├── gradient_boosting_model.pkl
│   ├── linear_regression_model.pkl
│   └── random_forest_model.pkl
├── utils/
│   ├── __init__.py
│   ├── evaluation.py         # Model evaluation utilities
│   ├── nowcasting.py         # Real-time weather data handling
│   └── preprocessing.py      # Data preprocessing functions
├── app.py                    # Main app entry point
├── Makefile                  # Make commands for setup and execution
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation


