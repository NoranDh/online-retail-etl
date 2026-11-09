# Query plans

Generated 2026-11-09 11:25:49 by `scripts/performance.py`.

Each query is run twice: with index scans allowed, and with index scans turned off. The second run shows what the planner does without the indexes.

## Revenue by product category

With indexes:
```
Finalize GroupAggregate  (cost=12592.37..12654.38 rows=200 width=64) (actual time=288.024..313.308 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=7058
  ->  Gather Merge  (cost=12592.37..12648.28 rows=480 width=64) (actual time=288.005..313.287 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=7058
        ->  Sort  (cost=11592.35..11592.85 rows=200 width=64) (actual time=216.370..216.376 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=7058
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=11582.20..11584.70 rows=200 width=64) (actual time=216.317..216.326 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=7042
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=89.45..11025.28 rows=111385 width=48) (actual time=2.186..142.938 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=7042
                          ->  Parallel Append  (cost=0.00..10642.91 rows=111384 width=20) (actual time=0.021..76.838 rows=174959.33 loops=3)
                                Buffers: shared hit=6931
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1566.69 rows=24434 width=20) (actual time=0.018..31.746 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1078
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1123.36 rows=17568 width=20) (actual time=0.015..19.105 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=772
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..935.36 rows=14618 width=20) (actual time=0.011..18.281 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=643
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..790.35 rows=12268 width=20) (actual time=0.017..16.140 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=545
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..736.88 rows=11494 width=20) (actual time=0.014..12.406 rows=38395.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 684
                                      Buffers: shared hit=507
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..688.93 rows=10746 width=20) (actual time=0.016..4.040 rows=11972.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 207
                                      Buffers: shared hit=474
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..686.26 rows=10713 width=20) (actual time=0.007..10.411 rows=35716.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 709
                                      Buffers: shared hit=472
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..682.90 rows=10645 width=20) (actual time=0.006..10.998 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=470
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..657.47 rows=10224 width=20) (actual time=0.006..10.343 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=453
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..656.48 rows=10274 width=20) (actual time=0.008..12.196 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=451
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..555.18 rows=8659 width=20) (actual time=0.007..8.957 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=382
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..516.89 rows=8045 width=20) (actual time=0.008..9.168 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=356
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..476.19 rows=7409 width=20) (actual time=0.019..8.354 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=328
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.06 rows=153 width=20) (actual time=0.003..0.003 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=60.31..60.31 rows=2331 width=36) (actual time=2.142..2.143 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=111
                                ->  Seq Scan on dim_product p  (cost=0.00..60.31 rows=2331 width=36) (actual time=0.370..1.219 rows=3828.00 loops=3)
                                      Buffers: shared hit=111
Planning:
  Buffers: shared hit=144
Planning Time: 1.938 ms
Execution Time: 313.525 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=12592.37..12654.38 rows=200 width=64) (actual time=333.947..372.212 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=7058
  ->  Gather Merge  (cost=12592.37..12648.28 rows=480 width=64) (actual time=333.926..372.187 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=7058
        ->  Sort  (cost=11592.35..11592.85 rows=200 width=64) (actual time=280.205..280.212 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=7058
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=11582.20..11584.70 rows=200 width=64) (actual time=279.945..279.954 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=7042
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=89.45..11025.28 rows=111385 width=48) (actual time=2.294..184.643 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=7042
                          ->  Parallel Append  (cost=0.00..10642.91 rows=111384 width=20) (actual time=0.027..98.728 rows=174959.33 loops=3)
                                Buffers: shared hit=6931
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1566.69 rows=24434 width=20) (actual time=0.031..40.591 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1078
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1123.36 rows=17568 width=20) (actual time=0.016..28.706 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=772
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..935.36 rows=14618 width=20) (actual time=0.011..24.733 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=643
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..790.35 rows=12268 width=20) (actual time=0.024..22.772 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=545
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..736.88 rows=11494 width=20) (actual time=0.015..18.098 rows=38395.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 684
                                      Buffers: shared hit=507
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..688.93 rows=10746 width=20) (actual time=0.015..4.646 rows=11972.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 207
                                      Buffers: shared hit=474
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..686.26 rows=10713 width=20) (actual time=0.010..7.785 rows=17858.00 loops=2)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 354
                                      Buffers: shared hit=472
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..682.90 rows=10645 width=20) (actual time=0.007..14.687 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=470
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..657.47 rows=10224 width=20) (actual time=0.010..13.247 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=453
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..656.48 rows=10274 width=20) (actual time=0.008..12.984 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=451
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..555.18 rows=8659 width=20) (actual time=0.010..12.188 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=382
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..516.89 rows=8045 width=20) (actual time=0.007..9.014 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=356
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..476.19 rows=7409 width=20) (actual time=0.022..9.201 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=328
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.06 rows=153 width=20) (actual time=0.004..0.004 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=60.31..60.31 rows=2331 width=36) (actual time=2.243..2.244 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=111
                                ->  Seq Scan on dim_product p  (cost=0.00..60.31 rows=2331 width=36) (actual time=0.294..1.234 rows=3828.00 loops=3)
                                      Buffers: shared hit=111
Planning:
  Buffers: shared hit=4
Planning Time: 1.078 ms
Execution Time: 372.400 ms
```

