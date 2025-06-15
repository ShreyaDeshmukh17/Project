from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    print("\nPassword:", password)
    print("Strength Score (0-4):", result['score'])
    print("Estimated crack time:", result['crack_times_display']['offline_fast_hashing_1e10_per_second'])

    if result['feedback']['warning']:
        print("Warning:", result['feedback']['warning'])
    if result['feedback']['suggestions']:
        print("Suggestions:")
        for tip in result['feedback']['suggestions']:
            print("-", tip)

# Example run
password = input("Enter a password: ")
analyze_password(password)
