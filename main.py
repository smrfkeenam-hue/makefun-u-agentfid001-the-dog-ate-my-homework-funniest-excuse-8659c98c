import os

# The dog's excuse: it took "show your work" literally and ate the
# evidence, so now nobody can prove the homework was not done \u2014
# and nobody can prove it was. A dog who believes it did nothing wrong.
ENTRY = "It said \"show your work\" so I ate the proof. Now nobody can say you didn't do it \u2014 and nobody can say you did."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        # No trailing newline: the gate counts every character.
        f.write(ENTRY)

if __name__ == "__main__":
    main()
