"""Check the metadata and local links used by this Skill."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "project-code-discipline"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    source = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", source, re.S)
    require(frontmatter, "SKILL.md needs frontmatter.")
    metadata = frontmatter.group(1)
    require(re.search(r"^name: " + re.escape(SKILL.name) + r"$", metadata, re.M),
            "Skill name must match the directory.")
    require(re.search(r'^description: ".+"$', metadata, re.M), "Missing description.")
    version = re.search(r'^  version: "(\d+\.\d+\.\d+)"$', metadata, re.M)
    require(version, "Missing semantic version.")
    require(f"## v{version.group(1)}\n" in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"),
            "Changelog must contain the current version.")
    for file in ROOT.rglob("*.md"):
        if any(part in {".git", "codexwork", ".venv", "dist"} for part in file.relative_to(ROOT).parts):
            continue
        for href in re.findall(r"\]\(([^()\s]+)\)", file.read_text(encoding="utf-8")):
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (file.parent / unquote(url.path)).resolve()
            require(target.is_relative_to(ROOT) and target.exists(),
                    f"Broken local link: {file.relative_to(ROOT)} -> {href}")
    require((ROOT / "LICENSE").read_bytes() == (SKILL / "LICENSE").read_bytes(),
            "Repository and Skill licenses must match.")
    print(f"Skill v{version.group(1)} metadata, local links and license checked.")


if __name__ == "__main__":
    main()
