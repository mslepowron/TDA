.PHONY: test clean test_dq test_pd

PYTHON := python3
SCRIPT_DQ := ../puentes_dq.py
SCRIPT_PD := ../puentes_pd.py
CASES_DIR := cases
TMP_OUTPUT := .tmp_output.txt

# Encuentra todas las carpetas case-N existentes
TEST_CASES := $(shell find $(CASES_DIR) -type f -name barrios.txt | sed -E 's|.*/(case-[0-9]+).*|\1|' | sort -u)

define run_tests
	@echo "Ejecutando tests de $(1)..."
	@passed=0; \
	failed=0; \
	for case in $(TEST_CASES); do \
		case_path=$(CASES_DIR)/$$case; \
		echo "🔍 Test $$case:"; \
		$(PYTHON) $(2) $$case_path/barrios.txt $$case_path/propuestas.txt > $(TMP_OUTPUT); \
		head -n 1 $(TMP_OUTPUT) > .tmp_output_first_line.txt; \
		if diff -b -q .tmp_output_first_line.txt $$case_path/$(3) > /dev/null; then \
			echo "✅ Test $$case pasó"; \
			passed=$$((passed+1)); \
		else \
			echo "❌ Test $$case falló"; \
			echo "Esperado:"; cat $$case_path/$(3); \
			echo "Obtenido:"; cat .tmp_output_first_line.txt; \
			failed=$$((failed+1)); \
		fi; \
		echo ""; \
	done; \
	rm -f $(TMP_OUTPUT) .tmp_output_first_line.txt; \
	echo "Resumen:"; \
	echo "✔ Pasaron: $$passed"; \
	echo "✘ Fallaron: $$failed"; \
	if [ $$failed -eq 0 ]; then \
		echo "🎉 Todos los tests pasaron."; \
	else \
		exit 1; \
	fi
endef

test_dq:
	$(call run_tests,$(SCRIPT_DQ),$(SCRIPT_DQ),esperado-dq.txt)

test_pd:
	$(call run_tests,$(SCRIPT_PD),$(SCRIPT_PD),esperado-pd.txt)

test: test_dq test_pd

clean:
	rm -f $(TMP_OUTPUT) .tmp_output_first_line.txt
