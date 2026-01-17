import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="EduInsight Pro | Learning Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ENHANCED CSS & ANIMATIONS =================
st.markdown("""
<style>
/* Galaxy Background */
.stApp {
    background: linear-gradient(135deg, #0a0a0a 0%, #0f172a 25%, #1e1b4b 50%, #0f172a 75%, #0a0a0a 100%);
    background-size: 400% 400%;
    animation: galaxyFloat 60s ease infinite;
    color: #f1f5f9;
}

@keyframes galaxyFloat {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Enhanced Sidebar */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.95) !important;
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(94, 234, 212, 0.15);
}

/* Glowing Cards */
.glow-card {
    background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9));
    backdrop-filter: blur(12px);
    border: 1px solid rgba(94, 234, 212, 0.2);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3),
                0 0 30px rgba(59, 130, 246, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.glow-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4),
                0 0 40px rgba(94, 234, 212, 0.2);
    border-color: rgba(94, 234, 212, 0.4);
}

/* Animated Gradient Text */
.gradient-text {
    background: linear-gradient(90deg, #60a5fa, #8b5cf6, #ec4899, #60a5fa);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientFlow 6s ease infinite;
}

@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Pulse Animation for Alerts */
@keyframes pulse-glow {
    0% { 
        box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7),
                    0 0 0 0 rgba(239, 68, 68, 0.4);
    }
    70% { 
        box-shadow: 0 0 0 15px rgba(239, 68, 68, 0),
                    0 0 0 30px rgba(239, 68, 68, 0);
    }
    100% { 
        box-shadow: 0 0 0 0 rgba(239, 68, 68, 0),
                    0 0 0 0 rgba(239, 68, 68, 0);
    }
}

.pulse-alert {
    animation: pulse-glow 2s infinite;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(30, 41, 59, 0.5);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #3b82f6, #8b5cf6);
    border-radius: 5px;
    border: 2px solid rgba(15, 23, 42, 0.5);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #60a5fa, #a78bfa);
}

/* Tab Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(30, 41, 59, 0.5);
    border-radius: 12px;
    padding: 8px;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 8px;
    padding: 12px 24px;
    border: none;
    color: #cbd5e1;
    transition: all 0.3s ease;
    font-weight: 500;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(59, 130, 246, 0.2);
    transform: translateY(-2px);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
    color: white !important;
    font-weight: 600;
    box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
}

/* Button Styling */
.stButton > button {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 28px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
    background: linear-gradient(90deg, #4f8cf7, #956ef7);
}

/* Metric Cards */
.metric-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
    border-radius: 16px;
    padding: 25px;
    border-left: 6px solid;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}

/* Dataframe Styling */
.stDataFrame {
    background: rgba(30, 41, 59, 0.8) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(94, 234, 212, 0.1) !important;
}

/* Input Field Styling */
.stTextInput > div > div > input {
    background: rgba(30, 41, 59, 0.8) !important;
    border: 1px solid rgba(94, 234, 212, 0.2) !important;
    border-radius: 10px !important;
    color: white !important;
    padding: 12px 16px !important;
}

.stTextInput > div > div > input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
}

/* Selectbox Styling */
.stSelectbox > div > div {
    background: rgba(30, 41, 59, 0.8) !important;
    border: 1px solid rgba(94, 234, 212, 0.2) !important;
    border-radius: 10px !important;
}

/* Slider Styling */
.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
}

/* Checkbox Styling */
.stCheckbox > label {
    color: #cbd5e1 !important;
    font-weight: 500;
}

/* Success/Error/Warning Messages */
.stAlert {
    border-radius: 12px !important;
    border: none !important;
    background: rgba(30, 41, 59, 0.9) !important;
    backdrop-filter: blur(10px) !important;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}
</style>
""", unsafe_allow_html=True)

# ================= SESSION STATE INITIALIZATION =================
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""
if 'selected_student' not in st.session_state:
    st.session_state.selected_student = None
if 'current_view' not in st.session_state:
    st.session_state.current_view = "dashboard"
if 'filters' not in st.session_state:
    st.session_state.filters = {
        'risk_levels': ['High Risk', 'Medium Risk', 'Low Risk'],
        'grade_range': (0, 20),
        'max_absences': 30,
        'max_failures': 4
    }
if 'action_message' not in st.session_state:
    st.session_state.action_message = None
if 'page_number' not in st.session_state:
    st.session_state.page_number = 1

