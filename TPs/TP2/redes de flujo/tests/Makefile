.PHONY: test clean

PYTHON := python3
SCRIPT := ../traslado.py
CASES_DIR := cases
TMP_OUTPUT := output.txt

test:
	@echo "Ejecutando pruebas de traslado..."
	@passed=0; \
	failed=0; \
	for case in $(shell find $(CASES_DIR) -maxdepth 1 -type d -name "case-*"); do \
		echo "-----------------------------------------"; \
		echo "Probando $$case"; \
		config=$$case/config.txt; \
		if [ ! -f "$$config" ]; then \
			echo "❌ Error: config.txt no encontrado"; \
			failed=$$((failed+1)); \
			continue; \
		fi; \
		read n s < "$$config"; \
		if [ -z "$$n" ] || [ -z "$$s" ]; then \
			echo "❌ Error: config.txt mal formado"; \
			failed=$$((failed+1)); \
			continue; \
		fi; \
		echo "Ejecutando: $(PYTHON) $(SCRIPT) $$n $$s $$case/ciudades.txt $$case/espias.txt"; \
		$(PYTHON) $(SCRIPT) $$n $$s $$case/ciudades.txt $$case/espias.txt > $(TMP_OUTPUT); \
		if cmp -s $(TMP_OUTPUT) $$case/esperado.txt; then \
			echo "✅ Test $$case pasó"; \
			passed=$$((passed+1)); \
		else \
			echo "❌ Test $$case falló"; \
			echo "Esperado:"; cat $$case/esperado.txt; \
			echo "Obtenido:"; cat $(TMP_OUTPUT); \
			failed=$$((failed+1)); \
		fi; \
		echo ""; \
	done; \
	rm -f $(TMP_OUTPUT); \
	echo "====================================="; \
	echo "✔ Pasaron: $$passed"; \
	echo "✘ Fallaron: $$failed"; \
	if [ $$failed -gt 0 ]; then exit 1; fi

clean:
	rm -f $(TMP_OUTPUT)
