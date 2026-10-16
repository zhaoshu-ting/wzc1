import streamlit as st

# ========== 账号配置 ==========
USER_ACCOUNT = "wzc"
USER_PASSWORD = "123"

# 初始化session
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False
if "page" not in st.session_state:
    st.session_state.page = "线上编码工具"

# ===================== 页面CSS全局样式 =====================
st.markdown("""
<style>
/* 隐藏页面顶部多余白色空框 */
.block-container > div:first-child {
    display: none;
}
/* 页面整体背景 左右分块深蓝色+白色 */
.stApp {
    background: linear-gradient(90deg, #0f3460 42%, #ffffff 42%);
}

/* 隐藏默认streamlit顶部栏 */
header {visibility:hidden;}

/* 隐藏页面顶部多余白色空框 */
.block-container > div:first-child {
    display: none;
}

/* 登录卡片：减少padding，缩短高度 */
.login-card{
    background:#ffffff;
    border-radius:18px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.08);
    padding:24px 28px;
    max-width:420px;
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
    margin-bottom:16px;
}

/* 导航按钮样式（登录成功后的顶部导航高亮） */
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
    st.markdown('<div class="login-title"><span style="background:#2b78e4;color:white;border-radius:8px;width:36px;height:36px;text-align:center;line-height:36px;">工</span>工具箱</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">商品资料与线上编码管理平台</div>', unsafe_allow_html=True)
    st.markdown("**登录系统**")
    st.markdown("<span style='color:#666;font-size:14px;'>使用管理员分配的账号进入系统</span>", unsafe_allow_html=True)
    st.divider()

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

# ========== 【重点！全部后台页面都放在这个else里面】 ==========
else:
    # 顶部导航栏布局
    nav_col1, nav_col2, nav_col3 = st.columns([1,1,1])

    # 导航按钮1：线上编码工具
    with nav_col1:
        if st.session_state.page == "线上编码工具":
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        btn_code = st.button("线上编码工具")
        if st.session_state.page == "线上编码工具":
            st.markdown('</div>', unsafe_allow_html=True)
        if btn_code:
            st.session_state.page = "线上编码工具"
            st.rerun()

    # 导航按钮2：利润测算
    with nav_col2:
        if st.session_state.page == "利润测算":
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        btn_profit = st.button("利润测算")
        if st.session_state.page == "利润测算":
            st.markdown('</div>', unsafe_allow_html=True)
        if btn_profit:
            st.session_state.page = "利润测算"
            st.rerun()

    # 导航按钮3：退出登录
    with nav_col3:
        logout_btn = st.button("退出登录")
        if logout_btn:
            st.session_state.login_ok = False
            st.rerun()

    st.divider()

    # 页面渲染
    if st.session_state.page == "线上编码工具":
        import page1
        page1.run()
    elif st.session_state.page == "利润测算":
        import page2
        page2.run()
