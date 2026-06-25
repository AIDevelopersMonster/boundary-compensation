# BC-Origin IV software patch v0.1.1

This software layer implements the stricter BC-Origin IV convention:

- lifted phase flow, not physical time;
- structural overlap, not pairwise fitted coupling;
- closure-lift reindexing, not a physical Thouless-pump claim;
- interpolated horizon-event estimates through `lambda_min(D)=0` and `det(D2)=0` diagnostics.

Run from the package root:

```bash
python origin_iv/software/generate_bc_origin_iv_figures.py --out origin_iv/figures
```

Generated figures include avoided crossings, horizon-event curves/maps, gap protection,
lifted phase reindexing and multi-shadow branch counts.
