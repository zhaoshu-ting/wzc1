import streamlit as st

# ========== 登录账号密码，自行修改 ==========
USER_ACCOUNT = "admin"
USER_PASSWORD = "12345678"

# 初始化登录状态
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False

if not st.session_state.login_ok:
    st.set_page_config(page_title="工具箱-登录", layout="centered")

    # 自定义CSS：深蓝色对角渐变背景、登录白色卡片，和你截图风格一致
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #082040 0%, #0b3060 45%, #ffffff 45%, #ffffff 100%);
    }
    .login-card{
        width:440px;
        margin: 70px auto;
        padding:32px;
        background:#ffffff;
        border-radius:14px;
        box-shadow: 0 8px 32px rgba(0,20,60,0.15);
    }
    .logo-title{
        display:flex;
        align-items:center;
        gap:10px;
        font-size:26px;
        font-weight:bold;
        color:#112244;
    }
    .logo-icon{
        width:36px;
        height:36px;
        background:#2478e0;
        border-radius:8px;
        color:white;
        text-align:center;
        line-height:36px;
        font-weight:bold;
    }
    .sub-desc{
        color:#666666;
        font-size:14px;
        margin-bottom:24px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="logo-title"><span class="logo-icon">工</span>工具箱</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-desc">商品资料与线上编码管理平台</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#444; font-size:15px;'>登录系统<br><span style='font-size:13px;color:#777'>使用管理员分配的账号进入系统</span></p>", unsafe_allow_html=True)

    username = st.text_input("*登录账号", placeholder="支持中文、字母或数字，不能包含空格")
    pwd = st.text_input("*密码", placeholder="至少8位", type="password")
    login_btn = st.button("登录", type="primary", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if login_btn:
        if username == USER_ACCOUNT and pwd == USER_PASSWORD:
            st.session_state.login_ok = True
            st.rerun()
        else:
            st.error("账号或密码错误！")

# ========== 登录成功后系统主页【顶部横向导航 + 选中高亮】 ==========
else:
    st.set_page_config(page_title="商品工具箱", layout="wide")

    # 导航栏样式CSS，实现选中高亮
    st.markdown("""
    <style>
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

    # 初始化当前页面
    if "page" not in st.session_state:
        st.session_state.page = "线上编码工具"

    # 顶部导航布局
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1,1,1,6])

    # 按钮1：班尼路商品资料
    with nav_col1:
        if st.session_state.page == "班尼路商品资料":
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        btn_ban = st.button("班尼路商品资料")
        if st.session_state.page == "班尼路商品资料":
            st.markdown('</div>', unsafe_allow_html=True)
        if btn_ban:
            st.session_state.page = "班尼路商品资料"
            st.rerun()

    # 按钮2：线上编码工具
    with nav_col2:
        if st.session_state.page == "线上编码工具":
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        btn_code = st.button("线上编码工具")
        if st.session_state.page == "线上编码工具":
            st.markdown('</div>', unsafe_allow_html=True)
        if btn_code:
            st.session_state.page = "线上编码工具"
            st.rerun()

    # 按钮3：利润投产测算
    with nav_col3:
        if st.session_state.page == "利润投产测算":
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        btn_profit = st.button("利润投产测算")
        if st.session_state.page == "利润投产测算":
            st.markdown('</div>', unsafe_allow_html=True)
        if btn_profit:
            st.session_state.page = "利润投产测算"
            st.rerun()

    # 右上角退出登录
    with nav_col4:
        logout_btn = st.button("退出登录")
        if logout_btn:
            st.session_state.login_ok = False
            st.rerun()

    st.divider()

    # 页面渲染
    if st.session_state.page == "班尼路商品资料":
        st.title("班尼路商品资料")
        st.info("该模块待开发，可以后续添加功能")
    elif st.session_state.page == "线上编码工具":
        import page1
        page1.run()
    elif st.session_state.page == "利润投产测算":
        import page2
        page2.run()
