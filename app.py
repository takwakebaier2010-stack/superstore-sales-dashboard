import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard Ventes Superstore", page_icon="📊", layout="wide")

PRIMARY = "#10B981"
DARK = "#047857"
LIGHT = "#6EE7B7"
POSITIVE = "#10B981"
NEGATIVE = "#EF4444"
TEXT = "#065F46"

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

    html, body, .stApp {font-family: 'Poppins', sans-serif;}

    .stApp {
        background: linear-gradient(135deg, #ECFDF5 0%, #FFFFFF 50%, #D1FAE5 100%);
        background-attachment: fixed;
    }
    header[data-testid="stHeader"] {background: transparent;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .block-container {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 28px;
        padding: 2rem 2.2rem !important;
        margin-top: 1rem;
        margin-bottom: 1rem;
        max-width: 1400px;
        box-shadow: 0 20px 50px rgba(16, 185, 129, 0.12);
    }

    section[data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(14px);
        border-right: 1px solid rgba(167, 243, 208, 0.6);
    }
    section[data-testid="stSidebar"] > div {background: transparent;}

    .brand {font-size: 1.3rem; font-weight: 700; color: #059669; margin-bottom: 1rem;}
    .brand span {font-size: 0.8rem; font-weight: 400; color: #6B8F7E;}

    .hello h1 {font-size: 2.1rem; font-weight: 700; color: #064E3B; margin: 0; padding: 0;}
    .hello p {color: #5B8A74; margin: 0.2rem 0 1.2rem 0;}

    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #10B981 0%, #047857 100%);
        border-radius: 20px;
        padding: 1.1rem 1.3rem;
        box-shadow: 0 10px 25px rgba(5, 150, 105, 0.30);
    }
    div[data-testid="stMetric"] * {color: white !important;}
    div[data-testid="stMetricValue"] {font-weight: 600;}

    div[data-testid="stPlotlyChart"] {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(167, 243, 208, 0.6);
        border-radius: 20px;
        padding: 0.5rem;
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.10);
    }
    div[data-testid="stDataFrame"] {border-radius: 16px; overflow: hidden;}

    button[data-baseweb="tab"] {font-weight: 500;}

    .stDownloadButton button {
        background: linear-gradient(135deg, #10B981, #047857);
        border: none;
        border-radius: 12px;
    }
    .stDownloadButton button, .stDownloadButton button p {color: white !important;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    df = pd.read_csv("data/superstore.csv", encoding="latin-1")
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
    return df


def style_fig(fig, height=360):
    fig.update_layout(
        template="plotly_white",
        height=height,
        margin=dict(l=10, r=10, t=60, b=10),
        title_font=dict(size=16, color=TEXT),
        font=dict(family="Poppins, sans-serif", color=TEXT),
        legend=dict(title_text="", orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    fig.update_xaxes(title_text="", showgrid=False)
    fig.update_yaxes(title_text="", gridcolor="rgba(6, 95, 70, 0.12)")
    return fig


df = load_data()

st.markdown(
    f"""
    <div class="hello">
        <h1>Dashboard des ventes</h1>
        <p>Superstore · commandes de {df["Year"].min()} à {df["Year"].max()}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    '<div class="brand">🟢 Superstore<br><span>Sales Analytics</span></div>',
    unsafe_allow_html=True,
)
st.sidebar.header("Filtres")
all_years = sorted(df["Year"].unique().tolist())
all_regions = sorted(df["Region"].unique().tolist())
all_categories = sorted(df["Category"].unique().tolist())

years = st.sidebar.multiselect("Année", all_years, default=all_years)
regions = st.sidebar.multiselect("Région", all_regions, default=all_regions)
categories = st.sidebar.multiselect("Catégorie", all_categories, default=all_categories)

filtered = df[
    df["Year"].isin(years)
    & df["Region"].isin(regions)
    & df["Category"].isin(categories)
]

if filtered.empty:
    st.warning("Aucune donnée avec ces filtres.")
    st.stop()

total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
nb_orders = filtered["Order ID"].nunique()
margin = total_profit / total_sales * 100

c1, c2, c3, c4 = st.columns(4)
c1.metric("Ventes totales", f"{total_sales:,.0f} $")
c2.metric("Profit total", f"{total_profit:,.0f} $")
c3.metric("Commandes", f"{nb_orders:,}")
c4.metric("Marge", f"{margin:.1f} %")

st.write("")
tab1, tab2, tab3 = st.tabs(["Vue d'ensemble", "Produits et clients", "Données"])

with tab1:
    monthly = filtered.groupby("Month", as_index=False)[["Sales", "Profit"]].sum()
    fig_month = px.area(
        monthly, x="Month", y=["Sales", "Profit"],
        title="Ventes et profit par mois", line_shape="spline",
        color_discrete_sequence=[PRIMARY, LIGHT],
    )
    fig_month.update_traces(stackgroup=None, fill="tozeroy")
    fig_month.data[0].fillcolor = "rgba(16, 185, 129, 0.30)"
    fig_month.data[1].fillcolor = "rgba(110, 231, 183, 0.50)"
    st.plotly_chart(style_fig(fig_month, 400), width="stretch")

    left, right = st.columns(2)

    by_cat = filtered.groupby("Category", as_index=False)[["Sales", "Profit"]].sum()
    fig_cat = px.bar(
        by_cat, x="Category", y=["Sales", "Profit"], barmode="group",
        title="Ventes et profit par catégorie", text_auto=".2s",
        color_discrete_sequence=[DARK, LIGHT],
    )
    left.plotly_chart(style_fig(fig_cat), width="stretch")

    by_region = filtered.groupby("Region", as_index=False)["Profit"].sum()
    fig_region = px.bar(
        by_region, x="Region", y="Profit", title="Profit par région",
        text_auto=".2s", color_discrete_sequence=[PRIMARY],
    )
    right.plotly_chart(style_fig(fig_region), width="stretch")

with tab2:
    left2, right2 = st.columns(2)

    by_sub = (
        filtered.groupby("Sub-Category", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit")
    )
    by_sub["Résultat"] = by_sub["Profit"].apply(lambda x: "Profit" if x >= 0 else "Perte")
    fig_sub = px.bar(
        by_sub, x="Profit", y="Sub-Category", orientation="h",
        color="Résultat", title="Profit par sous-catégorie",
        color_discrete_map={"Profit": POSITIVE, "Perte": NEGATIVE},
    )
    left2.plotly_chart(style_fig(fig_sub, 460), width="stretch")

    top_products = (
        filtered.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .nlargest(10, "Sales")
        .sort_values("Sales")
    )
    top_products["Product Name"] = top_products["Product Name"].str.slice(0, 35)
    fig_top = px.bar(
        top_products, x="Sales", y="Product Name", orientation="h",
        title="Top 10 produits par ventes", color_discrete_sequence=[PRIMARY],
    )
    right2.plotly_chart(style_fig(fig_top, 460), width="stretch")

    left3, right3 = st.columns(2)

    by_segment = filtered.groupby("Segment", as_index=False)["Sales"].sum()
    fig_seg = px.pie(
        by_segment, names="Segment", values="Sales", hole=0.55,
        title="Ventes par segment de clients",
        color_discrete_sequence=[PRIMARY, LIGHT, DARK],
    )
    left3.plotly_chart(style_fig(fig_seg), width="stretch")

    top_customers = (
        filtered.groupby("Customer Name", as_index=False)["Sales"]
        .sum()
        .nlargest(10, "Sales")
        .sort_values("Sales")
    )
    fig_cust = px.bar(
        top_customers, x="Sales", y="Customer Name", orientation="h",
        title="Top 10 clients par ventes", color_discrete_sequence=[DARK],
    )
    right3.plotly_chart(style_fig(fig_cust), width="stretch")

with tab3:
    st.caption(f"{len(filtered):,} lignes après filtres")
    st.dataframe(filtered.drop(columns=["Month"]).head(200), width="stretch")
    csv = filtered.drop(columns=["Month"]).to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Télécharger les données filtrées (CSV)",
        csv, "superstore_filtre.csv", "text/csv",
    )