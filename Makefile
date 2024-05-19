build: README.md
	pandoc \
		--data-dir ./pandoc/ \
		--filter panflute-pyscript.py \
		--metadata-file ./metadata.yaml \
		--template pyscript.html \
		-i README.md \
		-o docs/index.html

serve:
	env python -m http.server --directory build
