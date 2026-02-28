#!/bin/bash
# Validate Prometheus configuration and rules.
# Requires: promtool (comes with Prometheus)
set -euo pipefail

CONFIG_FILE="${1:-prometheus.yml}"
RULES_DIR="${2:-rules}"

echo "=== Prometheus Configuration Validator ==="

# Validate main config
echo "\n[1/2] Validating configuration: $CONFIG_FILE"
if promtool check config "$CONFIG_FILE"; then
    echo "  Configuration is valid."
else
    echo "  ERROR: Configuration validation failed!"
    exit 1
fi

# Validate rules
echo "\n[2/2] Validating rules in: $RULES_DIR/"
ERRORS=0
for rule_file in "$RULES_DIR"/*.yml; do
    if [ -f "$rule_file" ]; then
        if promtool check rules "$rule_file"; then
            echo "  $rule_file: OK"
        else
            echo "  $rule_file: FAILED"
            ERRORS=$((ERRORS + 1))
        fi
    fi
done

if [ $ERRORS -gt 0 ]; then
    echo "\nERROR: $ERRORS rule file(s) failed validation."
    exit 1
fi

echo "\n=== All validations passed ==="
