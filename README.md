# Puducherry RTI Analysis

Research scripts used to turn Puducherry electricity RTI responses into structured evidence and readable reports. The wider local workspace also contains school-education analysis; this repository publishes the selected electricity-processing scripts only.

## Contents and inputs

`tmp/reconciliation/` contains evidence extraction and summary generation scripts. `tmp/build_site.py` and `tmp/simplify_site.py` support an accompanying evidence site. `tmp/lead_spending.py` analyses selected spending material.

Source replies, personal correspondence, extracted records, images, and generated documents are excluded. Supply your own lawfully obtained and redacted inputs in `inputs/` and the expected extraction folders. Scripts retain the filenames and workflow assumptions of the original study; this is a research snapshot rather than a general-purpose parser.

## Reproduction

Python 3 is required. Individual scripts identify their third-party imports; install those dependencies in an isolated environment after reviewing them. Do not run the full workflow without the required source PDFs and intermediate artifacts. File paths are checkout-relative rather than tied to the original machine.

## Status

Research and report-generation tools. Findings require checking the underlying source pages and reconciliation notes. No original correspondence or private case material is published here.
