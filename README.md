# SmartFarm AI - Intelligent Agricultural Advisory System

A full-featured Flask web application that provides AI-powered agricultural advisory services. SmartFarm AI combines machine learning, deep learning image recognition, and community features to help farmers make data-driven decisions about crop selection, yield optimization, disease management, and more.

## Features

### AI Prediction Services

- **Crop Yield Prediction** - Predicts crop yield (hg/ha) using a Random Forest Regressor trained on rainfall, pesticide, and temperature data.
- **Disease Risk Assessment** - Evaluates disease risk levels (Low/Medium/High) based on environmental conditions using a Random Forest Classifier, with actionable prevention recommendations.
- **Fertilizer Recommendation** - Provides NPK (Nitrogen, Phosphorus, Potassium) dosage recommendations tailored to crop type, soil, growth stage, and field size. Includes application schedules and cost estimates.
- **Weather Prediction** - Forecasts rainfall trends for a given year using Linear Regression on historical data, with general weather advisories.
- **Crop Recommendation** - Suggests the best crops to grow based on 10+ input factors (soil type, pH, season, water availability, market preference, etc.) with suitability scores, expected yields, and profit margins.

### Deep Learning Image Analysis

- **Plant Disease Detection** - Upload a leaf photo and a VGG16-based CNN identifies diseases across 9 plant species (Apple, Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, Tomato) with 33 detectable conditions. Returns confidence scores, top predictions, and treatment recommendations.
- **Crop Classification** - Upload a crop photograph and a MobileNetV2-based CNN identifies it from 30 agricultural crop types including Rice, Wheat, Cotton, Sugarcane, Tea, Coffee, and more.

### Farmer Connect Community

- **Discussion Forum** - Post questions categorized by crop type and topic (Disease Management, Pest Control, Soil Management, etc.). Get answers from the community.
- **Marketplace** - Buy and sell crops, seeds, equipment, and farming inputs. Create listings with pricing, quantity, and location details.
- **Expert Advice** - Connect with agricultural experts and extension officers for professional guidance.
- **Local Connections** - Find and connect with nearby farmers based on location and crop interest for knowledge sharing.

### User Management

- **Role-Based Access** - Three user roles: Admin, Farmer, and User, each with tailored dashboard views.
- **Admin Dashboard** - Platform statistics, user management, forum post moderation, and marketplace listing oversight.
- **Farmer Dashboard** - Prediction history, agricultural stats, quick access to all AI services.
- **User Dashboard** - Personal prediction history and profile management.
- **Prediction History** - All predictions are saved and viewable in detailed modals with input parameters and results.

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| Backend | Flask 2.3.3, Python, SQLite |
| ML Models | scikit-learn 1.3.0 (Random Forest, Linear Regression) |
| Deep Learning | TensorFlow/Keras (VGG16, MobileNetV2) |
| Image Processing | OpenCV, Pillow |
| Frontend | Bootstrap 5, Font Awesome 6, Inter (Google Fonts) |
| Visualization | Chart.js (client), matplotlib/seaborn (training) |
| Auth | Werkzeug password hashing, Flask sessions |

## Project Structure

