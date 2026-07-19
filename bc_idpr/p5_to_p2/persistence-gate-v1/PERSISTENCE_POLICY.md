# BC-IDPR P5 -> P2 Downstream-Necessity Persistence Gate

Status: ACTIVE

No scientific step beyond the current accepted node may be taken until every artifact required for completion of P5 or execution/audit of P2 is stored in both:

1. the canonical GitHub repository;
2. the project Google Drive archive.

An absent file is not by itself a dependency failure when all of the following hold:

- the accepted certificate fully records the object, frozen protocol, status, gates, numerical margins, provenance and claim boundary;
- downstream work does not read the absent file;
- the absent file is review-only, diagnostic, temporary, or reconstructible;
- its absence does not prevent repetition of a critical downstream calculation under the declared reconstruction route.

Temporary memmaps, slabs, large candidate matrices, symbol caches and runtime logs may be omitted when the canonical certificate and exact reconstruction scripts are retained.

Every future P5/P2 handoff must update `P5_P2_PERSISTENCE_MANIFEST.json` and pass two-storage parity before the obligation graph advances.
