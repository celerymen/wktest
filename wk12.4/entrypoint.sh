#!/bin/bash

grep -P '\t' /workdir/bob.html > /workdir/foundthishtml
wkhtmltopdf --quiet /workdir/bob.html /workdir/bob.pdf
python pdfcheck.py /workdir/bob.pdf > /workdir/foundthispdf

