all: authors.tex pprint.pdf paper.pdf supplement.pdf rebuttal.pdf

paper.pdf: paper.tex authors.tex introduction.tex architecture.tex features.tex numerics.tex domain_specific.tex conclusion_and_future_work.tex acknowledgements.tex siamart0216_uppercase_fix.tex pprint.pdf pprint.tex printers.tex calculus.tex matrices.tex images/circuitplot-qft.pdf paper.bib
	pdflatex -shell-escape --halt-on-error paper.tex
	bibtex paper.aux
	pdflatex -shell-escape --halt-on-error paper.tex
	pdflatex -shell-escape --halt-on-error paper.tex

supplement.pdf: categories.tex comparison_with_mma.tex diophantine.tex examples.tex gamma.tex gruntz.tex live.tex logic.tex nsimplify.tex other_projects_that_use_sympy.tex polys.tex series.tex sets.tex simplification.tex solvers.tex stats.tex supplement.tex tensors.tex paper.bib images/integral_steps.png
	pdflatex -shell-escape --halt-on-error supplement.tex
	bibtex supplement
	pdflatex -shell-escape --halt-on-error supplement.tex
	pdflatex -shell-escape --halt-on-error supplement.tex

rebuttal.pdf: rebuttal.tex
	pdflatex -shell-escape --halt-on-error rebuttal.tex
	pdflatex -shell-escape --halt-on-error rebuttal.tex

authors.tex: authors/list_latex.py authors/authors.json
	cd authors; ./list_latex.py

pprint.pdf: pprint.tex
	xelatex --halt-on-error pprint.tex

.PHONY: test
test:
	python test-paper.py

.PHONY: clean
clean:
	(rm -rf *.ps *.log *.dvi *.aux *.*% *.lof *.lop *.lot *.toc *.idx *.ilg *.ind *.bbl *.blg *.cpt)
	(rm -rf authors.tex pprint.pdf paper.pdf supplement.pdf rebuttal.pdf)
