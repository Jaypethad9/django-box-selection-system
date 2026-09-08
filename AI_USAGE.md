# AI Usage

## 1. AI Tool Used

ChatGPT was used as an AI assistance tool during development of this
assignment.

The AI was used primarily for learning Django concepts, understanding
the assignment requirements, writing and reviewing code, debugging
errors, and designing automated tests.

---

## 2. How AI Was Used

AI assistance was used for the following development activities:

- Understanding the assignment requirements.
- Understanding Django project and app structure.
- Creating Django database models.
- Understanding Django migrations.
- Configuring Django Admin.
- Designing the box-selection business logic.
- Creating automated test cases.
- Creating the API endpoint.
- Debugging the CSRF error encountered while testing the API.
- Debugging a Python indentation error in the test file.
- Understanding test results.
- Preparing project documentation.

The generated code was reviewed and tested before being considered
part of the project.

---

## 3. Prompts Used

The following prompts were used during development:

### Prompt 1

"Hello Jay, [assignment email] ... Can you explain me what am I
supposed to do in this assignment I don't know at all"

Purpose:
To understand the assignment requirements and break the project
into manageable development phases.

### Prompt 2

"lets start with phase 2"

Purpose:
To begin setting up the Python, virtual environment, Django,
and development environment.

### Prompt 3

"next"

Purpose:
To continue through the development steps after completing each
stage.

### Prompt 4

"server is running"

Purpose:
To confirm that the Django development server was successfully
started and continue with the next setup stage.

### Prompt 5

"no issue"

Purpose:
To confirm that the Django system check completed successfully.

### Prompt 6

"I cannot see boxes"

Purpose:
To troubleshoot why the Product, Box, Order, and OrderItem models
were not visible in Django Admin.

### Prompt 7

"no issues"

Purpose:
To confirm that the Django models and application configuration
were working correctly.

### Prompt 8

"PS ... CSRF verification failed. Request aborted."

Purpose:
To troubleshoot the CSRF error encountered when testing the POST
API endpoint from PowerShell.

### Prompt 9

"PS ... StatusCode : 200 ... Medium Box"

Purpose:
To confirm that the API request was successful and that the box
recommendation logic returned the expected result.

### Prompt 10

The user provided a Python test-file error screenshot showing an
indentation problem.

Purpose:
To troubleshoot the Python indentation error and correct the
automated test file.

---

## 4. AI Output Accepted

AI assistance was accepted for several implementation and learning
tasks after review.

Examples include:

- The basic Django project structure.
- Product, Box, Order, and OrderItem models.
- Django Admin registration.
- The box-selection service structure.
- Automated test structure.
- The recommendation API structure.
- Basic project documentation structure.

The implementation was not accepted solely because it was generated
by AI. The code was run and verified locally.

---

## 5. AI Output Rejected or Modified

AI-generated suggestions were reviewed and modified when necessary.

### Test case mismatch

An initial test named:

`test_box_rejected_when_weight_exceeds_limit`

did not completely match the scenario it was testing because the
test data also allowed a larger box to accept the product.

This was identified during review and the test was modified so that
it specifically tests the small box's weight limit.

### Python indentation problem

An indentation error occurred while adding additional API tests to
the test file.

Instead of continuing with the broken file, the test file was
rewritten with consistent indentation and then executed again.

### API testing

The first attempt to test the POST API using PowerShell resulted in
a Django CSRF verification error.

The API view was adjusted for the API-style endpoint and the request
was tested again successfully.

---

## 6. Mistakes / Problems Identified

### CSRF verification error

When the recommendation endpoint was first tested using a POST
request from PowerShell, Django returned:

`403 Forbidden - CSRF verification failed.`

This was investigated and the API endpoint was adjusted so that the
PowerShell API request could be tested.

The endpoint was then tested again and returned HTTP 200.

### Incorrect test scenario

One automated test initially had a mismatch between its name and
the actual data being tested.

The test was reviewed and corrected.

### Python indentation error

An indentation error occurred while adding API tests.

The test file was corrected and the complete test suite was executed
again.

---

## 7. Verification Steps

The implementation was verified using Django's system check:

```text
python manage.py check
System check identified no issues (0 silenced).
python manage.py test

Ran 11 tests in 0.034s

OK

The recommendation API was also manually tested using PowerShell:

Invoke-WebRequest -UseBasicParsing -Method POST http://127.0.0.1:8000/api/orders/1/recommend-box/