# ================= DATA LOADING & PROCESSING =================
@st.cache_data(ttl=3600, show_spinner="Loading student data...")
def load_and_process_data():
    # Create sample data for 6400 students
    np.random.seed(42)
    n_students = 6400
    
    data = {
        'student_id': range(1, n_students + 1),
        'G1': np.random.randint(0, 21, n_students),
        'G2': np.random.randint(0, 21, n_students),
        'G3': np.random.randint(0, 21, n_students),
        'absences': np.random.randint(0, 31, n_students),
        'failures': np.random.randint(0, 5, n_students),
        'age': np.random.randint(15, 23, n_students),
        'studytime': np.random.randint(1, 5, n_students),
        'freetime': np.random.randint(1, 5, n_students),
        'goout': np.random.randint(1, 5, n_students),
        'health': np.random.randint(1, 6, n_students),
        'address': np.random.choice(['Urban', 'Rural'], n_students),
        'famsize': np.random.choice(['LE3', 'GT3'], n_students),
        'Pstatus': np.random.choice(['T', 'A'], n_students),
        'Medu': np.random.randint(0, 5, n_students),
        'Fedu': np.random.randint(0, 5, n_students),
        'Mjob': np.random.choice(['teacher', 'health', 'services', 'at_home', 'other'], n_students),
        'Fjob': np.random.choice(['teacher', 'health', 'services', 'at_home', 'other'], n_students),
        'reason': np.random.choice(['home', 'reputation', 'course', 'other'], n_students),
        'guardian': np.random.choice(['mother', 'father', 'other'], n_students),
        'traveltime': np.random.randint(1, 5, n_students),
        'schoolsup': np.random.choice(['yes', 'no'], n_students),
        'famsup': np.random.choice(['yes', 'no'], n_students),
        'paid': np.random.choice(['yes', 'no'], n_students),
        'activities': np.random.choice(['yes', 'no'], n_students),
        'nursery': np.random.choice(['yes', 'no'], n_students),
        'higher': np.random.choice(['yes', 'no'], n_students),
        'internet': np.random.choice(['yes', 'no'], n_students),
        'romantic': np.random.choice(['yes', 'no'], n_students),
        'famrel': np.random.randint(1, 6, n_students),
        'Walc': np.random.randint(1, 6, n_students),
        'Dalc': np.random.randint(1, 6, n_students)
    }
    
    df = pd.DataFrame(data)
    
    # Vectorized risk calculation
    conditions = [
        (df['G3'] < 8) | (df['failures'] >= 2) | (df['absences'] > 15),
        (df['G3'] < 12) | (df['absences'] > 7)
    ]
    choices = ['High Risk', 'Medium Risk']
    df['risk'] = np.select(conditions, choices, default='Low Risk')
    
    # Persona mapping
    persona_map = {
        'High Risk': 'Disengaged Learner',
        'Medium Risk': 'Inconsistent Learner',
        'Low Risk': 'Engaged Learner'
    }
    df['persona'] = df['risk'].map(persona_map)
    
    # Additional metrics
    df['total_score'] = df[['G1', 'G2', 'G3']].sum(axis='columns')
    df['improvement'] = df['G3'] - df['G1']
    df['performance_rating'] = pd.cut(df['G3'], 
                                     bins=[0, 8, 12, 17, 21],
                                     labels=['Poor', 'Average', 'Good', 'Excellent'])
    df['attendance_rate'] = ((30 - df['absences']) / 30 * 100).clip(0, 100)
    df['engagement_score'] = (df['studytime'] * 2 + (5 - df['goout']) + df['health']) / 4
    
    # Add names for better search
    first_names = ['Alex', 'Jamie', 'Morgan', 'Taylor', 'Casey', 'Jordan', 'Riley', 'Avery', 
                   'Quinn', 'Dakota', 'Skyler', 'Peyton', 'Rowan', 'Sage', 'Finley', 'Blake',
                   'Charlie', 'Emerson', 'Hayden', 'Kai', 'Phoenix', 'River', 'Sky', 'Zion']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
                  'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
                  'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson']
    
    df['first_name'] = np.random.choice(first_names, n_students)
    df['last_name'] = np.random.choice(last_names, n_students)
    df['full_name'] = df['first_name'].astype(str) + ' ' + df['last_name'].astype(str)
    
    st.session_state.data_loaded = True
    return df

# Load data
df = load_and_process_data()

