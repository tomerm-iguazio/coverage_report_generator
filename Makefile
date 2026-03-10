# ── config ────────────────────────────────────────────────────────────────────
PYTHON      := .venv/bin/python
COV_FILE    := main.py
TEST_FILE   := tests/test_main.py
COV_DATA    := tests/coverage_reports/main.coverage
HTML_DIR    := tests/coverage_reports/htmlcov
HTML_REPORT := $(HTML_DIR)/main_py.html

# Default: one small test. Override with: make test-forked TEST=tests/test_main.py::TestAddNumbers
TEST        ?= $(TEST_FILE)::TestAddNumbers::test_add_positive_numbers

# ── targets ───────────────────────────────────────────────────────────────────
.PHONY: test-forked open help

## Run tests with --forked, coverage for main.py only, then open the HTML report
test-forked:
	mkdir -p tests/coverage_reports
	$(PYTHON) \
		-X faulthandler \
		-m coverage run --data-file="$(COV_DATA)" \
		-m pytest -v \
		--capture=no \
		--disable-warnings \
		--durations=100 \
		--forked \
		-rf \
		$(TEST)
	COVERAGE_FILE=$(COV_DATA) $(PYTHON) -m coverage html \
		--include=$(COV_FILE) \
		-d $(HTML_DIR)
	@echo "\n✅  HTML report ready → $(HTML_REPORT)"
	open $(HTML_REPORT)

test:
	mkdir -p tests/coverage_reports
	$(PYTHON) \
		-X faulthandler \
		-m coverage run --data-file="$(COV_DATA)" \
		-m pytest -v \
		--capture=no \
		--disable-warnings \
		--durations=100 \
		-rf \
		$(TEST)
	COVERAGE_FILE=$(COV_DATA) $(PYTHON) -m coverage html \
		--include=$(COV_FILE) \
		-d $(HTML_DIR)
	@echo "\n✅  HTML report ready → $(HTML_REPORT)"
	open $(HTML_REPORT)

## Just open the last generated report
open:
	open $(HTML_REPORT)

help:
	@echo "Usage:"
	@echo "  make test-forked                        Run default single test"
	@echo "  make test-forked TEST=tests/test_main.py::TestAddNumbers"
	@echo "  make test-forked TEST=tests/test_main.py  Run all tests"
	@echo "  make open                               Re-open the last HTML report"

