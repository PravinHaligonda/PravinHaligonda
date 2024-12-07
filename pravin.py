from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(":call_me_hand: [link=https://www.linkedin.com/in/pravinhaligonda/]Pravin Haligonda", guide_style="bold cyan")
python_tree = tree.add(":computer: Computer & Computational Linguist", guide_style="green")
python_tree.add("DL Engineer")
python_tree.add("Rust Language")
python_tree.add("MakeMore")
interest_tree = tree.add(":speaking_head: Interest")
interest_tree.add("Object Detection")
interest_tree.add("Video Processing")
tree.add(":open_book: Reading")

about = """\
I’m a curious computer person who loves turning ideas into reality — solving problems,
focusing on open source, Video processing, DL.
I love Rust Language. 

Follow me on Twitter! [link=https://x.com/pravinhaligonda]@pravinhaligonda
"""

panel = Panel.fit(about, box=box.DOUBLE, border_style="blue", title="[b]Hey hey! :wave:", width=60)
console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo, 'DejaVu Sans Mono', consoles, 'Courier New', monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
