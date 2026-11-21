# Execution log (record for the assignment)

## 1. Ingest and Check 1 (claims against sources)
| # | Problem found | Where | Decision |
|---|---|---|---|
| 1 | Paris Philharmonie date 2014 vs 2015 | S1, S5 vs S4 | Checked externally: 14 Jan 2015 |
| 2 | Copenhagen hall date 2006 vs 2009 | S4 vs S1 | Checked externally: 17 Jan 2009 |
| 3 | RT target ranges differ | S2, S7 | Shown together; depends on hall type |
| 4 | Fan-shaped example differs (Barbican, Heydar Aliyev, Tanglewood) | S4, S7, S10 | Use Barbican and Tanglewood |
| 5 | Horseshoe had only one source | S6 | Searched; added S10 |
| 6 | S5 is the chamber orchestra's site and looks copied from Wikipedia | S5 | Retired; replaced by official S8 |
| 7 | La Scala seat count ambiguous in the list | S1 | Left out |
| 8 | Name traps (two Heydar Aliyev buildings, Odeon software vs Odense hall) | S1, S7 | Left out |
| 9 | Terminology: vineyard, arena, surround | S4, S10 (and snippets) | Wiki uses "vineyard"; recorded in conflicts |
| 10 | Berlin capacity 2,440 vs 2,250 | S1, S4, S8 | Use 2,440 |
| 11 | Sabine dating differs; user's "1919" is the year Sabine died, not a publication year | S2, S10, S11 | Wording avoids a publication year |
| 12 | S7's table labels total support as "STlate" while its text says STtotal | S7 | Not used in the Wiki |
| 13 | S11 gives three different days for Sabine's death | S11 | Not used in the Wiki |

## 2. Automatic citation check
See tools/check_citations.py. It flags any claim line without a source ID and any source ID missing from sources.md.
