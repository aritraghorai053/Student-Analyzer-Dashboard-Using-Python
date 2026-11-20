
import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# 2. LOAD DATA
# ==========================================

@st.cache_data
def load_data():
    return pd.read_csv("student_data.csv")

df = load_data()

# Check required columns
required_columns = [
    "Student_ID", "Roll_No", "Student_Name",
    "Department", "Total", "Average",
    "Percentage", "Grade"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    st.error(f"Missing columns: {missing_columns}")
    st.info("Run analysis.py first to generate Total, Average, Percentage and Grade.")
    st.stop()

# ==========================================
# 3. HEADER
# ==========================================

st.title("🎓 Student Performance Analyzer")

st.markdown(
    "### Academic Performance Analytics Dashboard"
)

st.caption(
    "Analyze student results, compare departments and track academic performance."
)

st.divider()

# ==========================================
# 4. SIDEBAR FILTERS
# ==========================================

st.sidebar.title("🎯 Dashboard Filters")

departments = ["All"] + sorted(
    df["Department"].dropna().unique().tolist()
)

selected_department = st.sidebar.selectbox(
    "Select Department",
    departments
)

if selected_department == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["Department"] == selected_department
    ].copy()

st.sidebar.divider()

st.sidebar.write("📊 Dataset Information")
st.sidebar.write("Total Records:", len(df))
st.sidebar.write("Departments:", df["Department"].nunique())

# ==========================================
# 5. KPI CARDS
# ==========================================

st.subheader("📌 Overall Statistics")

total_students = len(filtered_df)

average_marks = (
    filtered_df["Average"].mean()
    if total_students else 0
)

highest_marks = (
    filtered_df["Total"].max()
    if total_students else 0
)

passed_students = len(
    filtered_df[filtered_df["Grade"] != "F"]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Students",
    total_students
)

col2.metric(
    "Average Marks",
    f"{average_marks:.2f}"
)

col3.metric(
    "Highest Total",
    f"{highest_marks:.0f}"
)

col4.metric(
    "Passed Students",
    passed_students
)

st.divider()

# Stop if the selected filter has no records
if filtered_df.empty:
    st.warning("No student records found.")
    st.stop()

# ==========================================
# 6. DEPARTMENT PERFORMANCE
# ==========================================

st.subheader("📊 Department Performance")

department_avg = (
    filtered_df.groupby("Department")["Average"]
    .mean()
    .reset_index()
)

fig1 = px.bar(
    department_avg,
    x="Department",
    y="Average",
    title="Department-wise Average Marks",
    text_auto=".2f",
    labels={
        "Average": "Average Marks",
        "Department": "Department"
    }
)

fig1.update_layout(
    yaxis_range=[0, 100],
    template="plotly_white"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# ==========================================
# 7. GRADE DISTRIBUTION
# ==========================================

st.subheader("🏆 Grade Distribution")

grade_counts = (
    filtered_df["Grade"]
    .value_counts()
    .rename_axis("Grade")
    .reset_index(name="Students")
)

fig2 = px.pie(
    grade_counts,
    names="Grade",
    values="Students",
    title="Student Grade Distribution",
    hole=0.4
)

fig2.update_layout(
    template="plotly_white"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# ==========================================
# 8. TOP 10 STUDENTS
# ==========================================

st.subheader("🥇 Top 10 Students")

top_students = (
    filtered_df.sort_values(
        by="Total",
        ascending=False
    ).head(10)
)

fig3 = px.bar(
    top_students.sort_values("Total"),
    x="Total",
    y="Student_Name",
    orientation="h",
    title="Top 10 Students by Total Marks",
    text="Total",
    labels={
        "Total": "Total Marks",
        "Student_Name": "Student Name"
    }
)

fig3.update_layout(
    template="plotly_white"
)

st.plotly_chart(
    fig3,
    width="stretch"
)

# ==========================================
# 9. SUBJECT-WISE PERFORMANCE
# ==========================================

st.subheader("📚 Subject-wise Average Marks")

subject_cols = [
    col
    for col in filtered_df.select_dtypes(include="number").columns
    if col not in ["Total", "Average", "Percentage"]
]

if subject_cols:

    subject_avg = (
        filtered_df[subject_cols]
        .mean()
        .reset_index()
    )

    subject_avg.columns = [
        "Subject",
        "Average Marks"
    ]

    fig4 = px.bar(
        subject_avg,
        x="Subject",
        y="Average Marks",
        title="Subject-wise Average Marks",
        text_auto=".2f"
    )

    fig4.update_layout(
        yaxis_range=[0, 100],
        template="plotly_white"
    )

    st.plotly_chart(
        fig4,
        width="stretch"
    )

# ==========================================
# 10. STUDENT RECORDS
# ==========================================

st.subheader("📋 Student Records")

search = st.text_input(
    "🔍 Search by Student Name or Roll Number"
)

display_df = filtered_df.copy()

if search:
    display_df = display_df[
        display_df["Student_Name"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        display_df["Roll_No"].astype(str).str.contains(
            search,
            case=False,
            na=False
        )
    ]

st.dataframe(
    display_df[
        [
            "Student_ID",
            "Roll_No",
            "Student_Name",
            "Department",
            "Total",
            "Average",
            "Percentage",
            "Grade"
        ]
    ].sort_values(
        "Total",
        ascending=False
    ),
    width="stretch",
    hide_index=True
)

# ==========================================
# 11. DOWNLOAD CSV
# ==========================================

st.subheader("📥 Download Report")

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Student Performance CSV",
    data=csv,
    file_name="student_performance_report.csv",
    mime="text/csv"
)

# ==========================================
# 12. FOOTER
# ==========================================

st.divider()

st.markdown(
    "<center>🎓 Student Performance Analyzer | "
    "Built with Python, Pandas, Plotly and Streamlit</center>",
    unsafe_allow_html=True
)
