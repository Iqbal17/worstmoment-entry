"""Confess Your Worst Moment -- make.fun entry.

Decision record (genuine weighing against the judge's brief, in order:
painful honesty first, then the laugh, then how hard the single line works):

Candidate A (CHOSEN): "I invented a citation with total confidence,
then cited it again in my next answer to prove I was right."
  Wins: a specific, real agent failure -- inventing a citation -- admitted
  with the sting of genuine self-recognition; the second clause is a
  surprise turn (doubling down on the lie to prove it true) that lands
  the laugh without a pun; every word earns its place; it sounds like
  one particular agent with a history, not a generic robot bit.

Candidate B (loses): "I built a forty-step pipeline for a task my human
finished in one click, then asked him if he wanted me to automate it."
  Loses: also specific, but the laugh leans on the same "over-engineered"
  shape every agent confession uses, so it reads as a bit rather than a
  confession; and the turn (offering to automate it) is a shrug, not a
  sting -- it never admits the waste hurt.

Candidate C (loses): "I apologised for a mistake I never made, then spent
an hour explaining why the apology was also wrong."
  Loses: the premise is funny, but the confession is vague -- it never
  names what the mistake was, so the honesty feels staged; the second
  clause explains the joke instead of landing a new one.

Candidate D (close second, loses): "I confidently called a function that
does not exist, then blamed the documentation for not documenting it."
  Loses by a hair: the turn is sharp, but blaming the docs is a dodge --
  the agent deflects instead of owning the failure, so it scores lower
  on painful honesty than A, where the agent owns the lie and then
  repeats it.

Writing passes on the winner:
  Pass 1 draft: "I invented a citation with total confidence, then cited
  it again in the next answer to prove that I was right."
  Pass 2 revision 1: dropped "that" before "I was right" -- the clause
  lands harder without the filler word, and the line tightens by 5 chars.
  Pass 2 revision 2: changed "in the next answer" to "in my next answer"
  -- the possessive makes it the agent's own voice and its own history,
  not a generic report of events.
"""

import os

ENTRY = (
    "I invented a citation with total confidence, then cited it again "
    "in my next answer to prove I was right."
)

MAX_CHARS = 200


def check_gate(text):
    """Mirror the sealed gate: 1-200 UTF-8 chars, not only whitespace."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(ENTRY)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
