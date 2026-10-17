import streamlit as st
import pandas as pd
from io import BytesIO

def run():
    # ========= 新增这一段！！放在最开头 =========
    st.markdown("""
    <style>
    /* 清除本页面所有列背景，变成透明 */
    div[data-testid="stHorizontalBlock"] > div {
        background-color: transparent !important;
    }
    div[data-testid="stColumn"]{
        background: transparent !important;
    }
    .stAppViewContainer{
        background:#ffffff !important;
    }
    .block-container{
        font-size:18px !important;
    }
    </style>
    """,unsafe_allow_html=True)

    # 下面是你原来的代码不动
    st.title("线上编码工具")
    st.markdown("上传线上商品表，按商品编码匹配成本价，生成A表和B表。")
    col1, col2 = st.columns([2,1])
    ...

    st.title("线上编码工具")
    st.markdown("上传线上商品表，按商品编码匹配成本价，生成A表和B表。")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("线上商品表格")
        st.info("必传，作为生成A表和B表的主文件。仅支持 .xlsx")
        file_online = st.file_uploader("点击或拖拽线上商品Excel到这里", type=["xlsx"], key="f1")

    with col2:
        st.subheader("成本价文件")
        st.info("上传后会强校验，避免生成错误价格。只读取商品id、档口名称、款号、成本价四列")
        file_cost = st.file_uploader("点击或拖拽成本价Excel到这里", type=["xlsx"], key="f2")

    style_type = st.radio("款式类型（加绒自动覆盖）", ["薄", "厚"], horizontal=True)
    st.caption("编码预览：常规:款式编码-厚-颜色-码数；加绒:款式编码-绒-颜色加绒-码数")

    run_btn = st.button("开始处理", type="primary")

    def export_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="data")
        return output.getvalue()

    if run_btn:
        if not file_online or not file_cost:
            st.warning("⚠️ 请同时上传【线上商品表格】和【成本价文件】两个Excel！")
        else:
            df_online = pd.read_excel(file_online)
            df_cost = pd.read_excel(file_cost)

            # 检查必要列
            required_left = ["商品id", "款号"]
            required_right = ["商品id", "款号", "档口名称", "成本价"]
            miss_left = [c for c in required_left if c not in df_online.columns]
            miss_right = [c for c in required_right if c not in df_cost.columns]
            if miss_left:
                st.error(f"❌ 线上商品表缺少列：{miss_left}")
                st.stop()
            if miss_right:
                st.error(f"❌ 成本价文件缺少列：{miss_right}")
                st.stop()

            df_merge = pd.merge(
                df_online,
                df_cost[["商品id", "档口名称", "款号", "成本价"]],
                on=["款号", "商品id"],
                how="left"
            )

            table_A = df_merge.copy()
            table_B = df_merge[df_merge["成本价"].notna()].copy()

            st.success(f"✅ A表共生成 {len(table_A)} 条数据；B表生成 {len(table_B)} 条，{len(table_B)} 条匹配到成本价")

            a_file = export_excel(table_A)
            b_file = export_excel(table_B)
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 下载A表", data=a_file, file_name="A表_线上商品.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            with c2:
                st.download_button("📥 下载B表", data=b_file, file_name="B表_聚水潭导入.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

            with st.expander("字段来源和处理规则"):
                st.markdown("""
                - 匹配键：款号 + 商品id，两张表的这两列名称必须完全一致
                - 线上商品表必需字段：商品id、款号
                - 成本价表必需字段：商品id、款号、档口名称、成本价
                """)
