intended error
plot-%.png: %.dat plot.py
	./plot.py -i $*.dat -o $@
	Hello
paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex


