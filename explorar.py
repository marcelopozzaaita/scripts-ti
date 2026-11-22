from pathlib import Path

pasta = Path.home() / "teste_organizar"

for item in pasta.iterdir():
	print(item.name, "|", item.stem, "|", repr(item.suffix.lower().lstrip(".")), "|", item.is_file())


