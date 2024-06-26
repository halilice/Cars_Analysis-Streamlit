import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/free-vector/\
colorful-gradient-background-wave-white-color_343694-1466.\
jpg?w=1060&t=st=1718878613~exp=1718879213~hmac=e0323fdd13b1d9acde1ebfe0fc46a8294d8200a3f106676387e217642267001e");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown('**<p style="font-family:sans-serif; color:Darkblue; font-size: 30px;">\
          Analysis of Correlation et Distribution of Cars by Regions</p>**',
          unsafe_allow_html=True)

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

df['mpg'] = df['mpg'].apply(lambda x: round((x*1.609344/3.78541178),2))
df['cubicinches'] = df['cubicinches'].apply(lambda x: round((x*0.016387064),2))  
df['weightlbs'] = df['weightlbs'].apply(lambda x: round((x*0.45359237),2))
df = df.rename(columns={'mpg': 'km_per_liter', 
                        'cubicinches': 'engine displacement(liter)',
                        'weightlbs': 'weightkg',
                        'time-to-60': 'time-to-100',
                        'continent': 'region'})
df['year'] = pd.to_datetime(df.year, format='%Y')
df['year'] = df['year'].apply(lambda x: x.strftime('%Y'))

df

# Fuel consumption by different specifications of cars

st.markdown('**<p style="font-family:sans-serif; color:Darkblue; font-size: 24px;">\
            Fuel consumption by different specifications of cars</p>**', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(15,10), nrows=2, ncols=2)

ax1 = plt.subplot(221)
sns.barplot(data=df, x='cylinders', y='km_per_liter', hue='region', errorbar=None)
ax1.set_title('Km Made per Liter vs Number of Cylinders')

ax2 = plt.subplot(222)
sns.scatterplot(data=df, x='engine displacement(liter)', y='km_per_liter', hue='region')
ax2.set_title('Km Made per Liter vs Engine Displacement')

ax3 = plt.subplot(223)
sns.scatterplot(data=df, x='hp', y='km_per_liter', hue='region')
ax3.set_title('Km Made per Liter vs Horse Power')

ax4 = plt.subplot(224)
sns.scatterplot(data=df, x='weightkg', y='km_per_liter', hue='region')
ax4.set_title('Km Made per Liter vs Weight of Cars')

st.pyplot(fig)

# Correlation between time to reach 100 km/h and Engine Displacement & Horse Power

st.markdown('**<p style="font-family:sans-serif; color:Darkblue; font-size: 24px;">\
            Correlation between time to reach 100 km/h and Engine Displacement & Horse Power</p>**',\
            unsafe_allow_html=True)


fig, ax = plt.subplots(figsize=(15,5), nrows=1, ncols=2)

ax1 = plt.subplot(121)
sns.scatterplot(data=df, x='engine displacement(liter)', y='time-to-100', hue='region')
ax1.set_title('Time to Reach 100km/h vs Engine Displacement')

ax2 = plt.subplot(122)
sns.scatterplot(data=df, x='hp', y='time-to-100', hue='region')
ax2.set_title('Time to Reach 100km/h vs Horse Power')

st.pyplot(fig)

# Different specifications of cars by region

st.markdown('**<p style="font-family:sans-serif; color:Darkblue; font-size: 24px;">\
             Different specifications of cars by region</p>**', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(15,10), nrows=2, ncols=2)

ax1 = plt.subplot(221)
sns.barplot(data=df, x='region', y='hp', errorbar=None)
ax1.set_title('Horsepower by Continents', fontsize=10)

ax2 = plt.subplot(222)
sns.barplot(data=df, x='region', y='cylinders', errorbar=None)
ax2.set_title('Number of Cylinders by Continents', fontsize=10)

ax3 = plt.subplot(223)
sns.barplot(data=df, x='region', y='engine displacement(liter)', errorbar=None)
ax3.set_title('Engine Displacement (liter) by Continents', fontsize=10)

ax4 = plt.subplot(224)
sns.barplot(data=df, x='region', y='weightkg', errorbar=None)
ax4.set_title('Weight of Cars by Continents', fontsize=10)

st.pyplot(fig)
