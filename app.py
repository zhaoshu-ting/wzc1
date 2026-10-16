import streamlit as st

# ========== 账号配置 ==========
USER_ACCOUNT = "wzc"
USER_PASSWORD = "12345678"

# 初始化session
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False
if "page" not in st.session_state:
    st.session_state.page = "线上编码工具"

# ===================== CSS =====================
st.markdown("""
<style>
/* 左右对半背景 */
.stApp {
    background: linear-gradient(90deg, #0f3460 42%, #ffffff 42%);
}
header {visibility:hidden;}

/* 登录卡片：固定宽度，居中，圆角+阴影，参考图样式 */
.login-card{
    background:#ffffff;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    border-radius:16px;
    padding:36px;
    width: 520px;
    margin: 12vh auto 0 auto;
}

.login-title{
    font-size:24px;
    font-weight:bold;
    color:#111827;
    display:flex;
    align-items:center;
    gap:10px;
}
.login-subtitle{
    color:#555;
    font-size:14px;
    margin-bottom:24px;
}

/* ✅ 关键：限制输入框最大宽度，不让撑满屏幕 */
.login-card .stTextInput {
    max-width:440px !important;
}
.login-card .stButton {
    max-width:440px !important;
}

/* 登录按钮样式，蓝色和参考图一致 */
.login-card button {
    background-color:#2b78e4 !important;
    color:white !important;
}

/* 导航按钮（登录后页面） */
div.stButton > button {
    width:100%;
    height:42px;
    font-size:16px;
}
.nav-active button {
    background-color:#1f6ecd !important;
    color:white !important;
}
</style>
""", unsafe_allow_html=True)


# ========== 登录页面 ==========
if not st.session_state.login_ok:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("## 登录系统")
    st.markdown("<span style='color:#666;font-size:14px;'>使用管理员分配的账号进入系统</span>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    username = st.text_input("*登录账号", placeholder="支持中文、字母或数字，不能包含空格")
    pwd = st.text_input("*密码", placeholder="至少8位", type="password")

    login_btn = st.button("登录", type="primary", use_container_width=True)
    if login_btn:
        if username == USER_ACCOUNT and pwd == USER_PASSWORD:
            st.session_state.login_ok = True
            st.rerun()
        else:
            st.error("账号或密码错误！")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 登录成功后的后台页面 ==========
else:
    nav_col1, nav_col2, nav_col3 = st.columns([1,1,1])
    with nav_col1:
        if st.session_state.page == "线上编码工具":
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        btn_code = st.button("线上编码工具")
        if st.session_state.page == "线上编码工具":
            st.markdown('</div>', unsafe_allow_html=True)
        if btn_code:
            st.session_state.page = "线上编码工具"
            st.rerun()

    with nav_col2:
        if st.session_state.page == "利润测算":
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        btn_profit = st.button("利润测算")
        if st.session_state.page == "利润测算":
            st.markdown('</div>', unsafe_allow_html=True)
        if btn_profit:
            st.session_state.page = "利润测算"
            st.rerun()

    with nav_col3:
        logout_btn = st.button("退出登录")
        if logout_btn:
            st.session_state.login_ok = False
            st.rerun()

    st.divider()

    if st.session_state.page == "线上编码工具":
        import page1
        page1.run()
    elif st.session_state.page == "利润测算":
        import page2
        page2.run()
