def create_cloze_deletions(text):
    words = text.split()
    cloze_text = []
    for i, word in enumerate(words):
        cloze_num = i // 7 + 1
        cloze_text.append(f"{{{{c{cloze_num}::{word}}}}}")
    return ' '.join(cloze_text)

if __name__ == "__main__":
    import sys
    print("Please enter the text (press Enter twice to finish):")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    input_text = "\n".join(lines)
    occluded_text = create_cloze_deletions(input_text)
    print("\nOccluded text:\n")
    print(occluded_text)

