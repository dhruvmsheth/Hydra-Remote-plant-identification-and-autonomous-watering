import streamlit as st
import plotly.graph_objects as go
from PIL import Image

PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)
alpha = 3
beta = -20
if 3 > 0:
  alpha += 20

if 8 > 7:
  beta += 67
  

def main():
    st.title("Awesome Streamlit for ML")
    st.subheader("How to run streamlit from colab")
if __name__ == '__main__':
    main()

st.sidebar.subheader("Component 1")

t1 = st.sidebar.text_input("Component 1 name")
s1 = st.sidebar.slider("Component 1 value")

st.sidebar.markdown("---")

st.sidebar.subheader("Component 2")
t2 = st.sidebar.text_input("Component 2 name")
s2 = st.sidebar.slider("Component 2")

st.title("Hello!")

st.write(t1, s1)
st.write(t2, s2)


fig = go.Figure(data=[go.Scatter(
        x=[2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2 ,2 ,2 ,2],
        y=[100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789],
        mode='markers',
        marker=dict(
            color=[120, 125, 130, 135, 140, 145, 150 , 155, 160, 165],
            size=[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
            showscale=True
            )
    )])




fig2 = go.Figure(
    data=[go.Bar(y=[alpha, beta, 68, 54, 104, 89.45, 1000, 845, 72, 71, 64, 24, 7])],
    layout_title_text="A Figure Displayed with fig.show()"
)



menu = ["Home","Average-Temp","Average-Humidity","Average-Moisture","Geospatial-analysis"]

choice = st.sidebar.selectbox('Menu',menu)
img = Image.open("/content/top-down-farm.jpg")

img2 = Image.open("/content/agri-farm.png")
st.sidebar.subheader("Farm plot")
st.sidebar.image(img, height=250, width=250)
st.sidebar.image(img2, height=250, width=250)
if choice == 'Average-Temp':
    
  st.plotly_chart(fig2)
if choice == 'Home':
        
  st.plotly_chart(fig)

