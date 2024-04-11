import pandas as pd

def generate_timeline_html(df, margin_coefficient):
    """
    タイムラインのHTMLを生成する関数。

    Parameters:
    - df: タイムラインのデータを含むDataFrame。
    - margin_coefficient: 上部マージンの係数。

    Returns:
    - timeline_html: 生成されたタイムラインのHTML。
    """

    timeline_html = '<ul class="time-schedule">'
    base_time = pd.to_datetime(df["time"].iloc[0], format="%H:%M")
    
    for _, row in df.iterrows():
        time = row["time"]
        title = row["title"]
        content = row["content"]
        
        time_diff = pd.to_datetime(time, format="%H:%M") - base_time
        minutes_diff = time_diff.total_seconds() / 60
        margin_top = f"{minutes_diff * margin_coefficient}px"
        
        timeline_html += f'''
        <li style="margin-top: {margin_top};">
            <span class="time">{time}</span>
            <div class="sch_box">
                <p class="sch_title">{title}</p>
                <p class="sch_tx">{content}</p>
            </div>
        </li>'''
    
    timeline_html += '</ul>'
    
    return timeline_html