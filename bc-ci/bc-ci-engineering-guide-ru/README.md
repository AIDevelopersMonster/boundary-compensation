# BC-CI Engineering Guide I - reference supplement v0.1.0 draft (RU)

Эта папка сопровождает русский вариант документа:

**Boundary Compensation - Compensated Islands Engineering Guide I: Пошаговый сертификационный пайплайн**

Supplement демонстрирует детерминированный конечномерный статус-возвращающий аудит. Он не реализует физическую динамику, физическую причинность, термодинамику или геометрию пространства-времени.

## Файлы

- `configs/toy_protocol_config.json` - минимальный объявленный protocol package.
- `bc_ci_audit.py` - reference Python script для toy protocol.
- `outputs/response_status.csv` - threshold/readout status в каждом диагностическом узле.
- `outputs/section_status.csv` - Pareto и epsilon-robust section audit.
- `outputs/edge_status.csv` - robust edge / reset / fragile edge statuses.
- `outputs/reachability_matrix.csv` - certified reachability relation under path budget.
- `outputs/distance_depth.csv` - minimum certified depth diagnostics.
- `outputs/distance_cost.csv` - additive audit cost diagnostics.
- `outputs/bottleneck_margin.csv` - best bottleneck margin diagnostics.
- `outputs/path_count_matrix.csv` - certified path counts under path budget.
- `outputs/certification_entropy.csv` - log path-count entropy where support is nonempty.
- `outputs/run_summary.json` - top-level status summary and claim-firewall flags.
- `figures/diagnostic_graph.svg` - graph view of certified and reset/fragile edges.
- `figures/status_tree.svg` - status-returning audit flow.

## Запуск

```bash
python3 bc_ci_audit.py --config configs/toy_protocol_config.json --out outputs --figures figures
```

## Claim firewall

Выходные статусы являются статусами аудита. Они не являются физическими статусами.

- `TRANSPORT_NONPHYSICAL`: parameter continuation is not physical propagation.
- `CAUSALITY_NONCLAIM`: certified reachability is not physical causality.
- `THERMODYNAMIC_ENTROPY_NONCLAIM`: certification entropy is not thermodynamic entropy.
- `METRIC_TENSOR_NONCLAIM`: certified distances are not spacetime metric tensors.

## Reproducibility contract

Корректный BC-CI run должен объявить thresholds and protocol choices до просмотра желаемого output. Подгонка thresholds, measures, weights или distance costs после наблюдения output должна маркироваться как tuning artifact.
