%%writefile app.py

import random
import streamlit as st
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Digital Communication Simulator",
    page_icon="📡",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-title {
        font-size: 26px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    /* Algorithm cards */
    .algorithm-card {
        background-color: white;
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #e2e5eb;
        min-height: 190px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
    }

    .algorithm-card h3 {
        margin-top: 0px;
        font-size: 22px;
    }

    .algorithm-card p {
        font-size: 15px;
        line-height: 1.6;
    }

    /* Data cards */
    .data-card {
        background-color: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e2e5eb;
        text-align: center;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
    }

    .data-title {
        font-size: 15px;
        font-weight: 600;
    }

    .data-value {
        font-size: 18px;
        font-weight: 600;
        word-break: break-word;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 25px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📡 Digital Communication Simulator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'LFSR Scrambling • XOR Processing • Digital Line Coding'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ============================================================
# ALGORITHM OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-title">🔬 Line Coding Algorithms</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("""
    <div class="algorithm-card">

    <h3>📊 NRZ-L</h3>

    <p>
    <b>Non-Return-to-Zero-Level</b>
    </p>

    <p>
    1 → +1<br>
    0 → -1
    </p>

    <p>
    Simple level-based encoding.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="algorithm-card">

    <h3>🔄 NRZ-I</h3>

    <p>
    <b>Non-Return-to-Zero Inverted</b>
    </p>

    <p>
    1 → Transition<br>
    0 → No Transition
    </p>

    <p>
    Encoding depends on the previous signal level.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="algorithm-card">

    <h3>⚡ Manchester</h3>

    <p>
    <b>Manchester Encoding</b>
    </p>

    <p>
    1 → -1 to +1<br>
    0 → +1 to -1
    </p>

    <p>
    Every bit contains a middle transition.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚙️ Simulator Controls")

st.sidebar.markdown(
    "### 1. Select Data Source"
)

data_mode = st.sidebar.radio(
    "Data Source",
    [
        "Random Data",
        "Enter Binary Data"
    ]
)


# ============================================================
# DATA INPUT
# ============================================================

if data_mode == "Random Data":

    number_of_bits = st.sidebar.slider(
        "Number of Bits",
        min_value=5,
        max_value=50,
        value=20
    )

else:

    binary_input = st.sidebar.text_input(
        "Enter Binary Data",
        value="101100101001"
    )


st.sidebar.markdown(
    "### 2. Generate"
)

generate_button = st.sidebar.button(
    "🚀 Generate Communication Signal",
    use_container_width=True
)


# ============================================================
# LFSR FUNCTION
# ============================================================

def lfsr_sequence(length):

    register = [1, 0, 1, 1]

    sequence = []

    for i in range(length):

        # Last register bit is used as output
        output = register[-1]

        # XOR first and last register bits
        feedback = register[0] ^ register[3]

        # Shift register
        register = [feedback] + register[:3]

        sequence.append(output)

    return sequence


# ============================================================
# NRZ-L ENCODING
# ============================================================

def nrz_l_encode(data):

    signal = []

    for bit in data:

        if bit == 1:
            signal.append(1)

        else:
            signal.append(-1)

    return signal


# ============================================================
# NRZ-I ENCODING
# ============================================================

def nrz_i_encode(data):

    signal = []

    # Initial signal level
    current_level = -1

    for bit in data:

        # A 1 causes a transition
        if bit == 1:

            current_level = -current_level

        # A 0 does not change the level

        signal.append(current_level)

    return signal


# ============================================================
# MANCHESTER ENCODING
# ============================================================

def manchester_encode(data):

    signal = []

    for bit in data:

        if bit == 1:

            # 1 = -1 to +1
            signal.append(-1)
            signal.append(1)

        else:

            # 0 = +1 to -1
            signal.append(1)
            signal.append(-1)

    return signal


# ============================================================
# PLOT FUNCTION
# ============================================================

def create_plot(signal, title, bit_count, manchester=False):

    fig, ax = plt.subplots(figsize=(12, 4))

    x_values = range(len(signal))

    ax.step(
        x_values,
        signal,
        where="post"
    )

    ax.axhline(
        0,
        linewidth=1
    )

    ax.set_title(
        title,
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Bit Position")

    ax.set_ylabel("Signal Level")

    ax.set_ylim(-1.5, 1.5)

    ax.set_yticks([-1, 0, 1])

    if manchester:

        ax.set_xticks(
            [i * 2 for i in range(bit_count)]
        )

    else:

        ax.set_xticks(
            range(bit_count)
        )

    ax.grid(
        True,
        alpha=0.3
    )

    plt.tight_layout()

    return fig


# ============================================================
# MAIN PROCESS
# ============================================================

if generate_button:

    # --------------------------------------------------------
    # STEP 1: GET DIGITAL DATA
    # --------------------------------------------------------

    if data_mode == "Random Data":

        data = []

        for i in range(number_of_bits):

            bit = random.randint(0, 1)

            data.append(bit)

    else:

        # Remove spaces from input
        binary_input = binary_input.replace(" ", "")

        # Check whether input contains only 0 and 1
        if binary_input == "":

            st.error("Please enter binary data.")

            st.stop()

        if not all(bit in "01" for bit in binary_input):

            st.error(
                "Invalid input! Please enter only 0 and 1."
            )

            st.stop()

        data = [
            int(bit)
            for bit in binary_input
        ]


    # --------------------------------------------------------
    # STEP 2: GENERATE LFSR SEQUENCE
    # --------------------------------------------------------

    scrambling_sequence = lfsr_sequence(
        len(data)
    )


    # --------------------------------------------------------
    # STEP 3: SCRAMBLING USING XOR
    # --------------------------------------------------------

    scrambled_data = []

    for i in range(len(data)):

        scrambled_bit = (
            data[i]
            ^ scrambling_sequence[i]
        )

        scrambled_data.append(
            scrambled_bit
        )


    # --------------------------------------------------------
    # STEP 4: APPLY ALL THREE LINE CODING ALGORITHMS
    # --------------------------------------------------------

    nrzl_signal = nrz_l_encode(
        scrambled_data
    )

    nrzi_signal = nrz_i_encode(
        scrambled_data
    )

    manchester_signal = manchester_encode(
        scrambled_data
    )


    # ========================================================
    # DATA PROCESSING SECTION
    # ========================================================

    st.markdown(
        '<div class="section-title">📊 Data Processing</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            '<div class="data-card">'
            '<div class="data-title">Original Digital Data</div>'
            '<br>'
            '<div class="data-value">'
            + " ".join(map(str, data))
            + '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            '<div class="data-card">'
            '<div class="data-title">LFSR Scrambling Sequence</div>'
            '<br>'
            '<div class="data-value">'
            + " ".join(
                map(
                    str,
                    scrambling_sequence
                )
            )
            + '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            '<div class="data-card">'
            '<div class="data-title">Scrambled Data</div>'
            '<br>'
            '<div class="data-value">'
            + " ".join(
                map(
                    str,
                    scrambled_data
                )
            )
            + '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # SIGNAL SUMMARY
    # ========================================================

    st.markdown(
        '<div class="section-title">📈 Signal Summary</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Number of Bits",
            len(data)
        )


    with col2:

        st.metric(
            "LFSR Register",
            "1011"
        )


    with col3:

        st.metric(
            "Algorithms",
            "3"
        )


    # ========================================================
    # WAVEFORMS
    # ========================================================

    st.markdown(
        '<div class="section-title">📡 Waveform Analysis</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # NRZ-L
    # --------------------------------------------------------

    st.subheader(
        "1️⃣ NRZ-L — Non-Return-to-Zero-Level"
    )

    st.info(
        "Mapping: 1 → +1   |   0 → -1"
    )

    st.pyplot(
        create_plot(
            nrzl_signal,
            "NRZ-L Encoded Signal",
            len(data)
        )
    )


    # --------------------------------------------------------
    # NRZ-I
    # --------------------------------------------------------

    st.subheader(
        "2️⃣ NRZ-I — Non-Return-to-Zero Inverted"
    )

    st.info(
        "Mapping: 1 → Transition   |   0 → No Transition"
    )

    st.pyplot(
        create_plot(
            nrzi_signal,
            "NRZ-I Encoded Signal",
            len(data)
        )
    )


    # --------------------------------------------------------
    # MANCHESTER
    # --------------------------------------------------------

    st.subheader(
        "3️⃣ Manchester Encoding"
    )

    st.info(
        "Mapping: 1 → -1 to +1   |   0 → +1 to -1"
    )

    st.pyplot(
        create_plot(
            manchester_signal,
            "Manchester Encoded Signal",
            len(data),
            manchester=True
        )
    )


    # ========================================================
    # COMPARISON TABLE
    # ========================================================

    st.markdown(
        '<div class="section-title">📋 Algorithm Comparison</div>',
        unsafe_allow_html=True
    )


    comparison_data = {

        "Algorithm": [
            "NRZ-L",
            "NRZ-I",
            "Manchester"
        ],

        "Representation": [
            "1 = +1, 0 = -1",
            "1 = Transition, 0 = No Transition",
            "Middle-bit transition"
        ],

        "Synchronization": [
            "Low",
            "Moderate",
            "High"
        ],

        "Bandwidth": [
            "Low",
            "Low",
            "Higher"
        ],

        "Complexity": [
            "Low",
            "Low",
            "Moderate"
        ]
    }


    st.table(
        comparison_data
    )


    # ========================================================
    # EDUCATIONAL INFORMATION
    # ========================================================

    st.markdown(
        '<div class="section-title">📚 Algorithm Information</div>',
        unsafe_allow_html=True
    )


    tab1, tab2, tab3 = st.tabs(
        [
            "NRZ-L",
            "NRZ-I",
            "Manchester"
        ]
    )


    with tab1:

        st.markdown("""
        ### NRZ-L

        **Full Form:** Non-Return-to-Zero-Level

        NRZ-L represents digital bits using different
        voltage levels.

        **Mapping:**

        - Bit 1 → +1
        - Bit 0 → -1

        **Advantages:**
        - Simple implementation
        - Low bandwidth requirement
        - Easy to understand

        **Disadvantage:**
        - Long sequences of the same bit can make
          synchronization difficult.
        """)


    with tab2:

        st.markdown("""
        ### NRZ-I

        **Full Form:** Non-Return-to-Zero Inverted

        NRZ-I represents data using changes in signal level.

        **Mapping:**

        - Bit 1 → Signal transition
        - Bit 0 → No transition

        **Advantages:**
        - Simple implementation
        - Uses transitions to represent data

        **Disadvantage:**
        - Long sequences of 0s can still cause
          synchronization problems.
        """)


    with tab3:

        st.markdown("""
        ### Manchester Encoding

        Manchester encoding introduces a transition
        in the middle of every bit period.

        **Mapping used in this simulator:**

        - Bit 1 → -1 to +1
        - Bit 0 → +1 to -1

        **Advantages:**
        - Excellent synchronization
        - Every bit contains a transition
        - Clock recovery is easier

        **Disadvantage:**
        - Requires more bandwidth than NRZ techniques.
        """)


# ============================================================
# INITIAL MESSAGE
# ============================================================

else:

    st.markdown("""
    <div style="
        background-color:white;
        padding:30px;
        border-radius:15px;
        text-align:center;
        border:1px solid #e2e5eb;
    ">

    <h2>🚀 Ready to Simulate</h2>

    <p style="font-size:17px;">
    Select your data source from the sidebar and click
    <b>Generate Communication Signal</b> to start the simulation.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
    <b>Digital Communication Simulator</b><br>
    LFSR Scrambling + XOR + NRZ-L + NRZ-I + Manchester<br><br>
    Engineering College Project
    </div>
    """,
    unsafe_allow_html=True
)
