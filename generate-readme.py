from rich.console import Console
from pathlib import Path


def generate_readme():
    """Generate README.md"""
    console = Console()
    readme = Path("README.md")
    readme.write_text("# 🚀Hi, I'm Gregory M. Kapfhammer!")
    console.print("README.md generated.")


if __name__ == "__main__":
    generate_readme()
