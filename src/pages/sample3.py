# coding=utf-8
import streamlit as st
import sys
from pathlib import Path
base_path = Path.cwd().parent
sys.path.append(base_path / "src")
from utils import set_slider
import pandas as pd
import datetime
import pickle


def main():
    movie_name = "sample3.mov"
    video_path = base_path / "data"
    video_file = video_path / movie_name

    st.markdown(f"### 動画名:{video_file.name}")
    st.text(f"①　氏名を確認。")
    user = st.text_input('評価者の氏名', '佐藤太郎')
    result_file = base_path / "db" / f"{user}_{movie_name.split('.')[0]}.csv"

    st.text(f"②　動画を確認。")

    with open(video_file, 'rb') as inf:
        video_bytes = inf.read()
        container = set_slider()
        container.video(data=video_bytes)

    st.text(f"③　確認した動画を評価。")
    point = st.selectbox(
        '良い悪いを判断したポイント:',
        ['腕', '肘', '膝', '頭', '投げ手'])
    timing = st.selectbox(
        'ピッチングのタイミング：',
        ['投げ始め', 'リリース時', '投げ終わり'])
    time_from = st.text_input('動画内の開始時間', '00:00')
    time_to = st.text_input('動画内の終了時間', '00:00')
    evaluate = st.selectbox(
        'ポイントの評価：',
        ['○', '×'])
    comment = st.text_input('評価ポイントに対するコメント', '投げ終わりに腕を振り抜き切れていない。')
    total_evalate = st.selectbox(
        '総評(10段階)：',
        ['未評価', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

    if st.button('評価を追加する'):
        data = [
            movie_name,
            user,
            point,
            timing,
            time_from,
            time_to,
            evaluate,
            comment,
            total_evalate,
            datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        ]
        with open('aa.pkl', 'wb') as outf:
            pickle.dump(data, outf)
        result_df = pd.DataFrame(
            data = [data],
            columns=['movie', 'user', 'point', 'timing', 'time_from', 'time_to', 'evaluate', 'comment', 'total_evaluate', 'timestamp'],
        )
        if not result_file.exists():
            result_df.to_csv(result_file, index=False, sep='\t')
        else:
            prev_result_df = pd.read_csv(result_file, sep='\t')
            result_df = pd.concat([result_df, prev_result_df], axis=0)
            result_df.to_csv(result_file, index=False, sep='\t')

    if result_file.exists():

        st.text('\n\nあなたの過去の評価は以下です。')
        disp_targets = ['total_evaluate', 'point', 'timing', 'time_from', 'time_to', 'evaluate', 'comment', 'timestamp']
        eval_df = pd.read_csv(result_file, sep='\t')
        eval_df = eval_df[disp_targets]
        eval_df = eval_df.rename(columns = {
            'total_evaluate': '総評',
            'point': 'ポイント',
            'timing': 'タイミング',
            'time_from': '開始時間',
            'time_to': '終了時間',
            'evaluate': '評価',
            'comment': 'コメント',
            'timestamp': '評価時刻'
            })

        st.dataframe(eval_df)

if __name__ == '__main__':
    main()
