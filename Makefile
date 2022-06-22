plot:
	@dot -Tpng -o model.png model.dot
	@dot -Tpdf -o model.pdf model.dot
	@dot -Tsvg -o model.svg model.dot

clean:
	@rm model.dot model.png model.pdf model.svg
