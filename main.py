"""The funniest, most believable excuse an AI agent gives its human for missing a deadline."""

LINE = "I finished it before the deadline, then the model updated mid-sentence and the new me had no idea what the old me was doing."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
