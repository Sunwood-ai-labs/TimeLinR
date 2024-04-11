def create_custom_css_file(border_color="#a7be18", marker_color="#a7be18", box_background="#efefef", output_file_path="./docs/custom_style.css"):
    """
    指定された色を使用してカスタマイズされたCSSファイルを生成し、指定されたパスに出力する関数。

    Parameters:
    - border_color: 線の色。
    - marker_color: マーカーの色。
    - box_background: ボックスの背景色。
    - output_file_path: 出力ファイルのパス。

    Returns:
    - output_file_path: 出力ファイルのパス。
    """

    css_template = """
    *{{
        margin:0;
        padding:0;
        line-height: 1.3em;
        font-family: "Noto Serif JP", serif;
        font-weight: 400;
        font-style: normal;
    }} 
    /* time-schedule */
    .time-schedule {{
        min-width: 400px;
        max-width: 1200px;
        list-style: none;
        margin: 0 auto 0 6em;
        padding-left: 20px;
        border-left: 6px solid {border_color};
        box-sizing: border-box;
    }}

    .time-schedule li {{
        width: 100%;
        margin: 0 0;
        padding: 5px 0;
        position: relative;
    }}

    .time-schedule span.time {{
        width: 5em;
        display: inline-block;
        margin-left: -8em;
        padding: 0 0 5px;
        margin-top: 15px;
        vertical-align: top;
        position: relative;
        text-align: right;
        box-sizing: border-box;
    }}

    .time-schedule span.time::after {{
        content: "";
        position: absolute;
        right: -35px;
        top: 0;
        background: {marker_color};
        width: 20px;
        height: 20px;
        border-radius: 10px;
    }}

    .time-schedule .sch_box {{
        display: inline-block;
        width: 100%;
        margin-left: 30px;
        padding: 15px 10px 15px 10px;
        vertical-align: middle;
        background: {box_background};
        box-sizing: border-box;
        border-radius: 6px;
    }}

    .time-schedule .sch_title {{
        font-size: 16px;
        font-weight: 700;
    }}

    .time-schedule .sch_tx {{
        font-size: 14px;
        font-weight: normal;
    }}
    """

    custom_css = css_template.format(border_color=border_color, marker_color=marker_color, box_background=box_background)

    with open(output_file_path, "w") as file:
        file.write(custom_css)

    return output_file_path


if __name__ == "__main__":
    # テストケース1: デフォルトの色で実行
    test_output_file_path1 = create_custom_css_file()
    print(f"Test Case 1: {test_output_file_path1}")

    # テストケース2: カスタムの色で実行
    test_output_file_path2 = create_custom_css_file(border_color="#ff0000", marker_color="#00ff00", box_background="#0000ff")
    print(f"Test Case 2: {test_output_file_path2}")