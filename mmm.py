import requests
import streamlit as st
import xxx
from pyecharts import options as opts
from pyecharts.charts import Pie, Line, Bar, Scatter, Radar
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType
from snapshot_selenium import snapshot as driver
import random
from pyecharts.charts import Funnel, Gauge
# import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from pyecharts.charts import WordCloud


def get_data(url):
    # response = requests.get(url)
    data = []
    data = xxx.process_data(url)
    print('----------------------')
    print(data)
    return data


def visualize_pie(data):
    # 提取x_data和y_data
    x_data = [item['word'] for item in data]
    y_data = [item['count'] for item in data]

    # 创建饼图实例
    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add("", [list(z) for z in zip(x_data, y_data)])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="饼图"),
            legend_opts=opts.LegendOpts(
                orient="horizontal", pos_top="bottom")
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    # 生成静态图片
    make_snapshot(driver, pie.render(), "chart.png")


def visualize_line(data):
    # 提取x_data和y_data
    x_data = [item['word'] for item in data]
    y_data = [item['count'] for item in data]

    # 创建折线图实例
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x_data)
        .add_yaxis("", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="折线图"))
    )

    # 生成静态图片
    make_snapshot(driver, line.render(), "chart.png")


def visualize_bar(data):
    # 提取x_data和y_data
    x_data = [item['word'] for item in data]
    y_data = [item['count'] for item in data]

    # 创建柱状图实例
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x_data)
        .add_yaxis("", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="柱状图"))
        .set_series_opts(itemstyle_opts={"barWidth": "50%"}, tooltip_opts=opts.TooltipOpts(formatter="{b}: {c}"),  # 设置提示框格式
                         )  # 设置柱状图宽度为50%
    )

    # 生成静态图片
    make_snapshot(driver, bar.render(), "chart.png")


def visualize_wordcloud(data):
    # 提取词汇列表和词频列表
    words = [item['word'] for item in data]
    counts = [item['count'] for item in data]

    # 将词汇和词频列表转换为元组列表
    word_freq = list(zip(words, counts))

    # 创建词云图实例
    wordcloud = (
        WordCloud()
        .add(series_name="", data_pair=word_freq, word_size_range=[20, 100])
        .set_global_opts(title_opts=opts.TitleOpts(title="词云图"))
    )

    # 生成静态图片
    make_snapshot(driver, wordcloud.render(), "chart.png")


def visualize_scatter(data):
    # 提取x_data和y_data
    x_data = [item['word'] for item in data]
    y_data = [item['count'] for item in data]

    # 创建散点图实例
    scatter = (
        Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x_data)
        .add_yaxis("", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="散点图"))
    )

    # 生成静态图片
    make_snapshot(driver, scatter.render(), "chart.png")


def visualize_radar(data):
    # 提取x_data和y_data
    x_data = [item['word'] for item in data]
    y_data = [item['count'] for item in data]

    # 创建雷达图实例
    radar = (
        Radar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_schema(schema=[
            opts.RadarIndicatorItem(name=x, max_=max(y_data)) for x in x_data
        ])
        .add("", [y_data])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="雷达图"))
    )

    # 生成静态图片
    make_snapshot(driver, radar.render(), "chart.png")


def visualize_word_frequency_bar(data):
    # 提取x_data和y_data
    x_data = [item['word'] for item in data]
    y_data = [item['count'] for item in data]

    # 创建柱状图实例
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x_data)
        .add_yaxis("", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="词频柱状图"))
    )

    # 生成静态图片
    make_snapshot(driver, bar.render(), "chart.png")


def visualize_funnel(data):
    # 提取x_data和y_data
    x_data = [item['word'] for item in data]
    y_data = [item['count'] for item in data]

    # 创建漏斗图实例
    funnel = (
        Funnel(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add("", [list(z) for z in zip(x_data, y_data)])
        .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图"), legend_opts=opts.LegendOpts(orient='horizontal', pos_bottom='0%')
                         )
    )

    # 生成静态图片
    make_snapshot(driver, funnel.render(), "chart.png")


def visualize_gauge(data):
    # 提取x_data和y_data
    x_data = [item['word'] for item in data]
    y_data = [item['count'] for item in data]

    # 创建仪表盘实例
    gauge = (
        Gauge(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add("", [list(z) for z in zip(x_data, y_data)])
        .set_global_opts(title_opts=opts.TitleOpts(title="仪表盘"))
    )

    # 生成静态图片
    make_snapshot(driver, gauge.render(), "chart.png")

def main():
    st.sidebar.title("侧边导航栏")
    navigation = st.sidebar.radio("选择页面", ["主页",  "联系我们"])

    if navigation == "主页":
        st.title("交互式文本分析Web应用")
        url = st.text_input("请输入网址")
        chart_type = st.selectbox(
            "请选择图表类型", ["饼图", "折线图", "柱状图", "词云图", "散点图", "雷达图", "词频柱状图", "漏斗图", "仪表盘"])

        if st.button("获取数据"):
            data = get_data(url)
            if chart_type == "饼图":
                visualize_pie(data)
            elif chart_type == "折线图":
                visualize_line(data)
            elif chart_type == "柱状图":
                visualize_bar(data)
            elif chart_type == "词云图":
                visualize_wordcloud(data)
            elif chart_type == "散点图":
                visualize_scatter(data)
            elif chart_type == "雷达图":
                visualize_radar(data)
            elif chart_type == "词频柱状图":
                visualize_word_frequency_bar(data)
            elif chart_type == "漏斗图":
                visualize_funnel(data)
            elif chart_type == "仪表盘":
                visualize_gauge(data)

            st.markdown("<br></br>", unsafe_allow_html=True)

            st.image("chart.png", use_column_width=True)


    elif navigation == "联系我们":
        st.title("欢迎来邮")
        st.write("如果您有任何问题，请发送邮件至773074714@qq.com。")


if __name__ == "__main__":
    main()