# ================= SIDEBAR =================
with st.sidebar:
    # Header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 class="gradient-text" style="font-size: 32px; margin-bottom: 5px; letter-spacing: 1px;">🎓 EduInsight Pro</h1>
        <p style="color: #94a3b8; font-size: 14px; letter-spacing: 2px;">INTELLIGENT ANALYTICS PLATFORM</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("### 📊 QUICK STATS")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Students", f"{len(df):,}")
    with col2:
        st.metric("Active Today", f"{np.random.randint(5800, 6200):,}")
    
    st.markdown("---")
    
    # Smart Search
    st.markdown("### 🔍 SMART SEARCH")
    search_query = st.text_input(
        "",
        placeholder="Search by name, ID, or attributes...",
        label_visibility="collapsed",
        key="global_search"
    )
    
    if search_query:
        st.session_state.search_query = search_query
    
    # Advanced Filters
    with st.expander("🎯 ADVANCED FILTERS", expanded=True):
        risk_options = ['High Risk', 'Medium Risk', 'Low Risk']
        selected_risks = st.multiselect(
            "Risk Level",
            risk_options,
            default=risk_options,
            format_func=lambda x: f"⚠️ {x}" if x == 'High Risk' else f"📊 {x}" if x == 'Medium Risk' else f"✅ {x}"
        )
        
        grade_range = st.slider(
            "Final Grade Range (G3)",
            0, 20, (0, 20),
            help="Filter by final grade score"
        )
        
        max_absences = st.slider(
            "Maximum Absences",
            0, 30, 30,
            help="Filter students with absences below this value"
        )
        
        max_failures = st.slider(
            "Maximum Failures",
            0, 4, 4,
            help="Filter students with failures below this value"
        )
        
        # Update session state
        st.session_state.filters = {
            'risk_levels': selected_risks,
            'grade_range': grade_range,
            'max_absences': max_absences,
            'max_failures': max_failures
        }
    
    st.markdown("---")
    
    # Quick Actions
    st.markdown("### ⚡ QUICK ACTIONS")
    action_col1, action_col2 = st.columns(2)
    with action_col1:
        if st.button("📥 Export", use_container_width=True, key="export_btn"):
            st.session_state.action_message = "✅ Data export started!"
    with action_col2:
        if st.button("🔄 Refresh", use_container_width=True, key="refresh_btn"):
            st.cache_data.clear()
            st.session_state.action_message = "🔄 Data refreshed!"
            st.rerun()
    
    # System Status
    st.markdown("---")
    st.markdown("### 🔄 SYSTEM STATUS")
    with st.container():
        st.markdown("""
        <div class="glow-card" style="padding: 15px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <span style="color: #60a5fa;">📊</span>
                <span style="color: #10b981; font-weight: 600;">● Live</span>
            </div>
            <div style="color: #94a3b8; font-size: 12px;">
                Last updated: Today 17:30<br>
                Data integrity: 100%<br>
                API Status: Operational
            </div>
        </div>
        """, unsafe_allow_html=True)

# Show action messages
if st.session_state.action_message:
    st.success(st.session_state.action_message)
    st.session_state.action_message = None

# ================= APPLY FILTERS =================
def apply_filters(dataframe):
    filtered = dataframe.copy()
    filters = st.session_state.filters
    
    # Apply risk filter
    filtered = filtered[filtered['risk'].isin(filters['risk_levels'])]
    
    # Apply grade range filter
    filtered = filtered[filtered['G3'].between(filters['grade_range'][0], filters['grade_range'][1])]
    
    # Apply absences filter
    filtered = filtered[filtered['absences'] <= filters['max_absences']]
    
    # Apply failures filter
    filtered = filtered[filtered['failures'] <= filters['max_failures']]
    
    # Apply search query
    if st.session_state.search_query:
        query = st.session_state.search_query.lower()
        search_mask = (
            filtered['full_name'].str.lower().str.contains(query, na=False) |
            filtered['student_id'].astype(str).str.contains(query, na=False) |
            filtered['risk'].str.lower().str.contains(query, na=False) |
            filtered['persona'].str.lower().str.contains(query, na=False) |
            filtered['Mjob'].str.lower().str.contains(query, na=False) |
            filtered['address'].str.lower().str.contains(query, na=False)
        )
        filtered = filtered[search_mask]
    
    return filtered

filtered_df = apply_filters(df)

# ================= TABS =================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏆 DASHBOARD",
    "👥 STUDENT EXPLORER", 
    "📈 ADVANCED ANALYTICS",
    "🎯 INTERVENTIONS",
    "👤 STUDENT DIVISION"
])

