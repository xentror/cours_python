all: soundbox

soundbox:
	pandoc --pdf-engine=xelatex -H ../head.tex -V geometry:"top=2cm, bottom=1.5cm, left=2cm, right=2cm" --highlight-style ../pygments.theme SoundBox.md -o soundbox.pdf