## Top 10 customers by revenue

With indexes:
```
Limit  (cost=15397.55..15397.58 rows=10 width=36) (actual time=271.465..287.266 rows=10.00 loops=1)
  Buffers: shared hit=6994
  ->  Sort  (cost=15397.55..15408.85 rows=4520 width=36) (actual time=271.462..287.261 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6994
        ->  Finalize HashAggregate  (cost=15243.38..15299.88 rows=4520 width=36) (actual time=268.032..286.052 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6991
              ->  Gather  (cost=14020.72..15162.02 rows=10848 width=36) (actual time=255.016..274.475 rows=8132.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6991
                    ->  Partial HashAggregate  (cost=13020.72..13077.22 rows=4520 width=36) (actual time=203.823..205.581 rows=2710.67 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6991
                          Worker 0:  Batches: 1  Memory Usage: 1041kB
                          Worker 1:  Batches: 1  Memory Usage: 1297kB
                          ->  Hash Join  (cost=121.70..11906.87 rows=222770 width=20) (actual time=2.309..140.960 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6991
                                ->  Parallel Append  (cost=0.00..11199.85 rows=222771 width=20) (actual time=0.022..79.863 rows=178043.00 loops=3)
                                      Buffers: shared hit=6931
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1566.69 rows=48869 width=20) (actual time=0.018..31.040 rows=83077.00 loops=1)
                                            Buffers: shared hit=1078
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1123.36 rows=35136 width=20) (actual time=0.022..23.841 rows=59731.00 loops=1)
                                            Buffers: shared hit=772
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..935.36 rows=29236 width=20) (actual time=0.010..17.936 rows=49701.00 loops=1)
                                            Buffers: shared hit=643
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..790.35 rows=24535 width=20) (actual time=0.026..16.072 rows=41710.00 loops=1)
                                            Buffers: shared hit=545
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..736.88 rows=22988 width=20) (actual time=0.017..4.455 rows=13026.33 loops=3)
                                            Buffers: shared hit=507
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..688.93 rows=21493 width=20) (actual time=0.019..6.911 rows=18269.00 loops=2)
                                            Buffers: shared hit=474
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..686.26 rows=21426 width=20) (actual time=0.007..10.456 rows=36425.00 loops=1)
                                            Buffers: shared hit=472
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..682.90 rows=21290 width=20) (actual time=0.006..8.868 rows=36193.00 loops=1)
                                            Buffers: shared hit=470
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..657.47 rows=20447 width=20) (actual time=0.008..11.502 rows=34760.00 loops=1)
                                            Buffers: shared hit=453
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..656.48 rows=20548 width=20) (actual time=0.008..11.297 rows=34931.00 loops=1)
                                            Buffers: shared hit=451
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..555.18 rows=17318 width=20) (actual time=0.006..8.324 rows=29440.00 loops=1)
                                            Buffers: shared hit=382
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..516.89 rows=16089 width=20) (actual time=0.008..7.119 rows=27352.00 loops=1)
                                            Buffers: shared hit=356
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..476.19 rows=14819 width=20) (actual time=0.014..8.282 rows=25192.00 loops=1)
                                            Buffers: shared hit=328
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.06 rows=306 width=20) (actual time=0.004..0.004 rows=0.00 loops=1)
                                ->  Hash  (cost=65.20..65.20 rows=4520 width=8) (actual time=2.236..2.237 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..65.20 rows=4520 width=8) (actual time=0.284..1.156 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=84 read=1
Planning Time: 3.007 ms
Execution Time: 288.128 ms
```

