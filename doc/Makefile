# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -j auto
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
REPO_ROOT     = ../

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@REPO_ROOT=`realpath $(REPO_ROOT)` $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# customized to build the pdf rather than using latexpdf due to various issues
pdf:
	@REPO_ROOT=`realpath $(REPO_ROOT)` $(SPHINXBUILD) -M latex "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	cd $(BUILDDIR)/latex && latexmk -r latexmkrc -pdf *.tex -interaction=nonstopmode || true
	(test -f $(BUILDDIR)/latex/ansys-acp-core.pdf && echo pdf exists) || exit 1

# customized clean due to examples gallery
clean:
	rm -rf $(BUILDDIR)
	rm -rf $(SOURCEDIR)/examples/images
	rm -rf $(SOURCEDIR)/examples/modeling_features
	rm -rf $(SOURCEDIR)/examples/use_cases
	rm -rf $(SOURCEDIR)/examples/workflows
	rm -rf $(SOURCEDIR)/examples/sg_execution_times.rst
	find . -type d -name "_autosummary" -exec rm -rf {} +
