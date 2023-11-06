import streamlit as st
import pandas as pd
import xgboost as xgb

def main():
    html_temp = """ 
    <div style = "background-color:lightblue;padding:16px">
    <h2 style = "color:black;text-align:center;"> Diamond Price Prediction Web App </h2>
    </div>
    """
    
    model = xgb.XGBRegressor()
    model.load_model('diamond_xgb_model.json')
    
    st.markdown(html_temp, unsafe_allow_html = True)
    st.write ('')
    st.write ('')
    
    st.markdown("Let's Try Evaluating The Price Of These Of These Diamonds")
    
    p1 = st.number_input ('What is the carat of the diamond? (In Dollars)', 0.0, 5.0, step = 0.1)
    
    
    s1 = st.selectbox ('What is the cut of the diamond?', ('Premium', 'Fair', 'Very Good', 'Good', 'Ideal'))
    
    if s1 == 'Premium':
        p2 = 0
    elif s1 == 'Fair':
        p2 = 1
    elif s1 == 'Very Good':
        p2 = 2
    elif s1 == 'Good':
        p2 = 3
    elif s1 == 'Ideal':
        p2 = 4
    s2 = st.selectbox ('What is the color of the diamond?', ('F', 'G', 'E', 'D', 'H', 'J', 'I'))
    
    if s2 == 'F':
        p3 = 0
    elif s2 == 'G':
        p3 = 1
    elif s2 == 'E':
        p3 = 2
    elif s2 == 'D':
        p3 = 3
    elif s2 == 'H':
        p3 = 4
    elif s2 == 'J':
        p3 = 5
    else:
        p3 = 6
    
    s3 = st.selectbox ('What is the clarity of the diamond?', ('VS1', 'I1', 'VS2', 'VVS1', 'SI1', 'VVS2', 'SI2', 'IF'))
    
    if s3 == 'VS1':
        p4 = 0
    elif s3 == 'I1':
        p4 = 1
    elif s3 == 'VS2':
        p4 = 2
    elif s3 == 'VVS1':
        p4 = 3
    elif s3 == 'SI1':
        p4 = 4
    elif s3 == 'VVS2':
        p4 = 5
    elif s3 == 'SI2':
        p4 = 6
    else:
        p4 = 7
    
    
    
    data_new = pd.DataFrame ({
    'carat':p1,
    'cut': p2,
    'color':p3,
    'clarity':p4
}, index = [0])
    try:
        if st.button ('Predict'):
            pred = model.predict(data_new)
            if pred > 0:
                st.balloons()
                st.success('You can sell the diamond at {:.2f} Dollars'.format (pred[0]))
            else:
                st.Warning ("You can't sell this diamond")
    except:
        st.warning('Something Went Wrong,Try again')

if __name__ == '__main__':
    main()