Index scans turned off:
```
Limit  (cost=15397.55..15397.58 rows=10 width=36) (actual time=260.102..276.785 rows=10.00 loops=1)
  Buffers: shared hit=6991
  ->  Sort  (cost=15397.55..15408.85 rows=4520 width=36) (actual time=260.101..276.782 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6991
        ->  Finalize HashAggregate  (cost=15243.38..15299.88 rows=4520 width=36) (actual time=256.740..275.626 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6991
              ->  Gather  (cost=14020.72..15162.02 rows=10848 width=36) (actual time=244.300..265.860 rows=8138.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6991
                    ->  Partial HashAggregate  (cost=13020.72..13077.22 rows=4520 width=36) (actual time=192.955..194.843 rows=2712.67 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6991
                          Worker 0:  Batches: 1  Memory Usage: 1041kB
                          Worker 1:  Batches: 1  Memory Usage: 1297kB
                          ->  Hash Join  (cost=121.70..11906.87 rows=222770 width=20) (actual time=2.877..134.096 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6991
                                ->  Parallel Append  (cost=0.00..11199.85 rows=222771 width=20) (actual time=0.048..75.192 rows=178043.00 loops=3)
                                      Buffers: shared hit=6931
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1566.69 rows=48869 width=20) (actual time=0.026..29.395 rows=83077.00 loops=1)
                                            Buffers: shared hit=1078
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1123.36 rows=35136 width=20) (actual time=0.015..23.374 rows=59731.00 loops=1)
                                            Buffers: shared hit=772
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..935.36 rows=29236 width=20) (actual time=0.015..18.297 rows=49701.00 loops=1)
                                            Buffers: shared hit=643
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..790.35 rows=24535 width=20) (actual time=0.017..15.651 rows=41710.00 loops=1)
                                            Buffers: shared hit=545
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..736.88 rows=22988 width=20) (actual time=0.012..3.392 rows=13026.33 loops=3)
                                            Buffers: shared hit=507
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..688.93 rows=21493 width=20) (actual time=0.010..4.584 rows=18269.00 loops=2)
                                            Buffers: shared hit=474
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..686.26 rows=21426 width=20) (actual time=0.006..9.189 rows=36425.00 loops=1)
                                            Buffers: shared hit=472
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..682.90 rows=21290 width=20) (actual time=0.006..7.873 rows=36193.00 loops=1)
                                            Buffers: shared hit=470
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..657.47 rows=20447 width=20) (actual time=0.006..10.149 rows=34760.00 loops=1)
                                            Buffers: shared hit=453
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..656.48 rows=20548 width=20) (actual time=0.008..11.641 rows=34931.00 loops=1)
                                            Buffers: shared hit=451
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..555.18 rows=17318 width=20) (actual time=0.009..7.723 rows=29440.00 loops=1)
                                            Buffers: shared hit=382
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..516.89 rows=16089 width=20) (actual time=0.010..8.040 rows=27352.00 loops=1)
                                            Buffers: shared hit=356
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..476.19 rows=14819 width=20) (actual time=0.092..8.331 rows=25192.00 loops=1)
                                            Buffers: shared hit=328
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.06 rows=306 width=20) (actual time=0.003..0.004 rows=0.00 loops=1)
                                ->  Hash  (cost=65.20..65.20 rows=4520 width=8) (actual time=2.767..2.768 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..65.20 rows=4520 width=8) (actual time=0.334..1.398 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=4
Planning Time: 1.334 ms
Execution Time: 277.612 ms
```

