
import random
import matplotlib.pyplot as plt

data = []

for i in range(20):
    bit = random.randint(0, 1)
    data.append(bit)

print("Original Digital Data:")
print(data)


def lfsr_sequence(length):

    register = [1, 0, 1, 1]
    sequence = []

    for i in range(length):

        output = register[-1]

        feedback = register[0] ^ register[3]

        register = [feedback] + register[:3]

        sequence.append(output)

    return sequence


scrambling_sequence = lfsr_sequence(len(data))

print("\nLFSR Scrambling Sequence:")
print(scrambling_sequence)


scrambled_data = []

for i in range(len(data)):

    scrambled_bit = data[i] ^ scrambling_sequence[i]

    scrambled_data.append(scrambled_bit)


print("\nScrambled Data:")
print(scrambled_data)


def nrz_l_encode(data):

    signal = []

    for bit in data:

        if bit == 1:
            signal.append(1)

        else:
            signal.append(-1)

    return signal


encoded_signal = nrz_l_encode(scrambled_data)

print("\nNRZ-L Signal Levels:")
print(encoded_signal)


plt.figure(figsize=(12, 3))

plt.step(range(len(data)), data, where='post')

plt.title("Original Digital Data")
plt.xlabel("Bit")
plt.ylabel("Value")

plt.ylim(-0.5, 1.5)
plt.grid()

plt.show()


plt.figure(figsize=(12, 3))

plt.step(range(len(scrambled_data)), scrambled_data, where='post')

plt.title("Scrambled Digital Data")
plt.xlabel("Bit")
plt.ylabel("Value")

plt.ylim(-0.5, 1.5)
plt.grid()

plt.show()


plt.figure(figsize=(12, 4))

plt.step(
    range(len(encoded_signal)),
    encoded_signal,
    where='post'
)

plt.title("NRZ-L Encoded Signal")

plt.xlabel("Bit")
plt.ylabel("Amplitude")

plt.ylim(-1.5, 1.5)
plt.yticks([-1, 0, 1])

plt.grid()

plt.show()
