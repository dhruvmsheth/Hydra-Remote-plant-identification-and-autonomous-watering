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
 
img = Image.open("/content/top-down-farm.jpg")
st.image(img)
img2 = Image.open("/content/agri-farm.png")
st.image(img2)
fig = go.Figure(data=[go.Scatter(
        x=[1, 3.2, 5.4, 7.6, 9.8, 12.5, 13, 8, 3, 11.2],
        y=[1, 3.2, 5.4, 7.6, 9.8, 12.5, 12, 4, 7.6, 9.2],
        mode='markers',
        marker=dict(
            color=[120, 125, 130, 135, 140, 145, 150 , 155, 160, 165],
            size=[15, 30, 55, 70, 90, 40, 55, 83, 72, 34],
            showscale=True
            )
    )])




fig2 = go.Figure(
    data=[go.Bar(y=[alpha, beta, 68, 54, 104, 89.45, 1000, 845, 72, 71, 64, 24, 7])],
    layout_title_text="A Figure Displayed with fig.show()"
)



menu = ["Home","About"]
choice = st.sidebar.selectbox('Menu',menu)
if choice == 'About':
		
  st.plotly_chart(fig2)
if choice == 'Home':
		
  st.plotly_chart(fig)
