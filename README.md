# wktest

This is a sample to show that beginning wkhtmltopdf-0.12.5 on debian buster, 
the output pdf file has spaces replaced with tabs.
The demo uses grep to search for tabs in the html (should find none) and 
pdfminer.six to find tabs in the pdf (should find none with 12.4 and more than one with 12.5)

# To run the demo

1. cd to a subdir
2. docker build -t demo .
3. docker run -v $PWD/workdir:/workdir demo

With wk12.4 the foundthispdf should contain `[]` and foundthishtml should be empty.  
With wk12.5 the foundthispdf should contain something other than `[]` and foundthishtml should be empty.  

