import streamlit as st
import pandas as pd
import pickle
import logging
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Configure logging
logging.basicConfig(
    filename='movie_rating_predictor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load data and models
@st.cache_resource
def load_resources():
    try:
        # Load unseen data
        with open('./Datasets/Unseen_df.pkl', 'rb') as f:
            unseen_df = pickle.load(f)
        
        # Load target encoder
        with open('./models/target_encoder', 'rb') as f:
            encoder = pickle.load(f)
        
        # Load trained model
        with open('./models/model.py', 'rb') as f:
            model = pickle.load(f)

        # with open('./models/best_random_forest_regressor', 'rb') as f:
        #     model = pickle.load(f)
        
        logger.info("Data and models loaded successfully")
        return unseen_df, encoder, model
    
    except Exception as e:
        logger.error(f"Loading error: {str(e)}")
        st.error("Failed to load required files. Check logs for details.")
        st.stop()

unseen_df, encoder, model = load_resources()

# App configuration
st.set_page_config(page_title="Movie Rating Predictor", layout="wide")
st.title("🎬 Movie Rating Prediction System")

# Sidebar for movie selection
st.sidebar.header("Movie Selection")
selected_movie = st.sidebar.selectbox(
    "Select a movie",
    options=unseen_df['Name'].unique(),
    index=0
)

# Display selected movie details
st.header("Selected Movie Details")
movie_data = unseen_df[unseen_df['Name'] == selected_movie].iloc[0]

# Show all columns in an expandable section
with st.expander("View all movie details"):
    st.dataframe(movie_data)

# Prediction section
st.header("Rating Prediction")
predict_button = st.button("Predict Rating")

if predict_button:
    try:
        # Prepare target columns
        target_cols = ['Director', 'Actor 1', 'Actor 2', 'Actor 3']
        valid_genre_columns = [col for col in unseen_df.columns if col.startswith('genre_')]
        selected_features = target_cols + valid_genre_columns
        
        # Apply target encoding
        encoded_data = movie_data[target_cols].to_frame().T
        encoded_data = encoder.transform(encoded_data)
        
        # Prepare final input
        prediction_input = movie_data[selected_features].copy()
        prediction_input[target_cols] = encoded_data[target_cols]
        prediction_input = prediction_input[selected_features].to_frame().T
        
        # Make prediction
        predicted_rating = model.predict(prediction_input)[0]
        predicted_rating = max(1, min(10, predicted_rating))  # Clip to 1-10 range
        
        # Display prediction
        st.success(f"Predicted Rating: **{predicted_rating:.2f}/10**")
        logger.info(f"Predicted {selected_movie}: {predicted_rating:.2f}")
        
        # Show important features
        st.subheader("Top Influencing Features")
        feature_importance = pd.DataFrame({
            'Feature': selected_features,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False).head(5)
        
        st.table(feature_importance)
        
    except Exception as e:
        logger.error(f"Prediction failed for {selected_movie}: {str(e)}")
        st.error("Prediction error. Check logs for details.")

# Add download button for logs
with open('movie_rating_predictor.log', 'rb') as f:
    st.sidebar.download_button(
        "Download Logs",
        data=f,
        file_name="prediction_logs.log"
    )