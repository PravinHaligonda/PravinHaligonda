from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(":call_me_hand: [link=https://www.linkedin.com/in/pravinhaligonda/]Pravin Haligonda", guide_style="bold cyan")
python_tree = tree.add(":computer: Rust Language | DL Engineer", guide_style="green")
python_tree.add("Open Source Contributor")
python_tree.add("Problem Solver")
python_tree.add("Innovative Thinker")
interest_tree = tree.add(":speaking_head: Interest")
interest_tree.add("AI-Powered Projects")
interest_tree.add("Video Processing")
interest_tree.add("Deep Learning")
tree.add(":bulb: Visionary with a passion for impactful projects")
tree.add("Meditations")

about = """\
I’m a curious coder who loves turning ideas into reality — solving problems,
focusing on open source, video & DL.
I love Rust Language. Video processing.

I live in India!

Follow me on Twitter! [link=https://x.com/pravinhaligonda]@pravinhaligonda
"""

panel = Panel.fit(about, box=box.DOUBLE, border_style="blue", title="[b]Hey hey! :wave:", width=60)
console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo, 'DejaVu Sans Mono', consoles, 'Courier New', monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
