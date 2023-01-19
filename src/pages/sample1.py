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
from utils import selectValues

def main():
    movie_name = "sample1.mov"
    video_path = base_path / "data"
    video_file = video_path / movie_name
    select_values = selectValues()

    st.markdown(f"#### ①　評価者の氏名を入力")
    user = st.text_input('評価者の氏名', '佐藤太郎')
    result_file = base_path / "db" / f"{user}_{movie_name.split('.')[0]}.csv"

    st.markdown(f"#### ②　動画を確認")

    with open(video_file, 'rb') as inf:
        video_bytes = inf.read()
        container = set_slider()
        container.video(data=video_bytes)

    st.markdown(f"#### ③　確認した動画を評価")
    point = st.selectbox('良い悪いを判断したポイント:', select_values.points)
    eval_kind = st.selectbox('評価の観点:', select_values.eval_kinds)

    timing = st.selectbox('ピッチングのタイミング：', select_values.timings)
    time_from = st.text_input('動画内の開始時間', '00:00')
    time_to = st.text_input('動画内の終了時間', '00:00')
    evaluate = st.selectbox('注目したポイントの評価：', select_values.evaluates)
    comment = st.text_input('評価ポイントに対するコメント', '投げ終わりに腕を振り抜き切れていない。')
    total_evalate = st.selectbox('総評(10段階)：', select_values.total_evaluates)

    if st.button('評価を追加する'):
        data = [
            movie_name,
            user,
            point,
            eval_kind,
            timing,
            time_from,
            time_to,
            evaluate,
            comment,
            total_evalate,
            datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        ]
        result_df = pd.DataFrame(
            data = [data],
            columns=['movie', 'user', 'point', 'eval_kind', 'timing', 'time_from', 'time_to', 'evaluate', 'comment', 'total_evaluate', 'timestamp'],
        )
        if not result_file.exists():
            result_df.to_csv(result_file, index=False, sep='\t')
        else:
            prev_result_df = pd.read_csv(result_file, sep='\t')
            result_df = pd.concat([result_df, prev_result_df], axis=0)
            result_df.to_csv(result_file, index=False, sep='\t')

    if result_file.exists():

        st.text('\n\nあなたの過去の評価は以下です。')
        disp_targets = ['total_evaluate', 'point', 'eval_kind', 'timing', 'time_from', 'time_to', 'evaluate', 'comment', 'timestamp']
        eval_df = pd.read_csv(result_file, sep='\t')
        eval_df = eval_df[disp_targets]
        eval_df = eval_df.rename(columns = {
            'total_evaluate': '総評',
            'point': 'ポイント',
            'eval_kind': '評価の観点',
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
