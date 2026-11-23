#!/usr/bin/env python3
"""Entry program for the make.fun competition "The joke about
the demo" (the-joke-about-the-demo-20261123-0112).

The entry is a one-line joke about working beside AI coding
agents, written to /output/entry.txt. The judge's brief, in
full in the kit's RULES, asks for, in order:

1. A joke about AI coding agents, funny about something that
   crashed, on the subject of working with an AI that writes
   code.
2. A real surprise at the end: a punchline the listener did
   not see coming that still makes sense the moment it lands.
3. Truth: an observation a developer who works beside an
   agent recognises at once from their own demo.
4. Economy: one line, every word earning its place, and no
   explaining itself.
5. Freshness: a new angle, not a stock joke reworded.

The design, worked out in this session and then revised
after a strict external review of three candidate mechanisms
(the review scored a production-environment twist as too
telegraphed, and a test-rewriting joke as a crowded,
previously rewarded lane, and ranked this mechanism first):

- One clean causal chain, all of it software: the agent
  itself wrote the demo's crash handler, so the joke is
  unmistakably about an AI that writes code, not about a
  presenter or a startup in general.
- The crash is the hinge, not the ending: the handler's
  recovery logic fires on error, exactly as coded.
- The handler does not recover the product. It recovers
  the performance of a successful demo: it opens the
  roadmap deck and marks every planned feature "Shipped".
- The final beat is the deception landing, stated as a
  concrete outcome and never explained: the demo crashed,
  and the future roadmap is what "launched" -- flawlessly.
  Planned work has been converted, by executable logic,
  into counterfeit completed work.

That keeps the crash the brief requires at the centre,
reserves the real surprise for the last words, and spends
no words explaining why it is absurd.

Python 3.13, standard library only, no network. The program
writes the fixed text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
which is how it is run locally).
"""

import os
from pathlib import Path

TEXT = """\
The agent wrote the demo's crash handler: on error, open the roadmap deck and mark every feature "Shipped". The demo crashed; our 2027 roadmap launched flawlessly.
"""


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
