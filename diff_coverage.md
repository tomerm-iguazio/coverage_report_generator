# Diff Coverage
## Diff: origin/development...HEAD, staged and unstaged changes

- coverage_report_generator/__init__&#46;py (0.0%): Missing lines 7-9,11
- coverage_report_generator/diff_parser&#46;py (0.0%): Missing lines 10,12-14,17-18,21-24,27-28,34-39,42,52,54-55,57-62,64-72,74
- coverage_report_generator/io_utils&#46;py (0.0%): Missing lines 7,9-10,12,15-19,22-23,26-28
- coverage_report_generator/reporting&#46;py (0.0%): Missing lines 3,5,7,10,13-14,16-17,19-21,23-28,31,34,36-37,39-40,42-44,46
- main&#46;py (50.0%): Missing lines 21

## Summary

- **Total**: 85 lines
- **Missing**: 84 lines
- **Coverage**: 1%



## coverage_report_generator/__init__&#46;py

Lines 3-15

```python
   3 This package intentionally contains a few small, decoupled utilities to make it easy
   4 to import and reuse pieces from scripts or CI jobs.
   5 """
   6 
!  7 from .diff_parser import DiffCoverageSummary, parse_diff_cover_markdown
!  8 from .reporting import render_markdown_comment, render_text_table
!  9 from .io_utils import read_text, write_text, ensure_parent_dir
  10 
! 11 __all__ = [
  12     "DiffCoverageSummary",
  13     "parse_diff_cover_markdown",
  14     "render_markdown_comment",
  15     "render_text_table",
```


---



## coverage_report_generator/diff_parser&#46;py

Lines 6-32

```python
   6 The parser is intentionally tolerant: it uses a couple of regex heuristics rather
   7 than depending on a strict markdown schema.
   8 """
   9 
! 10 from __future__ import annotations
  11 
! 12 from dataclasses import dataclass
! 13 import re
! 14 from typing import Iterable, Optional
  15 
  16 
! 17 @dataclass(frozen=True)
! 18 class DiffCoverageSummary:
  19     """A compact summary of diff coverage."""
  20 
! 21     coverage_percent: Optional[float]
! 22     missing_lines: Optional[int]
! 23     measured_lines: Optional[int]
! 24     raw: str
  25 
  26 
! 27 _PERCENT_RE = re.compile(r"(?P<pct>\d+(?:\.\d+)?)\s*%")
! 28 _LINES_RE = re.compile(
  29     r"(?P<missing>\d+)\s*(?:missing|uncovered)\s*.*?out\s+of\s+(?P<measured>\d+)",
  30     re.IGNORECASE,
  31 )
```


---


Lines 30-46

```python
  30     re.IGNORECASE,
  31 )
  32 
  33 
! 34 def _first_match(pattern: re.Pattern, lines: Iterable[str]) -> Optional[re.Match]:
! 35     for line in lines:
! 36         m = pattern.search(line)
! 37         if m:
! 38             return m
! 39     return None
  40 
  41 
! 42 def parse_diff_cover_markdown(markdown_text: str) -> DiffCoverageSummary:
  43     """Parse a `diff-cover` markdown report and return a summary.
  44 
  45     Args:
  46         markdown_text: The content of the markdown report.
```


---


Lines 48-78

```python
  48     Returns:
  49         DiffCoverageSummary with best-effort extracted fields.
  50     """
  51 
! 52     lines = markdown_text.splitlines()
  53 
! 54     pct_match = _first_match(_PERCENT_RE, lines)
! 55     lines_match = _first_match(_LINES_RE, lines)
  56 
! 57     coverage_percent: Optional[float] = None
! 58     if pct_match:
! 59         try:
! 60             coverage_percent = float(pct_match.group("pct"))
! 61         except ValueError:
! 62             coverage_percent = None
  63 
! 64     missing_lines: Optional[int] = None
! 65     measured_lines: Optional[int] = None
! 66     if lines_match:
! 67         try:
! 68             missing_lines = int(lines_match.group("missing"))
! 69             measured_lines = int(lines_match.group("measured"))
! 70         except ValueError:
! 71             missing_lines = None
! 72             measured_lines = None
  73 
! 74     return DiffCoverageSummary(
  75         coverage_percent=coverage_percent,
  76         missing_lines=missing_lines,
  77         measured_lines=measured_lines,
  78         raw=markdown_text,
```


