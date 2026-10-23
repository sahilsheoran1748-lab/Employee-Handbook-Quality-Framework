# Employee Handbook Quality Framework

## Project Overview

The Employee Handbook Quality Framework is a Python-based document
quality-assurance project that analyzes a Microsoft Word employee
handbook. It extracts document content, inspects heading structure,
checks selected policy-related keywords, records findings, and produces
structured validation reports for human review.

The project uses an existing handbook as its source document. It does
not automatically rewrite or approve employment policies.

## Objectives

- Extract readable paragraphs, heading styles, and tables from a DOCX file.
- Inspect heading numbering and repeated paragraph text.
- Check for configured HR policy topic keywords.
- Record items that require manual review.
- Export findings in JSON, CSV, and text formats.
- Run automated tests against key project outputs.

## Implemented Features

1. Word document content extraction.
2. Heading and table structure analysis.
3. Topic keyword presence checks.
4. Policy content validation checks.
5. Manual review register generation.
6. Reusable Python audit module.
7. Automated project tests.
8. Central project configuration.
9. JSON, CSV, and text report outputs.

## Current Source Document

The configured source file is:

`data/raw/source_handbook.docx`

The current audit run extracted 95 non-empty paragraphs, detected
42 headings and 4 tables, and found no repeated non-empty paragraph
texts. The automated heading numbering check passed.

These results describe the current source file and should be recalculated
if the source document changes.

## Project Structure

```text
Employee-Handbook-Quality-Framework/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   └── handbook_audit.py
├── tests/
├── outputs/
│   ├── documents/
│   ├── logs/
│   ├── reports/
│   └── validation/
├── docs/
├── project_config.json
├── README.md
└── requirements.txt
```

## Environment and Dependencies

- Python 3.10 or later recommended
- python-docx

Install the required library:

```bash
pip install -r requirements.txt
```

## Usage

1. Place the source handbook at `data/raw/source_handbook.docx`.
2. Run the extraction and validation workflow.
3. Inspect JSON and CSV findings in `outputs/validation/`.
4. Review readable reports in `outputs/reports/`.
5. Manually investigate every item marked `REVIEW`.
6. Run the automated tests after changes.

The notebook workflow currently runs in Google Colab. File paths and
instructions may need adjustment for a local environment.

## Quality and Governance Limitations

This project performs structural checks and configured keyword matching.
A keyword match does not prove that a policy is complete, correct,
implemented, or legally compliant. A missing keyword does not prove
that the relevant policy is absent.

Blank paragraphs may be intentional formatting. Automated findings
must be reviewed before making edits.

Organization-specific policy wording, disciplinary rules, employment
terms, and legal obligations require review by authorized HR and
qualified legal professionals. This project does not provide legal
certification.

## Current Verification

The current run reports:

- 6 automated tests passed
- 0 test failures
- 0 test errors
- 4 reusable-module verification checks passed

These are results from the recorded run, not a guarantee that all future
changes or environments will pass.

## License and Confidentiality

No license has been assigned by this project. Confirm ownership and
permission before publishing or redistributing the source handbook.
Remove confidential or personally identifiable information before
making repository contents public.
