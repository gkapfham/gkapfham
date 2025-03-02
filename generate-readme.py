from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

# teaching links
teaching_tree = Tree(
    "🎉 Teaching",
    guide_style="bold red",
)
teaching_tree.add("[link=https://algorithmology.org/]Algorithm Analysis[/link]")
teaching_tree.add("[link=https://securitysynapse.org/]Computer Security[/link]")
teaching_tree.add("[link=https://developerdevelopment.com/]Software Engineering[/link]")

# research links
research_tree = Tree(
    "🔬 Research",
    guide_style="bold red",
)
research_tree.add(
    "[link=https://www.gregorykapfhammer.com/research/papers/#category=test-suite%20prioritization]Regression Testing[/link]"
)
research_tree.add(
    "[link=https://www.gregorykapfhammer.com/research/papers/#category=mutation%20testing]Mutation Testing[/link]"
)
research_tree.add(
    "[link=https://www.gregorykapfhammer.com/research/papers/#category=flaky%20tests]Flaky Tests[/link]"
)

software_tree = Tree(
    "🛠️ Software",
    guide_style="bold red",
)
software_tree.add("[link=https://github.com/AstuteSource/chasten]Chasten[/link]")
software_tree.add("[link=https://github.com/GatorEducator/gatorgrade]GatorGrade[/link]")
software_tree.add("[link=https://github.com/GatorEducator/reporover]RepoRover[/link]")

podcast_tree = Tree(
    "🎤 Podcasts",
    guide_style="bold red",
)
podcast_tree.add(
    "[link=https://se-radio.net/2024/09/se-radio-632-goran-petrovic-on-mutation-testing-at-google/]SE Radio Episode 632[/link]"
)
podcast_tree.add(
    "[link=https://se-radio.net/2024/07/se-radio-625-jonathan-schneider-on-automated-refactoring-with-openrewrite/]SE Radio Episode 625[/link]"
)
podcast_tree.add(
    "[link=https://se-radio.net/2024/07/se-radio-624-marcelo-trylesinski-on-fastapi/]SE Radio Episode 624[/link]"
)

about = """\
\nHello, my name is [link=https://www.gregorykapfhammer.com]Gregory M. Kapfhammer![/link] I'm a faculty member in the Department of Computer and Information Science at Allegheny College. I'm a professor, researcher, engineer, and podcaster.
"""

panel = Panel.fit(
    about,
    box=box.ROUNDED,
    border_style="blue",
    title="Professional Introduction",
    width=70,
)

console.print()
console.print(Columns([panel]))
console.print()
console.print(Columns([teaching_tree, research_tree], width=30))
console.print()
console.print(Columns([software_tree, podcast_tree], width=30))
console.print()
console.print("🤖 Want to know how I made this content? Clone this GitHub repository: [link=https://github.com/gkapfham/gkapfham]gkapfham/gkapfham[/link]")
console.print()
console.print(
    "🚧 Run this command to generate the README.md file: uv run --with rich generate-readme.py"
)

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
