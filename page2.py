import streamlit as st

def _page():
    st.title("利润投产测算")
    top_col1, top_col2 = st.columns([8,1])
    with top_col1:
        st.subheader("投产平衡点")
        st.info("投产广告后台至少需要达到多少支付投产比，才能覆盖退款与全部经营成本。\n投产比按`支付销售额 ÷ 推广费用`计算。退款单不产生比例费用，衣服成本视为可收回，但每单固定费用仍会损失。")
    with top_col2:
        if st.button("重置"):
            if "sell_price" in st.session_state:
                del st.session_state["sell_price"]
            if "cloth_cost" in st.session_state:
                del st.session_state["cloth_cost"]
            if "refund_rate" in st.session_state:
                del st.session_state["refund_rate"]
            if "tax_rate" in st.session_state:
                del st.session_state["tax_rate"]
            if "extra_fee" in st.session_state:
                del st.session_state["extra_fee"]
            st.rerun()

    col_left, col_right = st.columns([1,1])
    with col_left:
        st.markdown("#### 输入基础数据")
        sell_price = st.number_input("售卖价", min_value=0.0, value=st.session_state.get("sell_price",0.0), step=1.0, key="sell_price")
        cloth_cost = st.number_input("衣服成本", min_value=0.0, value=st.session_state.get("cloth_cost",0.0), step=1.0, key="cloth_cost")
        refund_rate = st.number_input("退款率(%)", min_value=0.0, max_value=100.0, value=st.session_state.get("refund_rate",0.0), step=0.1, key="refund_rate")
        tax_rate = st.number_input("税费点数(%)", min_value=0.0, max_value=100.0, value=st.session_state.get("tax_rate",8.0), step=0.1, key="tax_rate")
        extra_fee = st.number_input("杂费", min_value=0.0, value=st.session_state.get("extra_fee",2.0), step=0.1, key="extra_fee")

        st.divider()
        st.markdown("##### 计算公式")
        st.code("""
可投推广费 = (1 − 退款率) × (售卖价 × (0.885 − 税费点数/100) − 衣服成本) − (7.20 + 杂费)
投产平衡点 = 售卖价 ÷ 可投推广费
        """)

    with col_right:
        st.markdown("#### 测算结果")
        if sell_price > 0 and cloth_cost>0:
            r = refund_rate / 100
            tax = tax_rate / 100
            profit_per_order = (1 - r) * (sell_price * (0.885 - tax) - cloth_cost) - (7.2 + extra_fee)
            if profit_per_order <= 0:
                st.error("❌ 每单毛利为负，无论投产多少都会亏损！")
                break_even = None
            else:
                break_even = sell_price / profit_per_order
                st.success(f"✅ 可投推广费：{profit_per_order:.2f} 元/单")
                st.success(f"✅ 投产平衡点：{break_even:.3f}")
                st.caption(f"含义：投产 ≥ {break_even:.3f} 才不亏损")
        else:
            st.info("填写完整数据后自动计算")

    st.divider()
    st.subheader("实际投产盈亏测算")
    st.caption("实际投产比 = 退款前支付销售额 ÷ 推广费。按同一商品、每单一估算，不另计达人佣金。")

    use_param_btn = st.button("沿用上方成本和退款率")
    if use_param_btn:
        st.success("✅ 已读取上方售卖价、衣服成本、退款率、税费、杂费参数")

    c1,c2 = st.columns(2)
    with c1:
        real_roi = st.number_input("实际投产比", min_value=0.0, value=0.0, step=0.1)
    with c2:
        real_ad_cost = st.number_input("实际推广费", min_value=0.0, value=0.0, step=1.0)

    if st.button("计算实际盈亏"):
        if sell_price <=0 or cloth_cost <=0:
            st.warning("请先填写上方基础售卖价和衣服成本！")
        else:
            if real_roi <=0:
                st.warning("投产比必须大于0")
            else:
                pay_sales = real_roi * real_ad_cost
                order_num = pay_sales / sell_price
                r = refund_rate /100
                tax = tax_rate /100
                single_profit = (1 - r) * (sell_price * (0.885 - tax) - cloth_cost) - (7.2 + extra_fee)
                total_profit = order_num * single_profit - real_ad_cost
                if total_profit>0:
                    st.success(f"✅ 预估总盈利：{total_profit:.2f} 元")
                else:
                    st.error(f"❌ 预估总亏损：{abs(total_profit):.2f} 元")

def run():
    st.session_state.setdefault("sell_price",0.0)
    st.session_state.setdefault("cloth_cost",0.0)
    st.session_state.setdefault("refund_rate",0.0)
    st.session_state.setdefault("tax_rate",8.0)
    st.session_state.setdefault("extra_fee",2.0)
    _page()
