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
/* 全局页面纯白背景，覆盖所有外层深色 */
.stApp {
    background-color: #FFFFFF !important;
}
/* 清除所有列的背景色（解决左右分栏蓝底色） */
div[data-testid="stHorizontalBlock"] > div {
    background: transparent !important;
}
div[data-testid="stColumn"] {
    background: transparent !important;
}
/* 主内容容器字体放大 */
.block-container {
    font-size:18px !important;
}
.block-container h1 {
    font-size:32px !important;
}
.block-container h2 {
    font-size:26px !important;
}
.block-container h3 {
    font-size:22px !important;
}
/* 原生顶部header隐藏 */
header {
    visibility:hidden !important;
}
/* ========== 自定义导航栏 ========== */
.nav-wrap{
    width:100%;
    padding:15px 2rem;
    border-bottom:4px solid #2563eb; /*蓝色底条*/
    display:flex;
    align-items:center;
    gap:24px;
    box-sizing:border-box;
}
.nav-item{
    font-size:19px;
    font-weight:600;
    color:#222;
    cursor:pointer;
}
.nav-item:hover{
    color:#2563eb;
}
.nav-logout{
    margin-left:auto;
}
</style>
""",unsafe_allow_html=True)

# 导航栏HTML（纯flex，左对齐，不受streamlit列影响）
st.markdown("""
<div class="nav-wrap">
    <div class="nav-item" onclick="window.location.search='?page=线上编码工具'">线上编码工具</div>
    <div class="nav-item" onclick="window.location.search='?page=利润测算'">利润测算</div>
    <div class="nav-item nav-logout" onclick="window.location.search='?logout=1'">退出登录</div>
</div>
""",unsafe_allow_html=True)

/* 登录卡片：固定宽度，居中，圆角+阴影，参考图样式 */
.login-card{
    background:#ffffff;
    box-shadow: 0 3px 9px rgba(0,0,0,0.12);
    border-radius:6px;
    padding:12px;
    width: 520px;
    margin: 12vh auto 0 auto;
}

.login-title{
    font-size:12px;
    font-weight:bold;
    color:#111827;
    display:flex;
    align-items:center;
    gap:3px;
}
.login-subtitle{
    color:#555;
    font-size:6px;
    margin-bottom:12px;
}

/* ✅ 关键：限制输入框最大宽度，不让撑满屏幕 */
.login-card .stTextInput {
    max-width:60px !important;
}
.login-card .stButton {
    max-width:60px !important;
}

/* 登录按钮样式，蓝色和参考图一致 */
.login-card button {
    background-color:#2b78e4 !important;
    color:white !important;
}

/* 导航按钮（登录后页面） */
div.stButton > button {
    width:100%;
    height:12px;
    font-size:4px;
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
    st.markdown("<span style='color:#666;font-size:6px;'>使用管理员分配的账号进入系统</span>", unsafe_allow_html=True)
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
    st.markdown("""
    <style>
    .stApp {
        background: #ffffff !important;
    }

    .custom-nav-bar {
        background-color: #ffffff;
        border-bottom: 3px solid #2b78e4;
        padding: 14px 24px;
        display: flex;
        align-items: center;
        gap: 18px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }

    .main .block-container {
        font-size: 17px;
    }

    .main h1 {
        font-size: 30px;
    }

    .main h2 {
        font-size: 24px;
    }

    header {visibility:hidden;}
    </style>
    """, unsafe_allow_html=True)

    # 顶部蓝色条痕导航区
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1,1,1,8])

    with nav_col1:
        if st.button("线上编码工具"):
            st.session_state.page = "线上编码工具"
            st.rerun()

    with nav_col2:
        if st.button("利润测算"):
            st.session_state.page = "利润测算"
            st.rerun()

    with nav_col4:
        if st.button("退出登录"):
            st.session_state.login_ok = False
            st.rerun()

    st.divider()

    if st.session_state.page == "线上编码工具":
        import page1
        page1.run()
    elif st.session_state.page == "利润测算":
        import page2
        page2.run()
