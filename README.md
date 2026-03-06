# 🛡️ PredictiChain: Strategic Supply Chain Control Tower

**PredictiChain** is a production-ready, containerized Decision Intelligence platform designed to mitigate global supply chain disruptions. By integrating **Machine Learning optimization** with **Time Series forecasting**, it provides executive-level visibility into financial risks and inventory requirements.

---

## 🚀 Key Performance Indicators (KPIs)
* **Financial Risk Quantification**: Identified **$455,213,874** in total Revenue @ Risk.
* **Risk Frequency**: Monitoring a **61.3%** disruption probability across the global network.
* **Inventory Carrying Costs**: Managing **$415,845,862** in current inventory value.
* **Safety Stock Optimization**: Maintaining an average safety stock of **1848.2 MT** through ML-driven optimization.

---

## 🛠️ Technical Core
### 📈 Time Series Demand Forecasting
The platform features a dedicated **Demand Trend** module that utilizes historical data to generate **7-day predicted demand volume** trends. This allows for proactive rather than reactive logistics planning.

### 🤖 ML Optimization Engine
The backend engine analyzes shipment vulnerability scores and weather conditions (Hurricane, Storm, Fog, Rain) to calculate the **Required Buffer Stock** for every individual shipment.

### 🐳 Containerized Architecture
Built for scale using a decoupled Docker-Compose architecture:
* **Backend Container**: Executes data processing and ML optimization.
* **Frontend Container**: Serves an interactive Streamlit dashboard for executive decision-making.

---

## 📂 Project Structure
```text
PredictiChain/
├── Backend/                 # Optimization & ML Engine
│   ├── Data/                # Raw and Processed Analytics
│   ├── src/engine.py        # Core processing logic
│   └── models/              # Saved ML artifacts
├── Frontend/                # Strategic Dashboard
│   └── app/main.py          # Streamlit UI code
├── docker-compose.yml       # Service orchestration
└── Dockerfile               # Production environment blueprint