## One month of sales (June 2011)

With indexes:
```
Aggregate  (cost=1018.83..1018.84 rows=1 width=32) (actual time=13.764..13.764 rows=1.00 loops=1)
  Buffers: shared hit=472
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1018.38 rows=182 width=16) (actual time=0.027..8.704 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=472
Planning:
  Buffers: shared hit=38
Planning Time: 0.300 ms
Execution Time: 13.794 ms
```

Index scans turned off:
```
Aggregate  (cost=1018.83..1018.84 rows=1 width=32) (actual time=13.852..13.853 rows=1.00 loops=1)
  Buffers: shared hit=472
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1018.38 rows=182 width=16) (actual time=0.019..8.792 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=472
Planning Time: 0.179 ms
Execution Time: 13.880 ms
```

## One customer's orders (point lookup)

With indexes:
```
Aggregate  (cost=5289.56..5289.57 rows=1 width=8) (actual time=2.381..2.389 rows=1.00 loops=1)
  Buffers: shared hit=6 read=26
  ->  Append  (cost=5.91..5282.88 rows=2675 width=0) (actual time=0.642..2.379 rows=40.00 loops=1)
        Buffers: shared hit=6 read=26
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..412.47 rows=209 width=0) (actual time=0.514..0.515 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_customer_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.148..0.148 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..343.16 rows=174 width=0) (actual time=0.126..0.128 rows=12.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=1
              Buffers: shared hit=1 read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_customer_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.107..0.108 rows=12.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..270.98 rows=137 width=0) (actual time=0.488..0.489 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_customer_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.470..0.470 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..356.63 rows=181 width=0) (actual time=0.122..0.123 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_customer_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.111..0.111 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..291.32 rows=147 width=0) (actual time=0.442..0.442 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_04_customer_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.429..0.429 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..360.66 rows=183 width=0) (actual time=0.092..0.093 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_customer_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.082..0.082 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..358.65 rows=182 width=0) (actual time=0.093..0.099 rows=26.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=2
              Buffers: shared hit=2 read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_customer_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.077..0.077 rows=26.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..384.42 rows=195 width=0) (actual time=0.080..0.081 rows=2.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=1
              Buffers: shared hit=1 read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_customer_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.070..0.070 rows=2.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..344.06 rows=175 width=0) (actual time=0.078..0.078 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_customer_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.067..0.067 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..487.87 rows=249 width=0) (actual time=0.074..0.075 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_customer_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.064..0.064 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..584.98 rows=299 width=0) (actual time=0.078..0.078 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_customer_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.067..0.067 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..812.97 rows=415 width=0) (actual time=0.076..0.077 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_customer_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.066..0.066 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..250.06 rows=126 width=0) (actual time=0.077..0.077 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_customer_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.067..0.068 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.012..0.012 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_customer_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=9 read=1
Planning Time: 0.919 ms
Execution Time: 2.668 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11880.81..11880.82 rows=1 width=8) (actual time=163.657..191.690 rows=1.00 loops=1)
  Buffers: shared hit=6931
  ->  Gather  (cost=11880.59..11880.80 rows=2 width=8) (actual time=89.619..191.676 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6931
        ->  Partial Aggregate  (cost=10880.59..10880.60 rows=1 width=8) (actual time=32.743..32.746 rows=1.00 loops=3)
              Buffers: shared hit=6931
              ->  Parallel Append  (cost=0.00..10877.81 rows=1113 width=0) (actual time=11.495..32.733 rows=13.33 loops=3)
                    Buffers: shared hit=6931
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=244 width=0) (actual time=8.928..8.928 rows=0.00 loops=2)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 41538
                          Buffers: shared hit=1078
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=176 width=0) (actual time=12.378..12.378 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=772
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=146 width=0) (actual time=12.260..12.260 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=643
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=123 width=0) (actual time=6.970..6.970 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=545
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=115 width=0) (actual time=6.866..6.899 rows=2.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 39077
                          Buffers: shared hit=507
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=108 width=0) (actual time=4.939..4.939 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=474
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=107 width=0) (actual time=0.008..5.066 rows=26.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36399
                          Buffers: shared hit=472
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=106 width=0) (actual time=6.643..6.644 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=470
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=102 width=0) (actual time=5.951..6.596 rows=12.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34748
                          Buffers: shared hit=453
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=103 width=0) (actual time=6.948..6.948 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=451
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=86 width=0) (actual time=4.823..4.823 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 29440
                          Buffers: shared hit=382
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=81 width=0) (actual time=3.873..3.874 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=356
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.24 rows=74 width=0) (actual time=2.887..2.887 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=328
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=2 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 0.777 ms
Execution Time: 191.842 ms
```

