"""Digital Communication Simulator — Streamlit Cloud entry point.
Deploy this file from a GitHub repository with requirements.txt.
"""

import random
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Digital Communication Simulator",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM COLOR PALETTE CSS (Dark Background, Light Text)
# Palette: Alice Blue (#DAE8FB), Thistle (#F2D2FF), Pearl Aqua (#75CBD1), 
#          Dusk Blue (#3E5BA3), Deep Navy (#0C0D45)[cite: 3]
# ============================================================
st.markdown("""
<style>
    /* Global App Background & Text */
    .stApp {
        background-color: #0C0D45;
        color: #DAE8FB;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header Section */
    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: 800;
        color: #F2D2FF;
        margin-bottom: 2px;
        letter-spacing: -0.5px;
    }
    .subtitle {
        text-align: center;
        font-size: 16px;
        margin-bottom: 25px;
        color: #75CBD1;
        font-weight: 500;
    }
    
    /* Section Headers */
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #F2D2FF;
        margin-top: 28px;
        margin-bottom: 14px;
        letter-spacing: -0.3px;
        border-bottom: 2px solid #3E5BA3;
        padding-bottom: 6px;
    }
    
    /* Algorithm & Data Cards (Dusk Blue Background with Light Text) */
    .algorithm-card {
        background: #3E5BA3;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #75CBD1;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        min-height: 180px;
        color: #DAE8FB;
    }
    .algorithm-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
        border-color: #F2D2FF;
    }
    .algorithm-card h3 {
        margin-top: 0;
        font-size: 20px;
        color: #F2D2FF;
        font-weight: 700;
    }
    .algorithm-card p {
        font-size: 14px;
        color: #DAE8FB;
        line-height: 1.6;
    }
    
    .data-card {
        background: #3E5BA3;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #75CBD1;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        text-align: center;
        min-height: 110px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        color: #DAE8FB;
    }
    .data-title {
        font-size: 13px;
        font-weight: 700;
        color: #75CBD1;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }
    .data-value {
        font-size: 16px;
        font-weight: 700;
        color: #F2D2FF;
        overflow-wrap: anywhere;
        font-family: monospace;
    }
    
    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #3E5BA3;
        color: #DAE8FB;
    }
    section[data-testid="stSidebar"] .stMarkdown h1, 
    section[data-testid="stSidebar"] .stMarkdown h2, 
    section[data-testid="stSidebar"] .stMarkdown h3,
    section[data-testid="stSidebar"] label {
        color: #DAE8FB !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 30px;
        font-size: 13px;
        color: #75CBD1;
        border-top: 1px solid #3E5BA3;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================
st.markdown(
    '<div class="main-title">📡 Digital Communication Simulator Pro</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Advanced LFSR Scrambling • XOR Processing • Multi-Format Line Coding • Telemetry Noise Analysis</div>',
    unsafe_allow_html=True
)


# ============================================================
# ALGORITHM OVERVIEW CARDS
# ============================================================
st.markdown('<div class="section-title">🔬 Line Coding Algorithms Architecture</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="algorithm-card">
      <h3>📊 NRZ-L</h3>
      <p><b>Non-Return-to-Zero-Level</b></p>
      <p>• Binary 1 -> +1V Level<br>• Binary 0 -> -1V Level</p>
      <p>Direct voltage representation of logical bit levels.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="algorithm-card">
      <h3>🔄 NRZ-I</h3>
      <p><b>Non-Return-to-Zero Inverted</b></p>
      <p>• Binary 1 -> Level Transition<br>• Binary 0 -> No Transition</p>
      <p>Differential encoding resistant to phase inversion.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="algorithm-card">
      <h3>⚡ Manchester</h3>
      <p><b>Manchester Encoding</b></p>
      <p>• Binary 1 -> High-to-Low (-1 to +1)<br>• Binary 0 -> Low-to-High (+1 to -1)</p>
      <p>Self-clocking waveform with mid-bit transitions.</p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SIDEBAR CONTROLS
# ============================================================
st.sidebar.title("⚙️ Simulator Controls")
st.sidebar.markdown("---")

st.sidebar.markdown("### 1. Data Configuration")
data_mode = st.sidebar.radio(
    "Data Source",
    ["Random Data Stream", "Custom Binary Input"]
)

binary_input = "101100101001"
number_of_bits = 20

if data_mode == "Random Data Stream":
    number_of_bits = st.sidebar.slider(
        "Stream Length (Bits)", min_value=5, max_value=50, value=20,
        help="Number of pseudo-random bits to generate."
    )
else:
    binary_input = st.sidebar.text_input(
        "Enter Binary Data", value="101100101001",
        help="Type or paste a binary sequence (0s and 1s)."
    )

st.sidebar.markdown("---")
st.sidebar.markdown("### 2. Transmission Impairments")
noise_type = st.sidebar.selectbox(
    "Channel Noise Model",
    ["Gaussian", "Impulse", "None"],
    help="Gaussian introduces smooth thermal fluctuations. Impulse adds sharp transmission bursts."
)

noise_strength = st.sidebar.slider(
    "Noise Amplitude Intensity (%)",
    min_value=0, max_value=100, value=30, step=5,
    help="Controls the amplitude scaling of the channel distortion."
)

st.sidebar.markdown("---")
generate_button = st.sidebar.button(
    "🚀 Run Simulation Pipeline", use_container_width=True, type="primary"
)


# ============================================================
# LFSR AND SCRAMBLING CORE FUNCTIONS
# ============================================================
def lfsr_sequence(length):
    """Generate a deterministic bit sequence from a 4-bit LFSR."""
    register = [1, 0, 1, 1]
    sequence = []
    for _ in range(length):
        output = register[-1]
        feedback = register[0] ^ register[3]
        register = [feedback] + register[:3]
        sequence.append(output)
    return sequence

def xor_bits(first, second):
    return [a ^ b for a, b in zip(first, second)]


# ============================================================
# LINE CODERS
# ============================================================
def nrz_l_encode(data):
    return [1 if bit == 1 else -1 for bit in data]

def nrz_i_encode(data, initial_level=-1):
    signal = []
    current_level = initial_level
    for bit in data:
        if bit == 1:
            current_level = -current_level
        signal.append(current_level)
    return signal

def manchester_encode(data):
    signal = []
    for bit in data:
        if bit == 1:
            signal.extend([-1, 1])
        else:
            signal.extend([1, -1])
    return signal


# ============================================================
# OVERSAMPLING AND NOISE MODELS
# ============================================================
SAMPLES_PER_BIT = 20  # Even number required for Manchester encoding

def oversample_signal(symbols, samples_per_symbol=SAMPLES_PER_BIT):
    return np.repeat(np.asarray(symbols, dtype=float), samples_per_symbol)

def add_channel_noise(clean_samples, noise_type, strength_percent):
    clean_samples = np.asarray(clean_samples, dtype=float)
    if noise_type == "None" or strength_percent == 0:
        return clean_samples.copy(), np.zeros_like(clean_samples)

    rng = np.random.default_rng()
    sigma = (strength_percent / 100.0) * 1.2

    if noise_type == "Gaussian":
        noise = rng.normal(loc=0.0, scale=sigma, size=len(clean_samples))
    elif noise_type == "Impulse":
        noise = rng.normal(loc=0.0, scale=sigma * 0.2, size=len(clean_samples))
        spike_mask = rng.random(len(clean_samples)) < (strength_percent / 100.0 * 0.15)
        spikes = rng.choice([-1.0, 1.0], size=len(clean_samples))
        noise += spike_mask * spikes * sigma * 3.0
    else:
        noise = np.zeros_like(clean_samples)

    return clean_samples + noise, noise


# ============================================================
# RECEIVER / DECODERS
# ============================================================
def sample_nrz_levels(received_samples, bit_count):
    samples = received_samples.reshape(bit_count, SAMPLES_PER_BIT)
    midpoint = SAMPLES_PER_BIT // 2
    return samples[:, midpoint]

def decode_nrz_l(received_samples, bit_count):
    levels = sample_nrz_levels(received_samples, bit_count)
    return [1 if level >= 0 else 0 for level in levels]

def decode_nrz_i(received_samples, bit_count, initial_level=-1):
    levels = sample_nrz_levels(received_samples, bit_count)
    estimated_levels = [1 if level >= 0 else -1 for level in levels]
    bits = []
    previous_level = initial_level
    for level in estimated_levels:
        bits.append(1 if level != previous_level else 0)
        previous_level = level
    return bits

def decode_manchester(received_samples, bit_count):
    samples = received_samples.reshape(bit_count, SAMPLES_PER_BIT)
    half = SAMPLES_PER_BIT // 2
    first_half = np.mean(samples[:, :half], axis=1)
    second_half = np.mean(samples[:, half:], axis=1)
    return [1 if second > first else 0 for first, second in zip(first_half, second_half)]


# ============================================================
# TELEMETRY & PLOTTING ENGINES (Using Dark Background Palette)
# ============================================================
def create_digital_plot(symbols, title, bit_count, manchester=False):
    fig, ax = plt.subplots(figsize=(12, 3.2))
    fig.patch.set_facecolor('#0C0D45')
    ax.set_facecolor('#0C0D45')
    
    if manchester:
        x = np.arange(len(symbols)) * 0.5
        x = np.append(x, len(symbols) * 0.5)
        y = np.append(np.asarray(symbols, dtype=float), symbols[-1])
    else:
        x = np.arange(len(symbols))
        x = np.append(x, len(symbols))
        y = np.append(np.asarray(symbols, dtype=float), symbols[-1])
        
    ax.step(x, y, where="post", color="#75CBD1", linewidth=2.2, label="Logical Signal")
    ax.axhline(0, color="#3E5BA3", linewidth=1.0, linestyle="--")
    ax.set_title(title, fontweight="bold", color="#F2D2FF", fontsize=12)
    ax.set_xlabel("Time (Bit Periods)", color="#DAE8FB", fontsize=10)
    ax.set_ylabel("Amplitude (V)", color="#DAE8FB", fontsize=10)
    ax.set_xlim(0, bit_count)
    ax.set_ylim(-1.6, 1.6)
    ax.set_xticks(range(bit_count + 1))
    ax.tick_params(colors="#DAE8FB", labelsize=9)
    ax.grid(True, color="#3E5BA3", linewidth=0.7, alpha=0.8)
    
    for spine in ax.spines.values():
        spine.set_color("#3E5BA3")
    fig.tight_layout()
    return fig

def create_noisy_plot(clean_samples, noisy_samples, title, bit_count):
    fig, ax = plt.subplots(figsize=(12, 3.4))
    time = np.arange(len(noisy_samples)) / SAMPLES_PER_BIT

    ax.set_facecolor("#0C0D45")
    fig.patch.set_facecolor("#0C0D45")
    
    ax.plot(time, noisy_samples, color="#F2D2FF", linewidth=1.1, label="Impaired Waveform")
    ax.axhline(0, color="#3E5BA3", linewidth=0.8, linestyle=":")
    ax.set_title(title, color="#F2D2FF", fontweight="bold", fontsize=12)
    ax.set_xlabel("Time (Bit Periods)", color="#DAE8FB", fontsize=10)
    ax.set_ylabel("Amplitude (V)", color="#DAE8FB", fontsize=10)
    ax.set_xlim(0, bit_count)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xticks(range(bit_count + 1))
    ax.tick_params(colors="#DAE8FB", labelsize=9)
    ax.grid(True, color="#3E5BA3", linewidth=0.7, alpha=0.8)
    
    for spine in ax.spines.values():
        spine.set_color("#3E5BA3")
    fig.tight_layout()
    return fig

def create_noise_plot(noise_samples, title, bit_count):
    fig, ax = plt.subplots(figsize=(12, 2.4))
    time = np.arange(len(noise_samples)) / SAMPLES_PER_BIT
    ax.set_facecolor("#0C0D45")
    fig.patch.set_facecolor("#0C0D45")
    
    ax.plot(time, noise_samples, color="#75CBD1", linewidth=0.85, label="Noise Floor")
    ax.axhline(0, color="#3E5BA3", linewidth=0.8, linestyle=":")
    ax.set_title(title, color="#F2D2FF", fontweight="bold", fontsize=11)
    ax.set_xlabel("Time (Bit Periods)", color="#DAE8FB", fontsize=9)
    ax.set_ylabel("Noise (V)", color="#DAE8FB", fontsize=9)
    ax.set_xlim(0, bit_count)
    ax.tick_params(colors="#DAE8FB", labelsize=8)
    ax.grid(True, color="#3E5BA3", linewidth=0.7, alpha=0.8)
    
    for spine in ax.spines.values():
        spine.set_color("#3E5BA3")
    fig.tight_layout()
    return fig

def accuracy_percent(original, recovered):
    correct = sum(a == b for a, b in zip(original, recovered))
    total = len(original)
    return (100.0 * correct / total) if total else 0.0, correct, total - correct

def show_bit_card(title, bits):
    st.markdown(
        f'<div class="data-card"><div class="data-title">{title}</div><div class="data-value">{" ".join(map(str, bits))}</div></div>',
        unsafe_allow_html=True
    )


# ============================================================
# MAIN SIMULATION CONTROLLER
# ============================================================
if generate_button:
    if data_mode == "Random Data Stream":
        data = [random.randint(0, 1) for _ in range(number_of_bits)]
    else:
        cleaned_input = "".join(binary_input.split())
        if not cleaned_input:
            st.error("Please enter a valid binary data sequence.")
            st.stop()
        if any(bit not in "01" for bit in cleaned_input):
            st.error("Invalid input detected. Please enter only binary digits (0 and 1).")
            st.stop()
        data = [int(bit) for bit in cleaned_input]

    scrambling_sequence = lfsr_sequence(len(data))
    scrambled_data = xor_bits(data, scrambling_sequence)

    st.markdown('<div class="section-title">📊 Binary Data Pipeline & LFSR Scrambling</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        show_bit_card("Original Data Stream", data)
    with c2:
        show_bit_card("LFSR Generator Sequence", scrambling_sequence)
    with c3:
        show_bit_card("Scrambled Payload", scrambled_data)

    st.markdown('<div class="section-title">📡 Clean Transmitted Signals (Baseband)</div>', unsafe_allow_html=True)

    algorithms = [
        {"name": "NRZ-L", "symbols": nrz_l_encode(scrambled_data), "manchester": False, "decoder": decode_nrz_l},
        {"name": "NRZ-I", "symbols": nrz_i_encode(scrambled_data), "manchester": False, "decoder": decode_nrz_i},
        {"name": "Manchester", "symbols": manchester_encode(scrambled_data), "manchester": True, "decoder": decode_manchester}
    ]

    for item in algorithms:
        st.subheader(item["name"])
        st.pyplot(
            create_digital_plot(
                item["symbols"],
                item["name"] + " Baseband Encoded Waveform",
                len(data),
                manchester=item["manchester"]
            ),
            use_container_width=True
        )

    st.markdown('<div class="section-title">🌩️ Noisy Channel Telemetry Analysis</div>', unsafe_allow_html=True)
    st.info(f"Active Impairment Profile: **{noise_type} Noise** with **{noise_strength}%** intensity.")

    results = []
    tabs = st.tabs([item["name"] for item in algorithms])

    for tab, item in zip(tabs, algorithms):
        with tab:
            if item["manchester"]:
                samples_per_half_bit = SAMPLES_PER_BIT // 2
                clean_samples = np.repeat(np.asarray(item["symbols"], dtype=float), samples_per_half_bit)
            else:
                clean_samples = oversample_signal(item["symbols"])

            noisy_samples, noise_samples = add_channel_noise(clean_samples, noise_type, noise_strength)

            st.pyplot(
                create_noisy_plot(
                    clean_samples, noisy_samples,
                    item["name"] + " Received Signal Waveform",
                    len(data)
                ),
                use_container_width=True
            )
            
            with st.expander("🔍 Inspect Channel Noise Floor Waveform"):
                st.pyplot(
                    create_noise_plot(
                        noise_samples,
                        item["name"] + " Isolated Channel Noise",
                        len(data)
                    ),
                    use_container_width=True
                )

            recovered_scrambled = item["decoder"](noisy_samples, len(data))
            recovered_original = xor_bits(recovered_scrambled, scrambling_sequence)
            acc, correct, errors = accuracy_percent(data, recovered_original)
            ber = errors / len(data)

            results.append({
                "Algorithm": item["name"],
                "Accuracy (%)": round(acc, 2),
                "Correct Bits": correct,
                "Incorrect Bits": errors,
                "Bit Error Rate": round(ber, 4),
                "Recovered Data": "".join(map(str, recovered_original))
            })

            st.markdown("#### Receiver Demodulation Results")
            r1, r2, r3 = st.columns(3)
            with r1:
                st.metric("Bit Accuracy", f"{acc:.2f}%")
            with r2:
                st.metric("Correct Demodulations", f"{correct} / {len(data)}")
            with r3:
                st.metric("Bit Errors Detected", errors)

            st.markdown("**Recovered Binary Stream:**")
            st.code(" ".join(map(str, recovered_original)), language=None)
            
            if errors == 0:
                st.success("✨ Zero bit errors! Perfect channel recovery achieved.")
            else:
                st.warning(f"⚠️ {errors} transmission error(s) identified due to channel distortion.")

    st.markdown('<div class="section-title">🎯 Comparative Performance Summary</div>', unsafe_allow_html=True)
    best_result = max(results, key=lambda result: result["Accuracy (%)"])
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Highest Accuracy", f'{best_result["Accuracy (%)"]:.2f}%')
    with m2:
        st.metric("Optimal Scheme", best_result["Algorithm"])
    with m3:
        st.metric("Noise Level", f"{noise_strength}%")

    st.dataframe(results, use_container_width=True, hide_index=True)

else:
    st.markdown("""
    <div style="background:#3E5BA3;padding:40px;border-radius:18px;text-align:center;border:1px solid #75CBD1;box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);">
      <h2 style="color:#F2D2FF;margin-top:0;">🚀 Simulator Ready</h2>
      <p style="font-size:16px;color:#DAE8FB;max-width:600px;margin:0 auto 20px auto;">
        Configure your data stream parameters and channel noise profiles in the sidebar control panel, then click <b>Run Simulation Pipeline</b> to visualize end-to-end signal transmission.
      </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
  <b>Digital Communication Simulator Pro</b> • Advanced Telemetry & Line Coding Suite<br>
  Engineering College Project Architecture
</div>
""", unsafe_allow_html=True)