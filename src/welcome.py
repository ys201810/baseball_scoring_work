# coding=utf-8
import os
import streamlit as st
from pathlib import Path
base_path = Path.cwd().parent


def main():
    st.set_page_config(layout="wide")
    st.markdown("## 投打フォームへの採点画面イメージ画面")

    if st.button('評価をリセットする'):
        db_path = base_path / "db"
        for result_file in list(db_path.glob("*.csv")):
            os.remove(result_file)
            st.text('全ての評価を削除しました。')

    st.markdown("#### メモ")
    st.markdown("・動画が多くなったらstreamlitでは難しそう")
    st.markdown("・一気に評価させたいが、streamlitだと1つ1つの評価になってしまう・・・")
    st.markdown("・評価の削除が欲しい")
    st.markdown("・みんなの評価を1度に表示する機能")
    st.markdown("・投球タイミングの正確なリストが欲しい")
    st.markdown("・動画のサイズの指定がstreamlitの機能にない")

if __name__ == '__main__':
    main()
