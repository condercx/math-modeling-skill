import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PRESET_COMPOSITION = "dsh-plugin/math-modeling-agent/agent.cordis.yml"

# dsh-persona renamed its required config key `text` -> `prefix` between host
# 0.1.2-rc.1 and 0.1.5-rc.1. The 0.1.5 schema is `prefix` required, with
# `suffix`/`complete`/`includeRuntimeContext` defaulted. A preset authored
# against the old key mounts with
# "invalid config: - $.prefix missing required value".
STALE_PERSONA_KEYS = ("text",)


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def persona_block(text: str) -> str:
    """Return the `persona` row's own text, up to the next top-level row."""
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == "- id: persona":
            start = index
            break
    if start is None:
        raise AssertionError(f"no `- id: persona` row in {PRESET_COMPOSITION}")

    block = []
    for line in lines[start + 1:]:
        if line.startswith("- ") or line.startswith("# "):
            break
        block.append(line)
    return "\n".join(block)


class DshPresetPersonaTests(unittest.TestCase):
    def test_preset_composition_exists(self):
        self.assertTrue((ROOT / PRESET_COMPOSITION).is_file(), PRESET_COMPOSITION)

    def test_persona_uses_current_prefix_key(self):
        block = persona_block(read(PRESET_COMPOSITION))
        self.assertIn("prefix:", block)

    def test_persona_does_not_use_renamed_text_key(self):
        block = persona_block(read(PRESET_COMPOSITION))
        for stale in STALE_PERSONA_KEYS:
            self.assertNotIn(
                f"\n    {stale}:",
                "\n" + block,
                f"persona config still uses the renamed `{stale}` key; "
                "dsh-persona 0.1.5 requires `prefix`",
            )


if __name__ == "__main__":
    unittest.main()