## One product's sales (point lookup)

With indexes:
```
Aggregate  (cost=5289.56..5289.57 rows=1 width=8) (actual time=1.301..1.308 rows=1.00 loops=1)
  Buffers: shared hit=73 read=26
  ->  Append  (cost=5.91..5282.88 rows=2675 width=0) (actual time=0.192..1.296 rows=71.00 loops=1)
        Buffers: shared hit=73 read=26
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..412.47 rows=209 width=0) (actual time=0.192..0.228 rows=30.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=30
              Buffers: shared hit=30 read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_product_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.166..0.166 rows=30.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..343.16 rows=174 width=0) (actual time=0.116..0.141 rows=21.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=21
              Buffers: shared hit=21 read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_product_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.097..0.097 rows=21.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..270.98 rows=137 width=0) (actual time=0.093..0.100 rows=7.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=7
              Buffers: shared hit=7 read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_product_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.075..0.075 rows=7.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..356.63 rows=181 width=0) (actual time=0.087..0.096 rows=8.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=8
              Buffers: shared hit=8 read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_product_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.074..0.074 rows=8.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..291.32 rows=147 width=0) (actual time=0.088..0.093 rows=5.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=5
              Buffers: shared hit=5 read=2
              ->  Bitmap Index Scan on fact_sales_2011_04_product_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.074..0.074 rows=5.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..360.66 rows=183 width=0) (actual time=0.080..0.081 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_product_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.069..0.070 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..358.65 rows=182 width=0) (actual time=0.083..0.083 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_product_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.064..0.064 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..384.42 rows=195 width=0) (actual time=0.075..0.076 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_product_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.066..0.066 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..344.06 rows=175 width=0) (actual time=0.074..0.074 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_product_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.063..0.063 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..487.87 rows=249 width=0) (actual time=0.071..0.072 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_product_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.062..0.062 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..584.98 rows=299 width=0) (actual time=0.073..0.073 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_product_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.064..0.064 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..812.97 rows=415 width=0) (actual time=0.080..0.081 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_product_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.070..0.070 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..250.06 rows=126 width=0) (actual time=0.073..0.073 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_product_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.063..0.063 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.010..0.010 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_product_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.004..0.004 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=4
Planning Time: 0.791 ms
Execution Time: 1.577 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11880.81..11880.82 rows=1 width=8) (actual time=90.235..119.209 rows=1.00 loops=1)
  Buffers: shared hit=6931
  ->  Gather  (cost=11880.59..11880.80 rows=2 width=8) (actual time=89.749..119.198 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6931
        ->  Partial Aggregate  (cost=10880.59..10880.60 rows=1 width=8) (actual time=32.592..32.596 rows=1.00 loops=3)
              Buffers: shared hit=6931
              ->  Parallel Append  (cost=0.00..10877.81 rows=1113 width=0) (actual time=4.887..32.570 rows=23.67 loops=3)
                    Buffers: shared hit=6931
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=244 width=0) (actual time=4.500..4.500 rows=0.00 loops=3)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1078
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=176 width=0) (actual time=8.778..8.778 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=772
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=146 width=0) (actual time=6.117..6.117 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=643
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=123 width=0) (actual time=0.046..8.146 rows=30.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 41680
                          Buffers: shared hit=545
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=115 width=0) (actual time=8.209..8.210 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 39079
                          Buffers: shared hit=507
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=108 width=0) (actual time=7.816..7.816 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=474
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=107 width=0) (actual time=7.699..7.699 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36425
                          Buffers: shared hit=472
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=106 width=0) (actual time=0.209..7.400 rows=8.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36185
                          Buffers: shared hit=470
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=102 width=0) (actual time=0.530..7.372 rows=21.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 34739
                          Buffers: shared hit=453
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=103 width=0) (actual time=6.998..6.998 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=451
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=86 width=0) (actual time=0.082..5.836 rows=5.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 29435
                          Buffers: shared hit=382
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=81 width=0) (actual time=0.760..5.283 rows=7.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 27345
                          Buffers: shared hit=356
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.24 rows=74 width=0) (actual time=4.444..4.444 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=328
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=2 width=0) (actual time=0.004..0.004 rows=0.00 loops=1)
                          Filter: (product_key = 1)
Planning:
  Buffers: shared hit=4
Planning Time: 0.763 ms
Execution Time: 119.374 ms
```

