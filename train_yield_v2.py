import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error


def train():
    data_path = os.path.join('dataset', 'yield_df.csv')
    df = pd.read_csv(data_path)

    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    df = df.rename(columns={
        'average_rain_fall_mm_per_year': 'rainfall',
        'pesticides_tonnes': 'pesticide',
        'avg_temp': 'temperature',
        'Item': 'crop',
        'hg/ha_yield': 'y'
    })

    features = ['rainfall', 'pesticide', 'temperature', 'crop']
    X = df[features]
    y = df['y']

    # 80/20 split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Build Pipeline
    preprocessor = ColumnTransformer(
        [('crop', OneHotEncoder(handle_unknown='ignore'), ['crop'])],
        remainder='passthrough'
    )
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(
            n_estimators=150,
            min_samples_leaf=3,
            max_features=0.6,
            random_state=42,
            n_jobs=-1
        ))
    ])

    # Evaluate on 80/20 split
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"Hold-out R2: {r2:.4f}")
    print(f"Hold-out MAE: {mae:.2f}")

    # Refit on all data
    pipeline.fit(X, y)

    # Compute sorted list of crops and ranges
    crops = sorted(df['crop'].unique().tolist())
    ranges = {}
    for crop, group in df.groupby('crop'):
        ranges[crop] = {
            'lo': float(group['y'].quantile(0.01)),
            'hi': float(group['y'].quantile(0.99))
        }

    # Save to models/yield_model_v2.pkl
    save_data = {
        'model': pipeline,
        'crops': crops,
        'ranges': ranges
    }

    os.makedirs('models', exist_ok=True)
    model_path = os.path.join('models', 'yield_model_v2.pkl')
    joblib.dump(save_data, model_path, compress=3)
    print(f"Model saved successfully to {model_path}")


if __name__ == '__main__':
    train()