---



## coverage_report_generator/io_utils&#46;py

Lines 3-30

```python
   3 These wrappers make it easier to mock IO in the future, but they're also handy
   4 for keeping scripts small and readable.
   5 """
   6 
!  7 from __future__ import annotations
   8 
!  9 from pathlib import Path
! 10 from typing import Union
  11 
! 12 PathLike = Union[str, Path]
  13 
  14 
! 15 def ensure_parent_dir(path: PathLike) -> Path:
! 16     p = Path(path)
! 17     if p.parent and not p.parent.exists():
! 18         p.parent.mkdir(parents=True, exist_ok=True)
! 19     return p
  20 
  21 
! 22 def read_text(path: PathLike, encoding: str = "utf-8") -> str:
! 23     return Path(path).read_text(encoding=encoding)
  24 
  25 
! 26 def write_text(path: PathLike, text: str, encoding: str = "utf-8") -> None:
! 27     p = ensure_parent_dir(path)
! 28     p.write_text(text, encoding=encoding)
  29 
```


---



## coverage_report_generator/reporting&#46;py

Lines 1-48

```python
   1 """Rendering helpers for CI logs and PR comments."""
   2 
!  3 from __future__ import annotations
   4 
!  5 from typing import List, Optional, Sequence, Tuple
   6 
!  7 from .diff_parser import DiffCoverageSummary
   8 
   9 
! 10 def render_text_table(rows: Sequence[Tuple[str, str]], title: Optional[str] = None) -> str:
  11     """Render a small, fixed-width table suitable for CI logs."""
  12 
! 13     if not rows:
! 14         return "" if title is None else f"{title}\n"
  15 
! 16     left_width = max(len(k) for k, _ in rows)
! 17     right_width = max(len(v) for _, v in rows)
  18 
! 19     lines: List[str] = []
! 20     if title:
! 21         lines.append(title)
  22 
! 23     border = f"+-{'-' * left_width}-+-{'-' * right_width}-+"
! 24     lines.append(border)
! 25     for k, v in rows:
! 26         lines.append(f"| {k.ljust(left_width)} | {v.ljust(right_width)} |")
! 27     lines.append(border)
! 28     return "\n".join(lines) + "\n"
  29 
  30 
! 31 def render_markdown_comment(summary: DiffCoverageSummary, header: str = "Diff coverage") -> str:
  32     """Build a friendly markdown comment from a DiffCoverageSummary."""
  33 
! 34     parts: List[str] = [f"## {header}"]
  35 
! 36     if summary.coverage_percent is not None:
! 37         parts.append(f"**Coverage:** {summary.coverage_percent:.2f}%")
  38 
! 39     if summary.missing_lines is not None and summary.measured_lines is not None:
! 40         parts.append(f"**Uncovered lines:** {summary.missing_lines} / {summary.measured_lines}")
  41 
! 42     parts.append("\n<details><summary>Raw diff-cover output</summary>\n")
! 43     parts.append("\n```\n" + summary.raw.strip() + "\n```\n")
! 44     parts.append("</details>")
  45 
! 46     return "\n\n".join(parts).strip() + "\n"
  47 
```


---



## main&#46;py

Lines 17-25

```python
  17 
  18     Returns:
  19         a ** b
  20     """
! 21     return a ** b
  22 
  23 
  24 def multiply_numbers(a, b):
  25     """Multiply two numbers together.
```


---