## One day's sales (point lookup)

With indexes:
```
Aggregate  (cost=5289.56..5289.57 rows=1 width=8) (actual time=2.992..3.001 rows=1.00 loops=1)
  Buffers: shared hit=19 read=27
  ->  Append  (cost=5.91..5282.88 rows=2675 width=0) (actual time=1.995..2.923 rows=1073.00 loops=1)
        Buffers: shared hit=19 read=27
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..412.47 rows=209 width=0) (actual time=0.526..0.527 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_date_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.498..0.498 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..343.16 rows=174 width=0) (actual time=0.363..0.363 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_date_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.325..0.325 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..270.98 rows=137 width=0) (actual time=0.484..0.485 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_date_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.459..0.459 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..356.63 rows=181 width=0) (actual time=0.413..0.414 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_date_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.390..0.390 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..291.32 rows=147 width=0) (actual time=0.204..0.343 rows=1073.00 loops=1)
              Recheck Cond: (date_key = 100)
              Heap Blocks: exact=17
              Buffers: shared hit=17 read=3
              ->  Bitmap Index Scan on fact_sales_2011_04_date_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.180..0.180 rows=1073.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=3
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..360.66 rows=183 width=0) (actual time=0.087..0.088 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_date_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.076..0.076 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..358.65 rows=182 width=0) (actual time=0.098..0.098 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_date_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.075..0.075 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..384.42 rows=195 width=0) (actual time=0.082..0.082 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_date_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.070..0.070 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..344.06 rows=175 width=0) (actual time=0.082..0.082 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_date_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.070..0.070 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..487.87 rows=249 width=0) (actual time=0.096..0.096 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_date_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.086..0.086 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..584.98 rows=299 width=0) (actual time=0.078..0.078 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_date_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.068..0.068 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..812.97 rows=415 width=0) (actual time=0.078..0.078 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_date_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.068..0.068 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..250.06 rows=126 width=0) (actual time=0.079..0.079 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_date_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.069..0.069 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.011..0.011 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_date_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=30
Planning Time: 0.905 ms
Execution Time: 3.268 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11880.81..11880.82 rows=1 width=8) (actual time=73.582..97.820 rows=1.00 loops=1)
  Buffers: shared hit=6931
  ->  Gather  (cost=11880.59..11880.80 rows=2 width=8) (actual time=73.198..97.812 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6931
        ->  Partial Aggregate  (cost=10880.59..10880.60 rows=1 width=8) (actual time=25.136..25.139 rows=1.00 loops=3)
              Buffers: shared hit=6931
              ->  Parallel Append  (cost=0.00..10877.81 rows=1113 width=0) (actual time=3.736..25.103 rows=357.67 loops=3)
                    Buffers: shared hit=6931
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=244 width=0) (actual time=3.724..3.724 rows=0.00 loops=3)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1078
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=176 width=0) (actual time=7.404..7.404 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=772
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=146 width=0) (actual time=5.525..5.525 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=643
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=123 width=0) (actual time=4.521..4.521 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=545
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=115 width=0) (actual time=5.143..5.143 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 39079
                          Buffers: shared hit=507
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=108 width=0) (actual time=4.069..4.069 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=474
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=107 width=0) (actual time=4.324..4.324 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36425
                          Buffers: shared hit=472
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=106 width=0) (actual time=6.648..6.648 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=470
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=102 width=0) (actual time=6.991..6.991 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 34760
                          Buffers: shared hit=453
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=103 width=0) (actual time=6.670..6.670 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=451
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=86 width=0) (actual time=0.007..5.196 rows=1073.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 28367
                          Buffers: shared hit=382
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=81 width=0) (actual time=4.148..4.149 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=356
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.24 rows=74 width=0) (actual time=3.349..3.349 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=328
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=2 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                          Filter: (date_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 0.893 ms
Execution Time: 97.964 ms
```

