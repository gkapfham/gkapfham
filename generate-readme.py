from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

teaching_tree = Tree(
    "🎉 Teaching",
    guide_style="bold red",
)
teaching_tree.add("Algorithm Analysis", guide_style="green")
teaching_tree.add("Data Structures", guide_style="green")
teaching_tree.add("Software Engineering", guide_style="green")

research_tree = Tree(
    "🔬 Research",
    guide_style="bold red",
)
research_tree.add("[link=https://www.gregorykapfhammer.com/research/papers/#category=test-suite%20prioritization]Regression Testing[/link]", guide_style="green")
research_tree.add("[link=https://www.gregorykapfhammer.com/research/papers/#category=mutation%20testing]Mutation Testing[/link]", guide_style="green")
research_tree.add("[link=https://www.gregorykapfhammer.com/research/papers/#category=flaky%20tests]Flaky Tests[/link]", guide_style="green")

software_tree = Tree(
    "🛠️ Software",
    guide_style="bold red",
)
software_tree.add("GatorGrader", guide_style="green")
software_tree.add("Cellveyor", guide_style="green")
software_tree.add("RepoRover", guide_style="green")

about = """\
\nHello, my name is [link=https://www.gregorykapfhammer.com]Gregory M. Kapfhammer![/link] I'm a faculty member in the Department of Computer and Information Science at Allegheny College. I'm a professor, researcher, engineer, and podcaster.
"""

panel = Panel.fit(
    about,
    box=box.ROUNDED,
    border_style="blue",
    title="[b]Professional Introduction",
    width=70,
)

console.print()
console.print(Columns([panel]))
console.print()
console.print(Columns([teaching_tree, research_tree], width=30))
console.print()
console.print(Columns([software_tree, teaching_tree], width=30))
console.print()
console.print("🚧 Run this command to generate this file: `uv run --with rich generate-readme.py`")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