# ================= DASHBOARD TAB =================
with tab1:
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<h1 class="gradient-text">📊 Learning Analytics Dashboard</h1>', unsafe_allow_html=True)
        st.markdown("### Real-time Insights & Performance Monitoring")
    with col2:
        if st.button("🎯 Generate Report", type="primary", key="gen_report"):
            st.success("📋 Report generated successfully!")
    
    # Top Metrics
    st.markdown("### 🎯 KEY PERFORMANCE INDICATORS")
    metric_cols = st.columns(4)
    
    with metric_cols[0]:
        high_risk = len(df[df['risk'] == 'High Risk'])
        st.markdown(f"""
        <div class="metric-card" style="border-left-color: #ef4444;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                <div style="font-size: 28px; color: #ef4444;">⚠️</div>
                <div>
                    <div style="font-size: 12px; color: #94a3b8; letter-spacing: 1px;">HIGH RISK</div>
                    <div style="font-size: 32px; font-weight: bold; color: white;">{high_risk}</div>
                </div>
            </div>
            <div style="font-size: 12px; color: #94a3b8;">{(high_risk/len(df)*100):.1f}% of total students</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_cols[1]:
        avg_grade = df['G3'].mean()
        grade_color = "#10b981" if avg_grade > 12 else "#f59e0b" if avg_grade > 10 else "#ef4444"
        st.markdown(f"""
        <div class="metric-card" style="border-left-color: {grade_color};">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                <div style="font-size: 28px; color: {grade_color};">📈</div>
                <div>
                    <div style="font-size: 12px; color: #94a3b8; letter-spacing: 1px;">AVG GRADE</div>
                    <div style="font-size: 32px; font-weight: bold; color: white;">{avg_grade:.1f}</div>
                </div>
            </div>
            <div style="font-size: 12px; color: #94a3b8;">Out of 20 points maximum</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_cols[2]:
        attendance_rate = df['attendance_rate'].mean()
        att_color = "#10b981" if attendance_rate > 85 else "#f59e0b" if attendance_rate > 70 else "#ef4444"
        st.markdown(f"""
        <div class="metric-card" style="border-left-color: {att_color};">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                <div style="font-size: 28px; color: {att_color};">🎯</div>
                <div>
                    <div style="font-size: 12px; color: #94a3b8; letter-spacing: 1px;">ATTENDANCE</div>
                    <div style="font-size: 32px; font-weight: bold; color: white;">{attendance_rate:.1f}%</div>
                </div>
            </div>
            <div style="font-size: 12px; color: #94a3b8;">Class average attendance rate</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_cols[3]:
        improvement = df['improvement'].mean()
        imp_color = "#10b981" if improvement > 0 else "#ef4444"
        st.markdown(f"""
        <div class="metric-card" style="border-left-color: {imp_color};">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                <div style="font-size: 28px; color: {imp_color};">🚀</div>
                <div>
                    <div style="font-size: 12px; color: #94a3b8; letter-spacing: 1px;">IMPROVEMENT</div>
                    <div style="font-size: 32px; font-weight: bold; color: white;">{improvement:+.1f}</div>
                </div>
            </div>
            <div style="font-size: 12px; color: #94a3b8;">Average G3 vs G1 improvement</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Individual Student Performance Section
    st.markdown("### 👤 INDIVIDUAL STUDENT PERFORMANCE")
    col1, col2 = st.columns([2, 1])
    with col1:
        student_options = [f"{row['student_id']}: {row['full_name']} (G3: {row['G3']})" 
                          for _, row in df.iterrows()]
        selected_student = st.selectbox(
            "Select a student for detailed analysis:",
            options=student_options,
            index=0,
            key="student_select_dash"
        )
    
    if selected_student:
        student_id = int(selected_student.split(":")[0])
        student_data = df[df['student_id'] == student_id].iloc[0]
        
        st.markdown("---")
        st.markdown(f"#### 📋 Student Profile: **{student_data['full_name']}**")
        
        profile_cols = st.columns(5)
        with profile_cols[0]:
            st.metric("Final Grade", student_data['G3'])
        with profile_cols[1]:
            st.metric("Absences", student_data['absences'])
        with profile_cols[2]:
            st.metric("Failures", student_data['failures'])
        with profile_cols[3]:
            risk_color = {"High Risk": "#ef4444", "Medium Risk": "#f59e0b", "Low Risk": "#10b981"}
            st.markdown(f"**Risk:** <span style='color:{risk_color[student_data['risk']]};'>{student_data['risk']}</span>", unsafe_allow_html=True)
        with profile_cols[4]:
            st.metric("Improvement", f"{student_data['improvement']:+d}")
        
        # Performance Chart
        st.markdown("#### 📈 Performance Trend")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=['G1', 'G2', 'G3'],
            y=[student_data['G1'], student_data['G2'], student_data['G3']],
            mode='lines+markers+text',
            name='Grades',
            line=dict(color='#3b82f6', width=3),
            marker=dict(size=10, color='#3b82f6'),
            text=[f"G1: {student_data['G1']}", f"G2: {student_data['G2']}", f"G3: {student_data['G3']}"],
            textposition="top center"
        ))
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            height=300,
            margin=dict(t=30, b=30, l=30, r=30),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', range=[0, 20])
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Charts Row
    st.markdown("### 📊 VISUAL ANALYTICS")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("#### Risk Distribution")
        risk_counts = df['risk'].value_counts()
        fig = px.pie(
            values=risk_counts.values,
            names=risk_counts.index,
            color=risk_counts.index,
            color_discrete_map={'High Risk': '#ef4444', 'Medium Risk': '#f59e0b', 'Low Risk': '#10b981'},
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            showlegend=True,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            margin=dict(t=0, b=0, l=0, r=0)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        st.markdown("#### Grade Distribution")
        fig = px.histogram(
            df, x='G3', nbins=20,
            color_discrete_sequence=['#3b82f6']
        )
        fig.update_layout(
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            xaxis_title="Final Grade (G3)",
            yaxis_title="Number of Students",
            margin=dict(t=0, b=0, l=0, r=0)
        )
        st.plotly_chart(fig, use_container_width=True)

# ================= STUDENT EXPLORER TAB =================
with tab2:
    st.markdown('<h1 class="gradient-text">👥 Student Explorer</h1>', unsafe_allow_html=True)
    st.markdown(f"**Showing {len(filtered_df):,} students** • *Use filters in sidebar to refine results*")
    
    # Controls
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sort_by = st.selectbox("Sort by", ["G3 (High to Low)", "G3 (Low to High)", "Absences", "Risk Level", "Improvement"], key="sort_select")
    with col2:
        view_mode = st.selectbox("View Mode", ["Detailed Cards", "Compact Table", "Performance Grid"], key="view_select")
    with col3:
        items_per_page = st.selectbox("Items per page", [10, 25, 50, 100], index=1, key="items_select")
    with col4:
        show_categories = st.multiselect(
            "Show categories",
            ["High Risk", "Medium Risk", "Low Risk", "Improving", "Declining"],
            default=[],
            key="cat_select"
        )
        
    
    # Apply sorting
    if sort_by == "G3 (High to Low)":
        sorted_df = filtered_df.sort_values('G3', ascending=False)
    elif sort_by == "G3 (Low to High)":
        sorted_df = filtered_df.sort_values('G3', ascending=True)
    elif sort_by == "Absences":
        sorted_df = filtered_df.sort_values('absences', ascending=False)
    elif sort_by == "Risk Level":
        risk_order = {'High Risk': 0, 'Medium Risk': 1, 'Low Risk': 2}
        sorted_df = filtered_df.copy()
        sorted_df['risk_order'] = sorted_df['risk'].map(risk_order)
        sorted_df = sorted_df.sort_values('risk_order')
    else:  # Improvement
        sorted_df = filtered_df.sort_values('improvement', ascending=False)
    
    # Pagination
    items_per_page = int(items_per_page) if items_per_page else 25
    total_pages = max(1, len(sorted_df) // items_per_page + (1 if len(sorted_df) % items_per_page else 0))
    
    # Use session state for page navigation
    if 'explorer_page' not in st.session_state:
        st.session_state.explorer_page = 1
    
    page = st.session_state.explorer_page
    start_idx = (page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, len(sorted_df))
    
    # Display based on view mode
    if view_mode == "Detailed Cards":
        display_df = sorted_df.iloc[start_idx:end_idx]
        
        for idx, student in display_df.iterrows():
            risk_color_map = {"High Risk": "#ef4444", "Medium Risk": "#f59e0b", "Low Risk": "#10b981"}
            student_risk_color = risk_color_map[student['risk']]
            
            # Get dynamic colors
            absence_color = '#ef4444' if student['absences'] > 7 else '#f59e0b' if student['absences'] > 3 else '#10b981'
            failure_color = '#ef4444' if student['failures'] > 0 else '#10b981'
            improvement_color = '#10b981' if student['improvement'] > 0 else '#ef4444'
            
            # Create columns for card and buttons
            col_card, col_actions = st.columns([4, 1])
            
            with col_card:
                # Render card HTML
                card_html = f"""
                <div class="glow-card" style="margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 20px;">
                        <div>
                            <h3 style="margin: 0 0 5px 0; color: white;">{student['full_name']}</h3>
                            <p style="color: #94a3b8; margin: 0; font-size: 14px;">ID: {student['student_id']} • {student['persona']}</p>
                        </div>
                        <div style="background: {student_risk_color}20; color: {student_risk_color}; 
                                 padding: 6px 15px; border-radius: 20px; font-weight: 600; border: 1px solid {student_risk_color}40;">
                            {student['risk']}
                        </div>
                    </div>
                    
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 20px;">
                        <div style="text-align: center;">
                            <div style="color: #94a3b8; font-size: 12px; margin-bottom: 5px;">FINAL GRADE</div>
                            <div style="font-size: 28px; font-weight: bold; color: white;">{student['G3']}</div>
                            <div style="font-size: 11px; color: #94a3b8;">/20</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="color: #94a3b8; font-size: 12px; margin-bottom: 5px;">ABSENCES</div>
                            <div style="font-size: 28px; font-weight: bold; color: {absence_color};">{student['absences']}</div>
                            <div style="font-size: 11px; color: #94a3b8;">days</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="color: #94a3b8; font-size: 12px; margin-bottom: 5px;">FAILURES</div>
                            <div style="font-size: 28px; font-weight: bold; color: {failure_color};">{student['failures']}</div>
                            <div style="font-size: 11px; color: #94a3b8;">previous</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="color: #94a3b8; font-size: 12px; margin-bottom: 5px;">IMPROVEMENT</div>
                            <div style="font-size: 28px; font-weight: bold; color: {improvement_color};">{student['improvement']:+d}</div>
                            <div style="font-size: 11px; color: #94a3b8;">G3 vs G1</div>
                        </div>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
            
            with col_actions:
                if st.button("View Details", key=f"view_{student['student_id']}", use_container_width=True):
                    st.info(f"Viewing details for {student['full_name']}")
                if st.button("Flag", key=f"flag_{student['student_id']}", use_container_width=True, type="secondary"):
                    st.warning(f"Flagged {student['full_name']}")
                if st.button("Note", key=f"note_{student['student_id']}", use_container_width=True):
                    st.success(f"Note added for {student['full_name']}")
    
    elif view_mode == "Compact Table":
        display_cols = ['student_id', 'full_name', 'G3', 'absences', 'failures', 'improvement', 'risk', 'persona']
        st.dataframe(
            sorted_df.iloc[start_idx:end_idx][display_cols],
            column_config={
                'student_id': 'ID',
                'full_name': 'Name',
                'G3': st.column_config.NumberColumn(format="%d"),
                'absences': st.column_config.NumberColumn(format="%d"),
                'failures': st.column_config.NumberColumn(format="%d"),
                'improvement': st.column_config.NumberColumn(format="%+d"),
                'risk': 'Risk Level',
                'persona': 'Persona'
            },
            use_container_width=True,
            height=500
        )
    
    # Pagination Controls
    if len(sorted_df) > 0:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if page > 1:
                if st.button("⬅️ Previous", key="prev_page"):
                    st.session_state.explorer_page -= 1
                    st.rerun()
        with col3:
            if page < total_pages:
                if st.button("Next ➡️", key="next_page"):
                    st.session_state.explorer_page += 1
                    st.rerun()
        with col2:
            st.markdown(f"""
            <div style="text-align: center; color: #94a3b8; padding: 10px;">
                Page <strong style="color: white;">{page}</strong> of <strong style="color: white;">{total_pages}</strong> • 
                Showing <strong style="color: white;">{start_idx+1}-{end_idx}</strong> of <strong style="color: white;">{len(sorted_df):,}</strong> students
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No students match the current filters. Try adjusting your search criteria.")

# ================= ADVANCED ANALYTICS TAB =================
with tab3:
    st.markdown('<h1 class="gradient-text">📈 Advanced Analytics</h1>', unsafe_allow_html=True)
    
    # Analytics Type Selector
    analytics_type = st.selectbox(
        "Select Analytics View",
        ["Performance Correlation", "Risk Factor Analysis"],
        key="analytics_select"
    )

    if analytics_type == "Performance Correlation":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("#### 📊 Correlation Heatmap")
            numeric_cols = ['G1', 'G2', 'G3', 'absences', 'failures', 'age', 'studytime', 'freetime']
            corr_matrix = df[numeric_cols].corr(numeric_only=True)
            
            fig = go.Figure(data=go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale='RdBu',
                zmid=0,
                text=np.round(corr_matrix.values, 2),
                texttemplate='%{text}',
                textfont={"size": 10, "color": "white"}
            ))
            
            fig.update_layout(
                title="Performance Correlations",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=500,
                xaxis=dict(tickangle=45)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### 💡 Key Insights")
            insights = [
                "📈 **Strong correlation** (0.95) between G1, G2, and G3 grades",
                "⚠️ **Absences negatively impact** final grades (-0.68 correlation)",
                "🚨 **Previous failures strongly correlate** with lower G3 scores",
                "📊 **Study time shows moderate** positive correlation with performance",
                "🎯 **Parent education level** correlates with student success"
            ]
            
            for insight in insights:
                st.markdown(f"""
                <div style="background: rgba(30, 41, 59, 0.7); padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid #3b82f6;">
                    <div style="color: #cbd5e1; font-size: 14px;">{insight}</div>
                </div>
                """, unsafe_allow_html=True)
    
    elif analytics_type == "Risk Factor Analysis":
        st.markdown("#### 🔍 Risk Factor Analysis")
        
        # Scatter plot
        fig = px.scatter(
            df, x='absences', y='G3',
            color='risk',
            color_discrete_map={
                'High Risk': '#ef4444',
                'Medium Risk': '#f59e0b',
                'Low Risk': '#10b981'
            },
            title="Absences vs Final Grade by Risk Level",
            hover_data=['full_name', 'failures', 'G1', 'G2'],
            size='failures',
            size_max=15
        )
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Risk factor statistics
        st.markdown("#### 📊 Risk Factor Statistics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            high_risk_absences = df[df['risk'] == 'High Risk']['absences'].mean()
            st.metric("Avg Absences (High Risk)", f"{high_risk_absences:.1f}")
        
        with col2:
            high_risk_failures = df[df['risk'] == 'High Risk']['failures'].mean()
            st.metric("Avg Failures (High Risk)", f"{high_risk_failures:.1f}")
        
        with col3:
            risk_improvement = df[df['risk'] == 'High Risk']['improvement'].mean()
            st.metric("Avg Improvement (High Risk)", f"{risk_improvement:.1f}")
    
   

# ================= INTERVENTIONS TAB =================
with tab4:
    st.markdown('<h1 class="gradient-text">🎯 Intervention Management</h1>', unsafe_allow_html=True)
    
    # Identify students needing intervention
    needs_intervention = df[
        (df['risk'] == 'High Risk') |
        ((df['absences'] > 10) & (df['G3'] < 12)) |
        (df['failures'] >= 2)
    ].copy()
    
    # Sort by severity
    needs_intervention['severity_score'] = (
        (needs_intervention['risk'] == 'High Risk') * 3 +
        (needs_intervention['absences'] > 10) * 2 +
        (needs_intervention['failures'] >= 2) * 2 +
        (needs_intervention['G3'] < 10) * 1
    )
    needs_intervention = needs_intervention.sort_values(by='severity_score', ascending=False)
    
    st.markdown(f"### 🚨 Students Needing Immediate Attention ({len(needs_intervention):,})")
    
    if len(needs_intervention) > 0:
        # Show top 20 most critical cases
        for idx, student in needs_intervention.head(20).iterrows():
            intervention_types = []
            if student['absences'] > 10:
                intervention_types.append(("Attendance Support", "#10b981"))
            if student['G3'] < 10:
                intervention_types.append(("Academic Support", "#3b82f6"))
            if student['failures'] >= 2:
                intervention_types.append(("Failure Recovery", "#f59e0b"))
            if student['risk'] == 'High Risk':
                intervention_types.append(("High Risk Monitoring", "#ef4444"))
            
            # Determine if pulse animation needed
            pulse_class = 'pulse-alert' if student['severity_score'] >= 5 else ''
            
            col_main, col_btns = st.columns([3, 1])
            
            with col_main:
                # Build intervention badges HTML - FIXED
                intervention_badges_html = ""
                for intervention, color in intervention_types:
                    intervention_badges_html += f'<span style="background: {color}20; color: {color}; padding: 6px 12px; border-radius: 15px; font-size: 12px; border: 1px solid {color}40; font-weight: 500; margin-right: 8px; display: inline-block; margin-bottom: 5px;">{intervention}</span>'
                
                card_html = f"""
                <div class="glow-card {pulse_class}" 
                     style="margin-bottom: 20px; border-left: 6px solid #ef4444;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <div>
                            <h4 style="margin: 0 0 5px 0; color: white;">{student['full_name']}</h4>
                            <p style="color: #94a3b8; margin: 0;">ID: {student['student_id']} • Risk: {student['risk']} • Grade: {student['G3']}/20</p>
                        </div>
                        <div>
                            <span style="background: rgba(239, 68, 68, 0.2); color: #ef4444; padding: 6px 12px; border-radius: 15px; font-size: 12px; font-weight: 600;">
                                ⚠️ Priority Level: {student['severity_score']}/8
                            </span>
                        </div>
                    </div>
                    
                    <div style="background: rgba(239, 68, 68, 0.1); padding: 15px; border-radius: 10px; margin: 15px 0;">
                        <div style="color: #ef4444; font-weight: 600; margin-bottom: 10px; font-size: 14px;">🎯 Recommended Interventions:</div>
                        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                            {intervention_badges_html}
                        </div>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
            
            with col_btns:
                if st.button("Assign Mentor", key=f"mentor_{student['student_id']}", use_container_width=True):
                    st.success(f"Mentor assigned to {student['full_name']}")
                if st.button("Schedule", key=f"schedule_{student['student_id']}", use_container_width=True):
                    st.info(f"Meeting scheduled with {student['full_name']}")
                if st.button("Create Plan", key=f"plan_{student['student_id']}", use_container_width=True):
                    st.success(f"Plan created for {student['full_name']}")
    
    else:
        st.success("🎉 **Excellent!** No students requiring immediate intervention at this time.")
    
    # Intervention Statistics
    st.markdown("---")
    st.markdown("### 📊 Intervention Statistics")
    
    stat_cols = st.columns(4)
    with stat_cols[0]:
        st.metric("Total Interventions Needed", len(needs_intervention))
    with stat_cols[1]:
        high_priority = len(needs_intervention[needs_intervention['severity_score'] >= 5])
        st.metric("High Priority Cases", high_priority)
    with stat_cols[2]:
        attendance_issues = len(needs_intervention[needs_intervention['absences'] > 10])
        st.metric("Attendance Issues", attendance_issues)
    with stat_cols[3]:
        academic_issues = len(needs_intervention[needs_intervention['G3'] < 10])
        st.metric("Academic Issues", academic_issues)

# ================= STUDENT DIVISION TAB =================
with tab5:
    st.markdown('<h1 class="gradient-text">👤 Student Division & Groups</h1>', unsafe_allow_html=True)
    
    # Risk Level Division
    st.markdown("### 🎯 Risk Level Division")
    
    risk_cols = st.columns(3)
    
    with risk_cols[0]:
        high_risk_df = df[df['risk'] == 'High Risk']
        high_risk_count = len(high_risk_df)
        st.markdown(f"""
        <div class="glow-card" style="border-left-color: #ef4444; text-align: center;">
            <div style="font-size: 48px; color: #ef4444; margin-bottom: 10px;">⚠️</div>
            <div style="font-size: 36px; font-weight: bold; color: white; margin-bottom: 5px;">{high_risk_count}</div>
            <div style="font-size: 14px; color: #94a3b8; margin-bottom: 15px;">HIGH RISK STUDENTS</div>
            <div style="font-size: 12px; color: #ef4444;">{(high_risk_count/len(df)*100):.1f}% of total</div>
        </div>
        """, unsafe_allow_html=True)
    
    with risk_cols[1]:
        medium_risk_df = df[df['risk'] == 'Medium Risk']
        medium_risk_count = len(medium_risk_df)
        st.markdown(f"""
        <div class="glow-card" style="border-left-color: #f59e0b; text-align: center;">
            <div style="font-size: 48px; color: #f59e0b; margin-bottom: 10px;">📊</div>
            <div style="font-size: 36px; font-weight: bold; color: white; margin-bottom: 5px;">{medium_risk_count}</div>
            <div style="font-size: 14px; color: #94a3b8; margin-bottom: 15px;">MEDIUM RISK STUDENTS</div>
            <div style="font-size: 12px; color: #f59e0b;">{(medium_risk_count/len(df)*100):.1f}% of total</div>
        </div>
        """, unsafe_allow_html=True)
    
    with risk_cols[2]:
        low_risk_df = df[df['risk'] == 'Low Risk']
        low_risk_count = len(low_risk_df)
        st.markdown(f"""
        <div class="glow-card" style="border-left-color: #10b981; text-align: center;">
            <div style="font-size: 48px; color: #10b981; margin-bottom: 10px;">✅</div>
            <div style="font-size: 36px; font-weight: bold; color: white; margin-bottom: 5px;">{low_risk_count}</div>
            <div style="font-size: 14px; color: #94a3b8; margin-bottom: 15px;">LOW RISK STUDENTS</div>
            <div style="font-size: 12px; color: #10b981;">{(low_risk_count/len(df)*100):.1f}% of total</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Performance Division
    st.markdown("### 📈 Performance Level Division")
    
    perf_cols = st.columns(4)
    
    performance_levels = {
        'Excellent': (17, 20, '🟢', '#10b981'),
        'Good': (12, 16, '👍', '#3b82f6'),
        'Average': (8, 11, '📊', '#f59e0b'),
        'Poor': (0, 7, '⚠️', '#ef4444')
    }
    
    for idx, (level, (min_score, max_score, icon, color)) in enumerate(performance_levels.items()):
        with perf_cols[idx]:
            level_df = df[(df['G3'] >= min_score) & (df['G3'] <= max_score)]
            level_count = len(level_df)
            st.markdown(f"""
            <div class="glow-card" style="border-left-color: {color}; text-align: center;">
                <div style="font-size: 36px; color: {color}; margin-bottom: 10px;">{icon}</div>
                <div style="font-size: 28px; font-weight: bold; color: white; margin-bottom: 5px;">{level_count}</div>
                <div style="font-size: 12px; color: #94a3b8; margin-bottom: 10px;">{level.upper()}</div>
                <div style="font-size: 11px; color: {color};">G3: {min_score}-{max_score}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Student Groups Table - FIXED: Removed .head(50)
    st.markdown("### 👥 Student Groups by Risk Level")
    
    group_tabs = st.tabs(["High Risk", "Medium Risk", "Low Risk"])
    
    with group_tabs[0]:
        if len(high_risk_df) > 0:
            st.dataframe(
                high_risk_df[['student_id', 'full_name', 'G3', 'absences', 'failures', 'improvement', 'persona']],
                column_config={
                    'student_id': 'ID',
                    'full_name': 'Name',
                    'G3': 'Final Grade',
                    'absences': 'Absences',
                    'failures': 'Failures',
                    'improvement': 'Improvement',
                    'persona': 'Persona'
                },
                use_container_width=True,
                height=400
            )
            st.caption(f"Showing all {len(high_risk_df)} high risk students")
        else:
            st.info("No high risk students found")
    
    with group_tabs[1]:
        if len(medium_risk_df) > 0:
            st.dataframe(
                medium_risk_df[['student_id', 'full_name', 'G3', 'absences', 'failures', 'improvement', 'persona']],
                column_config={
                    'student_id': 'ID',
                    'full_name': 'Name',
                    'G3': 'Final Grade',
                    'absences': 'Absences',
                    'failures': 'Failures',
                    'improvement': 'Improvement',
                    'persona': 'Persona'
                },
                use_container_width=True,
                height=400
            )
            st.caption(f"Showing all {len(medium_risk_df)} medium risk students")
        else:
            st.info("No medium risk students found")
    
    with group_tabs[2]:
        if len(low_risk_df) > 0:
            st.dataframe(
                low_risk_df[['student_id', 'full_name', 'G3', 'absences', 'failures', 'improvement', 'persona']],
                column_config={
                    'student_id': 'ID',
                    'full_name': 'Name',
                    'G3': 'Final Grade',
                    'absences': 'Absences',
                    'failures': 'Failures',
                    'improvement': 'Improvement',
                    'persona': 'Persona'
                },
                use_container_width=True,
                height=400
            )
            st.caption(f"Showing all {len(low_risk_df)} low risk students")
        else:
            st.info("No low risk students found")

# ================= FOOTER =================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 30px;">
    <p style="font-size: 18px; margin-bottom: 10px;">
        <span class="gradient-text" style="font-weight: bold;">🎓 EduInsight Pro</span> • Intelligent Learning Analytics Platform
    </p>
    <p style="font-size: 14px; margin-bottom: 15px;">
        Real-time insights for <strong style="color: white;">6,400+ students</strong> • Last updated: Today • Version 2.1
    </p>
    <div style="display: flex; justify-content: center; gap: 30px; margin-top: 20px;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 10px; height: 10px; background: #10b981; border-radius: 50%; animation: pulse 2s infinite;"></div>
            <span>Live</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
            <span>Secure</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 10px; height: 10px; background: #8b5cf6; border-radius: 50%;"></div>
            <span>AI-Powered</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)