## Monthly revenue by country, from the fact table

With indexes:
```
Finalize GroupAggregate  (cost=25574.05..40127.28 rows=39996 width=68) (actual time=386.243..502.152 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Buffers: shared hit=7025, temp read=2263 written=2270
  ->  Gather Merge  (cost=25574.05..38467.45 rows=95990 width=68) (actual time=386.215..501.667 rows=336.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=7025, temp read=2263 written=2270
        ->  Partial GroupAggregate  (cost=24574.03..26387.80 rows=39996 width=68) (actual time=214.127..298.106 rows=112.00 loops=3)
              Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
              Buffers: shared hit=7025, temp read=2263 written=2270
              ->  Sort  (cost=24574.03..24852.49 rows=111384 width=52) (actual time=214.054..246.734 rows=174959.33 loops=3)
                    Sort Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
                    Sort Method: external merge  Disk: 8088kB
                    Buffers: shared hit=7025, temp read=2263 written=2270
                    Worker 0:  Sort Method: external merge  Disk: 5992kB
                    Worker 1:  Sort Method: external merge  Disk: 4024kB
                    ->  Parallel Append  (cost=0.00..11429.16 rows=111384 width=52) (actual time=0.032..120.679 rows=174959.33 loops=3)
                          Buffers: shared hit=6931
                          ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=24434 width=52) (actual time=0.033..50.517 rows=82004.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1073
                                Buffers: shared hit=1078
                          ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=17568 width=52) (actual time=0.013..34.650 rows=58537.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1194
                                Buffers: shared hit=772
                          ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=14618 width=52) (actual time=0.023..26.523 rows=48900.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 801
                                Buffers: shared hit=643
                          ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=12268 width=52) (actual time=0.015..24.642 rows=40991.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 719
                                Buffers: shared hit=545
                          ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=11494 width=52) (actual time=0.012..7.282 rows=12798.33 loops=3)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 228
                                Buffers: shared hit=507
                          ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=10746 width=52) (actual time=0.012..8.498 rows=17958.50 loops=2)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 310
                                Buffers: shared hit=474
                          ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=10713 width=52) (actual time=0.009..22.781 rows=35716.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 709
                                Buffers: shared hit=472
                          ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=10645 width=52) (actual time=0.005..19.236 rows=35497.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 696
                                Buffers: shared hit=470
                          ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=10224 width=52) (actual time=0.009..19.142 rows=34060.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 700
                                Buffers: shared hit=453
                          ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=10274 width=52) (actual time=0.008..21.530 rows=34264.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 667
                                Buffers: shared hit=451
                          ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=8659 width=52) (actual time=0.010..16.563 rows=28882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 558
                                Buffers: shared hit=382
                          ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=8045 width=52) (actual time=0.010..18.852 rows=26882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 470
                                Buffers: shared hit=356
                          ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.23 rows=7409 width=52) (actual time=0.029..16.917 rows=24833.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 359
                                Buffers: shared hit=328
                          ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=153 width=52) (actual time=0.003..0.003 rows=0.00 loops=1)
                                Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 0.863 ms
Execution Time: 504.663 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=25574.05..40127.28 rows=39996 width=68) (actual time=370.111..615.233 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Buffers: shared hit=7025, temp read=2261 written=2268
  ->  Gather Merge  (cost=25574.05..38467.45 rows=95990 width=68) (actual time=370.084..614.260 rows=321.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=7025, temp read=2261 written=2268
        ->  Partial GroupAggregate  (cost=24574.03..26387.80 rows=39996 width=68) (actual time=247.320..378.433 rows=107.00 loops=3)
              Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
              Buffers: shared hit=7025, temp read=2261 written=2268
              ->  Sort  (cost=24574.03..24852.49 rows=111384 width=52) (actual time=247.175..296.424 rows=174959.33 loops=3)
                    Sort Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
                    Sort Method: external merge  Disk: 7832kB
                    Buffers: shared hit=7025, temp read=2261 written=2268
                    Worker 0:  Sort Method: external merge  Disk: 5032kB
                    Worker 1:  Sort Method: external merge  Disk: 5224kB
                    ->  Parallel Append  (cost=0.00..11429.16 rows=111384 width=52) (actual time=0.027..139.946 rows=174959.33 loops=3)
                          Buffers: shared hit=6931
                          ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=24434 width=52) (actual time=0.022..62.698 rows=82004.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1073
                                Buffers: shared hit=1078
                          ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=17568 width=52) (actual time=0.023..42.454 rows=58537.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1194
                                Buffers: shared hit=772
                          ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=14618 width=52) (actual time=0.011..38.797 rows=48900.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 801
                                Buffers: shared hit=643
                          ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=12268 width=52) (actual time=0.018..25.895 rows=40991.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 719
                                Buffers: shared hit=545
                          ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=11494 width=52) (actual time=0.014..22.239 rows=38395.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 684
                                Buffers: shared hit=507
                          ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=10746 width=52) (actual time=0.016..9.462 rows=11972.33 loops=3)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 207
                                Buffers: shared hit=474
                          ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=10713 width=52) (actual time=0.008..19.285 rows=35716.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 709
                                Buffers: shared hit=472
                          ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=10645 width=52) (actual time=0.010..16.995 rows=35497.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 696
                                Buffers: shared hit=470
                          ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=10224 width=52) (actual time=0.009..22.030 rows=34060.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 700
                                Buffers: shared hit=453
                          ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=10274 width=52) (actual time=0.009..28.404 rows=34264.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 667
                                Buffers: shared hit=451
                          ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=8659 width=52) (actual time=0.010..21.790 rows=28882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 558
                                Buffers: shared hit=382
                          ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=8045 width=52) (actual time=0.008..19.795 rows=26882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 470
                                Buffers: shared hit=356
                          ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.23 rows=7409 width=52) (actual time=0.018..14.264 rows=24833.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 359
                                Buffers: shared hit=328
                          ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=153 width=52) (actual time=0.011..0.011 rows=0.00 loops=1)
                                Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 0.796 ms
Execution Time: 619.400 ms
```

## Monthly revenue by country, from the materialized view

With indexes:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.031..0.067 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning:
  Buffers: shared hit=8 read=1
Planning Time: 0.966 ms
Execution Time: 0.087 ms
```

Index scans turned off:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.022..0.058 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning Time: 0.089 ms
Execution Time: 0.073 ms
```
