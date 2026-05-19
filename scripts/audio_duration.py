def get_audio_duration_seconds(sample_rate, num_samples):
    """Return audio duration in seconds."""
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")
    return num_samples / sample_rate


def main():
    sample_rate = int(input("Enter sample rate in Hz: "))
    num_samples = int(input("Enter number of samples: "))
    duration = get_audio_duration_seconds(sample_rate, num_samples)
    print(f"Duration: {duration:.2f} seconds")


if __name__ == "__main__":
    main()