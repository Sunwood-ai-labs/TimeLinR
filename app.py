import streamlit as st
import pandas as pd
from io import StringIO
from html2image import Html2Image

hti = Html2Image()

from modules.create_custom_css_file import create_custom_css_file
from modules.timeline import generate_timeline_html
from config import config
import os

st.set_page_config(layout="wide")
hti = Html2Image()

def load_css(file_path):
    with open(file_path, encoding="utf8") as f:
        return f.read()

def load_markdown(file_path):
    with open(file_path, encoding="utf8") as f:
        return f.read()

def display_front_page():
    html_front = load_markdown('docs/html_front.md')
    st.markdown(f"{html_front}", unsafe_allow_html=True)

def get_csv_data():
    return st.text_area("CSVデータを貼り付けてください", height=200)

def get_user_inputs():
    margin_coefficient = st.number_input("上部マージンの係数", value=0.1, step=0.1)
    border_color = st.color_picker('境界線の色', '#a7be18')
    marker_color = st.color_picker('マーカーの色', '#a7be18')
    box_background = st.color_picker('ボックスの背景色', '#efefef')
    output_path = st.text_input('保存する画像のパス', 'timeline_image.png')
    return margin_coefficient, border_color, marker_color, box_background, output_path

def process_csv_data(csv_data):
    try:
        df = pd.read_csv(StringIO(csv_data), header=None, names=["time", "title", "content"])
        return df
    except Exception as e:
        st.error(f"CSVデータの解析中にエラーが発生しました: {str(e)}")
        return None

def generate_timeline(df, margin_coefficient):
    timeline_html = generate_timeline_html(df, margin_coefficient)
    st.write(timeline_html, unsafe_allow_html=True)
    return timeline_html

def create_custom_css(border_color, marker_color, box_background):
    os.makedirs("./tmp_TimeLinR", exist_ok=True)

    css_file_path = create_custom_css_file(border_color, marker_color, box_background, './tmp_TimeLinR/custom_style.css')
    custom_css = load_css(css_file_path)
    st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
    return custom_css

def download_image(output_path):
    with open(output_path, "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name="timeline.png",
            mime="image/png"
        )

def main():
    display_front_page()
    csv_data = get_csv_data()

    with st.sidebar:
        margin_coefficient, border_color, marker_color, box_background, output_path = get_user_inputs()

    if st.button("生成"):
        if csv_data.strip():
            df = process_csv_data(csv_data)
            if df is not None:
                timeline_html = generate_timeline(df, margin_coefficient)
                custom_css = create_custom_css(border_color, marker_color, box_background)
                hti.screenshot(html_str=timeline_html, css_str=custom_css, save_as=output_path)
                download_image(output_path)
        else:
            st.warning("CSVデータが入力されていません。")

if __name__ == "__main__":
    custom_css = load_css('config/custom_style.css')
    st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
    main()