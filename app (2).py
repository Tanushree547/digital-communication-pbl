
import random
import streamlit as st
import matplotlib.pyplot as plt


# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("Digital Communication System")
st.write("LFSR Scrambling + NRZ-L Line Encoding")


# -------------------------------------------------
# Number of bits
# -------------------------------------------------

number_of_bits = st.number_input(
    "Enter number of bits",
    min_value=5,
    max_value=100,
    value=20
)


# -------------------------------------------------
# Generate Signal button
# -------------------------------------------------

if st.button("Generate Signal"):

    # -------------------------------------------------
    # STEP 1: Generate Digital Data
    # -------------------------------------------------

    data = []

    for i in range(number_of_bits):
        bit = random.randint(0, 1)
        data.append(bit)

    st.subheader("1. Original Digital Data")
    st.write(data)


    # -------------------------------------------------
    # STEP 2: Generate LFSR Scrambling Sequence
    # -------------------------------------------------

    def lfsr_sequence(length):

        register = [1, 0, 1, 1]
        sequence = []

        for i in range(length):

            # Take the last bit as output
            output = register[-1]

            # XOR first and last bit
            feedback = register[0] ^ register[3]

            # Shift the register
            register = [feedback] + register[:3]

            # Store output
            sequence.append(output)

        return sequence


    scrambling_sequence = lfsr_sequence(len(data))

    st.subheader("2. LFSR Scrambling Sequence")
    st.write(scrambling_sequence)


    # -------------------------------------------------
    # STEP 3: Scramble the Digital Data
    # -------------------------------------------------

    scrambled_data = []

    for i in range(len(data)):

        scrambled_bit = data[i] ^ scrambling_sequence[i]

        scrambled_data.append(scrambled_bit)

    st.subheader("3. Scrambled Data")
    st.write(scrambled_data)


    # -------------------------------------------------
    # STEP 4: NRZ-L Line Encoding
    # -------------------------------------------------

    def nrz_l_encode(data):

        signal = []

        for bit in data:

            if bit == 1:
                signal.append(1)
            else:
                signal.append(-1)

        return signal


    encoded_signal = nrz_l_encode(scrambled_data)

    st.subheader("4. NRZ-L Signal Levels")
    st.write(encoded_signal)


    # -------------------------------------------------
    # STEP 5: Plot Original Digital Data
    # -------------------------------------------------

    st.subheader("5. Original Digital Data")

    fig1, ax1 = plt.subplots(figsize=(12, 3))

    ax1.step(
        range(len(data)),
        data,
        where="post"
    )

    ax1.set_title("Original Digital Data")
    ax1.set_xlabel("Bit")
    ax1.set_ylabel("Value")
    ax1.set_ylim(-0.5, 1.5)
    ax1.grid()

    st.pyplot(fig1)


    # -------------------------------------------------
    # STEP 6: Plot Scrambled Data
    # -------------------------------------------------

    st.subheader("6. Scrambled Digital Data")

    fig2, ax2 = plt.subplots(figsize=(12, 3))

    ax2.step(
        range(len(scrambled_data)),
        scrambled_data,
        where="post"
    )

    ax2.set_title("Scrambled Digital Data")
    ax2.set_xlabel("Bit")
    ax2.set_ylabel("Value")
    ax2.set_ylim(-0.5, 1.5)
    ax2.grid()

    st.pyplot(fig2)


    # -------------------------------------------------
    # STEP 7: Plot NRZ-L Encoded Signal
    # -------------------------------------------------

    st.subheader("7. NRZ-L Encoded Signal")

    fig3, ax3 = plt.subplots(figsize=(12, 4))

    ax3.step(
        range(len(encoded_signal)),
        encoded_signal,
        where="post"
    )

    ax3.set_title("NRZ-L Encoded Signal")
    ax3.set_xlabel("Bit")
    ax3.set_ylabel("Amplitude")
    ax3.set_ylim(-1.5, 1.5)
    ax3.set_yticks([-1, 0, 1])
    ax3.grid()

    st.pyplot(fig3)