```
SmartFarm-AI/
├── app.py                          # Main Flask application
├── database.py                     # SQLite database initialization & CRUD
├── requirements.txt                # Python dependencies
├── smartfarm.db                    # SQLite database (auto-created)
├── dataset/                        # Agricultural datasets
│   └── Agricultural-crops-dataset/
├── models/                         # Trained ML/DL models
│   ├── yield_prediction_model.pkl  # Random Forest Regressor
│   ├── disease_prediction_model.pkl# Random Forest Classifier
│   ├── weather_model.pkl           # Linear Regression
│   ├── fertilizer_recommender.pkl  # Fertilizer recommendation
│   ├── leaf_disease_model.h5       # VGG16 CNN (33 classes)
│   ├── crop_cnn_model.keras        # MobileNetV2 CNN (30 classes)
│   ├── yield_scaler.pkl            # Input normalization
│   ├── disease_scaler.pkl          # Input normalization
│   ├── disease_encoder.pkl         # Label encoding
│   ├── labels.json                 # Crop classification metadata
│   └── prediction_models.py        # Model loading & inference
├── static/
│   ├── css/style.css               # Custom styling
│   ├── js/
│   │   ├── main.js                 # Frontend logic
│   │   └── charts.js               # Data visualization
│   └── uploads/                    # User-uploaded images
├── templates/                      # 19 Jinja2 HTML templates
│   ├── base.html                   # Base layout (navbar, footer)
│   ├── index.html                  # Homepage
│   ├── about.html                  # About page
│   ├── login.html                  # Login form
│   ├── register.html               # Registration form
│   ├── yield_prediction.html       # Yield prediction form
│   ├── disease_prediction.html     # Disease risk form
│   ├── fertilizer_recommendation.html # Fertilizer advisor
│   ├── weather_prediction.html     # Weather forecast
│   ├── crop_recommendation.html    # Crop selection advisor
│   ├── plant_disease_detection.html# Leaf image upload
│   ├── crop_classification.html    # Crop image upload
│   ├── user_dashboard.html         # User dashboard
│   ├── farmer_dashboard.html       # Farmer dashboard
│   ├── admin_dashboard.html        # Admin panel
│   ├── farmer_connect.html         # Community hub
│   ├── farmer_forum.html           # Discussion forum
│   ├── farmer_marketplace.html     # Buy/sell marketplace
│   └── expert_advice.html          # Expert advisory
└── training notebooks
    ├── training.ipynb              # Yield/disease/weather model training
    ├── crop_classification_training.ipynb
    └── PlantDiseas.ipynb           # Leaf disease model training
```

## Datasets

| Dataset | Source |
|---------|--------|
| Plant Disease Detection | [Google Drive](https://drive.google.com/file/d/1RKNH8i_WDeJ7rFKuCgdTJsfwkqN0Z8ZJ/view) |
| Agriculture Crops (Classification) | [Kaggle](https://www.kaggle.com/datasets/osamajalilhassan/agriculture-crops-dataset) |

## Database Schema

| Table | Purpose |
|-------|---------|
| `users` | User accounts with role (admin/farmer/user), profile info |
| `predictions_history` | All prediction results linked to users (type, input JSON, result) |
| `forum_posts` | Community forum questions with category and crop tags |
| `marketplace_listings` | Buy/sell listings with item details and location |

Default admin account: `admin@smartfarmai.com` / `admin123`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/predict-yield` | POST | Crop yield prediction |
| `/api/predict-disease` | POST | Disease risk assessment |
| `/api/recommend-fertilizer` | POST | NPK fertilizer recommendation |
| `/api/predict-weather` | POST | Rainfall forecast |
| `/api/recommend-crop` | POST | Smart crop recommendation |
| `/api/detect-plant-disease` | POST | Leaf disease detection (image) |
| `/api/classify-crop` | POST | Crop classification (image) |
| `/api/post-question` | POST | Submit forum question |
| `/api/get-forum-posts` | GET | Retrieve forum posts |
| `/api/connect-farmers` | POST | Find nearby farmers |
| `/api/submit-listing` | POST | Create marketplace listing |

## Setup

### 1. Clone and install

```bash
git clone <repository_url>
cd SmartFarm-AI
python -m venv venv
source venv/bin/activate    # macOS/Linux
# .\venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Train models (optional)

Pre-trained models are included in `models/`. To retrain:

```bash
jupyter notebook training.ipynb
```

### 3. Run

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Supported Crops & Plants

**Disease Detection (9 species, 33 conditions):**
Apple, Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, Tomato

**Crop Classification (30 types):**
Almond, Banana, Cardamom, Cherry, Chilli, Clove, Coconut, Coffee Plant, Cotton, Cucumber, Fox Nut, Gram, Jowar, Jute, Lemon, Maize, Mustard Oil, Olive Tree, Papaya, Pearl Millet, Pineapple, Rice, Soyabean, Sugarcane, Sunflower, Tea, Tobacco, Tomato, Vigna Radiata (Mung), Wheat

**Crop Recommendation (20+ crops):**
Rice, Wheat, Maize, Cotton, Sugarcane, Soybeans, Groundnut, Chickpea, Pigeon Pea, Linseed, Mustard, Sunflower, Turmeric, Tea, Coffee, and more

## Contributing

Contributions are welcome. Open an issue or submit a pull request for bug fixes, improvements, or new features.
