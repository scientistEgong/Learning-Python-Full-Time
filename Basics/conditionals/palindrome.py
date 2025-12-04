# Check if a string is a palindrome.
# when a string is reversed it should be the same thing.
# Should be able to flag numbers.

def is_palindrome():
    while True:
        word_input = input("Enter a word or 'q' to quit: ")

        # Catch integer inputs.
        if any(word.isdigit() for word in word_input) :
            print("Integers are not allowed! Enter a word.")
            continue

        if word_input.lower() == "q":
            print("Exiting...")
            break

        parsed_string = "".join(word_input.split())
        reversed_word = parsed_string[::-1]
        if reversed_word == parsed_string:
            palindrome = f"{parsed_string} => {reversed_word}\nThis is a palindrome."

        else:
            palindrome = f"{parsed_string} => {reversed_word} This is not a palindrome."
        print(palindrome)        

is_palindrome()



# from chatgpt
# Robust palindrome checker for Unicode-aware text
# Requires: (optional) `regex` package for true grapheme-cluster support:
#    pip install regex
#
# Behavior:
#   - Normalizes to NFC
#   - Removes punctuation / whitespace (Unicode categories P* and Z*)
#   - Keeps letters, marks, numbers, symbols (including emoji)
#   - Uses grapheme clusters when regex is available
#   - Parameterize how to treat digits: "reject", "ignore", or "keep"

import unicodedata

try:
    import regex as _regex  # third-party; preferred for \X grapheme clusters
    _HAS_REGEX = True
except Exception:
    _HAS_REGEX = False

def _graphemes(s: str):
    """Return a list of grapheme clusters for s.
    Uses regex \X if available; otherwise falls back to list(s)."""
    if _HAS_REGEX:
        return _regex.findall(r'\X', s)
    else:
        # Fallback: naive character-by-character (not ideal for emoji/ZWJ, but usable)
        return list(s)

def _is_punctuation_or_separator(ch: str) -> bool:
    cat = unicodedata.category(ch)
    # 'P*' punctuation, 'Z*' separators (space, line separators)
    return cat.startswith('P') or cat.startswith('Z')

def normalized_filtered_graphemes(text: str, digits_mode: str = "reject"):
    """
    digits_mode: "reject" (default) -> if any ASCII/Unicode digit present, raise ValueError
                 "ignore"  -> strip digits out before checking
                 "keep"    -> treat digits like other characters (kept)
    Returns list of normalized (NFC) grapheme clusters to be compared.
    """
    if digits_mode not in {"reject", "ignore", "keep"}:
        raise ValueError("digits_mode must be 'reject', 'ignore' or 'keep'")

    # Normalize to NFC (composed form)
    text = unicodedata.normalize("NFC", text)

    # Quick digit check (covers ASCII and other Unicode digits)
    if digits_mode == "reject":
        for ch in text:
            if unicodedata.category(ch).startswith("N"):  # Number category
                raise ValueError("Input contains numeric characters and digits_mode='reject'")

    g = _graphemes(text)

    out = []
    for cluster in g:
        # cluster may be multiple code points (emoji sequences, base+combining marks, ...)
        # decide whether to keep it:
        # if every codepoint in cluster is punctuation/separator, drop it.
        # if it contains at least one non-(P or Z) codepoint, we keep the cluster
        if all(_is_punctuation_or_separator(ch) for ch in cluster):
            continue

        # handle digits_mode == "ignore": drop cluster if it's numeric
        if digits_mode == "ignore" and all(unicodedata.category(ch).startswith("N") for ch in cluster):
            continue

        # keep cluster, casefold for caseless comparison (casefold works on strings)
        out.append(cluster.casefold())

    return out

def is_palindrome_unicode(text: str, digits_mode: str = "reject") -> bool:
    """
    Returns True if text is a palindrome under the chosen rules.
    digits_mode as in normalized_filtered_graphemes.
    """
    clusters = normalized_filtered_graphemes(text, digits_mode=digits_mode)
    return clusters == list(reversed(clusters))


# -----------------------
# Example usage / tests
# -----------------------
if __name__ == "__main__":
    examples = [
        "Madam, I'm Adam",
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "été",            # accent composed/ decomposed issues
        "e\u0301",        # 'e' + combining acute
        "𝔘𝔫𝔦𝔠𝔬𝔡𝔢",        # fancy characters (mathematical alts)
        "👩‍👩‍👧‍👦👦‍👧‍👩‍👩", # emoji sequences (depends on grapheme handling)
        "12321",          # numeric palindrome
        "h3ll0",          # contains digits inside word
    ]

    for s in examples:
        try:
            print(f"'{s}' -> {is_palindrome_unicode(s, digits_mode='reject')}")
        except ValueError as e:
            print(f"'{s}' -> rejected: {e}")

    # Try with digits ignored:
    print("\nDigits ignored mode:")
    print("'12321' ->", is_palindrome_unicode("12321", digits_mode="ignore"))
    print("'h3ll0' ->", is_palindrome_unicode("h3ll0", digits_mode="ignore"))

    # Note whether regex support is active:
    print("\nGrapheme cluster support available:", _HAS_REGEX)
