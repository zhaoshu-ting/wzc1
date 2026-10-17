import streamlit as st

# ==========账号配置==========
USER_ACCOUNT = "wzc"
USER_PASSWORD = "12345678"

# ==========初始化session==========
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False
if "page" not in st.session_state:
    st.session_state.page = "线上编码工具"

# ================== 【登录页面】==================
if not st.session_state.login_ok:
    # 只给登录页用的CSS，不影响登录后页面！
    st.markdown("""
    <style>
    .login-card{ background:#ffffff; box-shadow: 0 3px 9px rgba(0,0,0,0.12); border-radius:6px; padding:12px; width: 520px; margin: 12vh auto 0 auto;}
    .login-title{ font-size:22px; font-weight:bold; color:#111827; display:flex; align-items:center; gap:3px; }
    .login-subtitle{ color:#555; font-size:16px; margin-bottom:12px; }
    .login-card .stTextInput { max-width:450px !important; }
    .login-card .stButton { max-width:200px !important; }
    .login-card button { background-color:#2b78e4 !important; color:white !important; }
    </style>
    """,unsafe_allow_html=True)
    # 登录页面UI
    st.markdown('<div class="login-card">',unsafe_allow_html=True)
    st.markdown('<div class="login-title">登录系统</div>',unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">使用管理员分配的账号进入系统</div>',unsafe_allow_html=True)
    username = st.text_input("账号")
    pwd = st.text_input("密码",type="password")
    if st.button("登录"):
        if username == USER_ACCOUNT and pwd == USER_PASSWORD:
            st.session_state.login_ok = True
            st.rerun()
        else:
            st.error("账号密码错误")
    st.markdown("</div>",unsafe_allow_html=True)

# ================== 【登录成功之后 单独写CSS！！！】==================
else:
    # ===== 登录后专属CSS，在这里写！！ =====
    st.markdown("""
    <style>
    /* 最外层容器，解决左右深色背景！！这是关键 */
    div[data-testid="stAppViewContainer"]{
        background-color: #FFFFFF !important;
    }
    .stApp {
        background-color: #FFFFFF !important;
    }
    /* 清除所有分栏、列的背景，全部透明 */
    div[data-testid="stHorizontalBlock"] > div {
        background: transparent !important;
    }
    div[data-testid="stColumn"] {
        background: transparent !important;
    }
    /* 主内容字体放大 */
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
    /* 隐藏原生顶部header */
    header {
        visibility:hidden !important;
    }
    /* 自定义导航栏 */
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

    # 导航栏HTML
    st.markdown("""
    <div class="nav-wrap">
        <div class="nav-item" onclick="window.location.search='?page=线上编码工具'">线上编码工具</div>
        <div class="nav-item" onclick="window.location.search='?page=利润测算'">利润测算</div>
        <div class="nav-item nav-logout" onclick="window.location.search='?logout=1'">退出登录</div>
    </div>
    """,unsafe_allow_html=True)

    # 处理参数
    query_params = st.query_params
    if "page" in query_params:
        page = query_params["page"]
        if page in ["线上编码工具", "利润测算"]:
            st.session_state.page = page
            st.rerun()
    if "logout" in query_params:
        st.session_state.login_ok = False
        st.rerun()

    st.divider()
    # 加载页面
    if st.session_state.page == "线上编码工具":
        import page1
        page1.run()
    elif st.session_state.page == "利润测算":
        import page2
        page2.run()
