import streamlit as st
import os

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="INA-PREDICT | Early Warning System",
    page_icon="🌋",
    layout="wide"
)

# ==================== READ HTML FILE ====================
def load_html(filename):
    """Membaca file HTML dan mengembalikan sebagai string"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"<h1>File {filename} tidak ditemukan</h1>"

# ==================== SIDEBAR NAVIGASI ====================
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem;">
    <div style="font-size: 3rem;">🛡️</div>
    <h2 style="color: #2b6e4e;">INA-PREDICT</h2>
    <p style="font-size: 0.7rem;">Early Warning System</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "📋 MENU NAVIGASI",
    ["🏠 Dashboard", "🤖 Chatbot AI", "📊 Prediksi Bencana", "📖 Panduan Aksi", "📞 Kontak Darurat", "💝 Donasi", "📧 Hubungi Kami"]
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
<div style="text-align: center; font-size: 0.6rem;">
    <i class="fas fa-clock"></i> Update: {__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M')}<br>
    Data BNPB - BMKG - BPBD
</div>
""", unsafe_allow_html=True)

# ==================== MENAMPILKAN HTML ASLI ====================

html_files = {
    "🏠 Dashboard": "index.html",
    "🤖 Chatbot AI": "chatbot.html",
    "📊 Prediksi Bencana": "prediksi.html",
    "📖 Panduan Aksi": "panduan.html",
    "📞 Kontak Darurat": "kontak.html",
    "💝 Donasi": "donasi.html",
    "📧 Hubungi Kami": "hubungikami.html"
}

if menu in html_files:
    html_file = html_files[menu]
    html_content = load_html(html_file)
    
    # Tampilkan HTML dengan komponen Streamlit
    st.components.v1.html(
        html_content,
        height=800,
        scrolling=True
    )
else:
    # Default ke index.html
    html_content = load_html("index.html")
    st.components.v1.html(
        html_content,
        height=800,
        scrolling=True
    )