plot:
	@dot -Tpng -o model.png model.dot
	@dot -Tpdf -o model.pdf model.dot

clean:
	@rm model.dot model.png model.pdf