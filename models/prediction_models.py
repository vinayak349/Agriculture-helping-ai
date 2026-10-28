import joblib
import numpy as np
import pandas as pd
import os

class PredictionModels:
    def __init__(self):
        self.models_dir = 'models/'
        self.yield_model = None
        self.yield_v2 = None
        self.yield_scaler = None
        self.disease_model = None
        self.disease_scaler = None
        self.disease_encoder = None
        self.weather_model = None
        self.fertilizer_recommender = None
        self.load_models()

    def _safe_load(self, filename):
        path = f'{self.models_dir}{filename}'
        if not os.path.exists(path):
            return None
        try:
            return joblib.load(path)
        except Exception as e:
            print(f"[models] Could not load {filename}: {e}")
            return None

    def load_models(self):
        """Load all trained models"""
        self.yield_v2 = self._safe_load('yield_model_v2.pkl')
        self.yield_model = self._safe_load('yield_prediction_model.pkl')
        self.yield_scaler = self._safe_load('yield_scaler.pkl')
        self.disease_model = self._safe_load('disease_prediction_model.pkl')
        self.disease_scaler = self._safe_load('disease_scaler.pkl')
        self.disease_encoder = self._safe_load('disease_encoder.pkl')
        self.weather_model = self._safe_load('weather_model.pkl')
        self.fertilizer_recommender = self._safe_load('fertilizer_recommender.pkl')
    
    def predict_yield(self, rainfall, pesticide, temperature, crop=None):
        """Predict crop yield"""
        crop_map = {
            'Rice': 'Rice, paddy',
            'Potato': 'Potatoes',
            'Soybean': 'Soybeans',
            'Sweet potato': 'Sweet potatoes',
            'Plantains': 'Plantains and others'
        }
        if crop:
            crop = crop_map.get(crop, crop)

        if self.yield_v2 and crop and crop in self.yield_v2.get('crops', []):
            df_row = pd.DataFrame(
                [[rainfall, pesticide, temperature, crop]],
                columns=['rainfall', 'pesticide', 'temperature', 'crop']
            )
            prediction = self.yield_v2['model'].predict(df_row)[0]
            crop_ranges = self.yield_v2.get('ranges', {}).get(crop)
            if crop_ranges:
                prediction = float(np.clip(prediction, crop_ranges['lo'], crop_ranges['hi']))
            return round(prediction, 2)

        if self.yield_model and self.yield_scaler:
            input_data = np.array([[rainfall, pesticide, temperature]])
            input_scaled = self.yield_scaler.transform(input_data)
            prediction = self.yield_model.predict(input_scaled)[0]
            return round(prediction, 2)
        return None
    
    def predict_disease_risk(self, rainfall, temperature, pesticide):
        """Predict disease risk"""
        if self.disease_model and self.disease_scaler and self.disease_encoder:
            input_data = np.array([[rainfall, temperature, pesticide]])
            input_scaled = self.disease_scaler.transform(input_data)
            prediction = self.disease_model.predict(input_scaled)[0]
            risk_level = self.disease_encoder.inverse_transform([prediction])[0]
            return risk_level
        return None
    
    def recommend_fertilizer(self, crop, rainfall):
        """Get fertilizer recommendation"""
        if self.fertilizer_recommender:
            npk, matched_crop = self.fertilizer_recommender(crop, rainfall)
            return {
                'matched_crop': matched_crop,
                'nitrogen_kg_ha': npk['N'],
                'phosphorus_kg_ha': npk['P'],
                'potassium_kg_ha': npk['K'],
                'recommendation': f"Apply {npk['N']}kg/ha N, {npk['P']}kg/ha P, {npk['K']}kg/ha K"
            }
        return None
    
    def predict_weather(self, year):
        """Predict weather patterns"""
        if self.weather_model:
            prediction = self.weather_model.predict(np.array([[year]]))[0]
            return round(prediction, 1)
        return None
