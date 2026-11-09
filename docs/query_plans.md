# Query plans

Generated 2026-11-09 11:10:56 by `scripts/performance.py`.

Each query is run twice: with index scans allowed, and with index scans turned off. The second run shows what the planner does without the indexes.

## Revenue by product category

With indexes:
```
Finalize GroupAggregate  (cost=12592.37..12654.38 rows=200 width=64) (actual time=314.542..344.262 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=7058
  ->  Gather Merge  (cost=12592.37..12648.28 rows=480 width=64) (actual time=314.515..344.232 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=7058
        ->  Sort  (cost=11592.35..11592.85 rows=200 width=64) (actual time=256.777..256.784 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=7058
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=11582.20..11584.70 rows=200 width=64) (actual time=256.708..256.718 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=7042
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=89.45..11025.28 rows=111385 width=48) (actual time=1.830..168.869 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=7042
                          ->  Parallel Append  (cost=0.00..10642.91 rows=111384 width=20) (actual time=0.022..89.844 rows=174959.33 loops=3)
                                Buffers: shared hit=6931
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1566.69 rows=24434 width=20) (actual time=0.018..41.558 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1078
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1123.36 rows=17568 width=20) (actual time=0.023..32.415 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=772
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..935.36 rows=14618 width=20) (actual time=0.017..19.348 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=643
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..790.35 rows=12268 width=20) (actual time=0.016..16.029 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=545
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..736.88 rows=11494 width=20) (actual time=0.014..5.041 rows=12798.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 228
                                      Buffers: shared hit=507
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..688.93 rows=10746 width=20) (actual time=0.014..7.255 rows=17958.50 loops=2)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 310
                                      Buffers: shared hit=474
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..686.26 rows=10713 width=20) (actual time=0.008..10.147 rows=35716.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 709
                                      Buffers: shared hit=472
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..682.90 rows=10645 width=20) (actual time=0.006..9.358 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=470
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..657.47 rows=10224 width=20) (actual time=0.008..11.409 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=453
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..656.48 rows=10274 width=20) (actual time=0.008..14.015 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=451
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..555.18 rows=8659 width=20) (actual time=0.005..9.579 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=382
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..516.89 rows=8045 width=20) (actual time=0.028..10.698 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=356
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..476.19 rows=7409 width=20) (actual time=0.014..9.778 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=328
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.06 rows=153 width=20) (actual time=0.004..0.004 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=60.31..60.31 rows=2331 width=36) (actual time=1.777..1.778 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=111
                                ->  Seq Scan on dim_product p  (cost=0.00..60.31 rows=2331 width=36) (actual time=0.243..0.978 rows=3828.00 loops=3)
                                      Buffers: shared hit=111
Planning:
  Buffers: shared hit=144
Planning Time: 2.183 ms
Execution Time: 344.481 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=12592.37..12654.38 rows=200 width=64) (actual time=408.503..422.195 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=7058
  ->  Gather Merge  (cost=12592.37..12648.28 rows=480 width=64) (actual time=408.481..422.171 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=7058
        ->  Sort  (cost=11592.35..11592.85 rows=200 width=64) (actual time=356.135..356.144 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=7058
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=11582.20..11584.70 rows=200 width=64) (actual time=356.061..356.075 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=7042
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=89.45..11025.28 rows=111385 width=48) (actual time=1.873..234.996 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=7042
                          ->  Parallel Append  (cost=0.00..10642.91 rows=111384 width=20) (actual time=0.020..125.416 rows=174959.33 loops=3)
                                Buffers: shared hit=6931
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1566.69 rows=24434 width=20) (actual time=0.020..40.731 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1078
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1123.36 rows=17568 width=20) (actual time=0.017..32.947 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=772
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..935.36 rows=14618 width=20) (actual time=0.014..24.247 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=643
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..790.35 rows=12268 width=20) (actual time=0.016..15.173 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=545
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..736.88 rows=11494 width=20) (actual time=0.020..40.064 rows=38395.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 684
                                      Buffers: shared hit=507
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..688.93 rows=10746 width=20) (actual time=0.014..30.471 rows=35917.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 621
                                      Buffers: shared hit=474
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..686.26 rows=10713 width=20) (actual time=0.013..7.378 rows=11905.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 236
                                      Buffers: shared hit=472
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..682.90 rows=10645 width=20) (actual time=0.009..25.451 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=470
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..657.47 rows=10224 width=20) (actual time=0.009..13.447 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=453
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..656.48 rows=10274 width=20) (actual time=0.009..16.221 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=451
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..555.18 rows=8659 width=20) (actual time=0.007..21.383 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=382
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..516.89 rows=8045 width=20) (actual time=0.008..9.901 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=356
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..476.19 rows=7409 width=20) (actual time=0.013..9.728 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=328
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.06 rows=153 width=20) (actual time=0.003..0.003 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=60.31..60.31 rows=2331 width=36) (actual time=1.825..1.826 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=111
                                ->  Seq Scan on dim_product p  (cost=0.00..60.31 rows=2331 width=36) (actual time=0.243..0.991 rows=3828.00 loops=3)
                                      Buffers: shared hit=111
Planning:
  Buffers: shared hit=4
Planning Time: 1.013 ms
Execution Time: 422.435 ms
```

## Top 10 customers by revenue

With indexes:
```
Limit  (cost=15397.55..15397.58 rows=10 width=36) (actual time=414.626..417.303 rows=10.00 loops=1)
  Buffers: shared hit=6994
  ->  Sort  (cost=15397.55..15408.85 rows=4520 width=36) (actual time=414.624..417.298 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6994
        ->  Finalize HashAggregate  (cost=15243.38..15299.88 rows=4520 width=36) (actual time=408.501..415.221 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6991
              ->  Gather  (cost=14020.72..15162.02 rows=10848 width=36) (actual time=389.119..398.276 rows=8115.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6991
                    ->  Partial HashAggregate  (cost=13020.72..13077.22 rows=4520 width=36) (actual time=310.206..313.328 rows=2705.00 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6991
                          Worker 0:  Batches: 1  Memory Usage: 1297kB
                          Worker 1:  Batches: 1  Memory Usage: 1041kB
                          ->  Hash Join  (cost=121.70..11906.87 rows=222770 width=20) (actual time=3.941..214.538 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6991
                                ->  Parallel Append  (cost=0.00..11199.85 rows=222771 width=20) (actual time=0.028..121.840 rows=178043.00 loops=3)
                                      Buffers: shared hit=6931
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1566.69 rows=48869 width=20) (actual time=0.028..54.703 rows=83077.00 loops=1)
                                            Buffers: shared hit=1078
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1123.36 rows=35136 width=20) (actual time=0.027..40.593 rows=59731.00 loops=1)
                                            Buffers: shared hit=772
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..935.36 rows=29236 width=20) (actual time=0.020..25.819 rows=49701.00 loops=1)
                                            Buffers: shared hit=643
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..790.35 rows=24535 width=20) (actual time=0.021..20.471 rows=41710.00 loops=1)
                                            Buffers: shared hit=545
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..736.88 rows=22988 width=20) (actual time=0.015..6.512 rows=13026.33 loops=3)
                                            Buffers: shared hit=507
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..688.93 rows=21493 width=20) (actual time=0.028..8.828 rows=18269.00 loops=2)
                                            Buffers: shared hit=474
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..686.26 rows=21426 width=20) (actual time=0.007..16.284 rows=36425.00 loops=1)
                                            Buffers: shared hit=472
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..682.90 rows=21290 width=20) (actual time=0.007..15.474 rows=36193.00 loops=1)
                                            Buffers: shared hit=470
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..657.47 rows=20447 width=20) (actual time=0.007..14.602 rows=34760.00 loops=1)
                                            Buffers: shared hit=453
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..656.48 rows=20548 width=20) (actual time=0.011..27.238 rows=34931.00 loops=1)
                                            Buffers: shared hit=451
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..555.18 rows=17318 width=20) (actual time=0.009..13.315 rows=29440.00 loops=1)
                                            Buffers: shared hit=382
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..516.89 rows=16089 width=20) (actual time=0.011..13.598 rows=27352.00 loops=1)
                                            Buffers: shared hit=356
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..476.19 rows=14819 width=20) (actual time=0.014..9.500 rows=25192.00 loops=1)
                                            Buffers: shared hit=328
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.06 rows=306 width=20) (actual time=0.004..0.004 rows=0.00 loops=1)
                                ->  Hash  (cost=65.20..65.20 rows=4520 width=8) (actual time=3.851..3.852 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..65.20 rows=4520 width=8) (actual time=0.370..2.043 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=85
Planning Time: 2.401 ms
Execution Time: 418.788 ms
```

Index scans turned off:
```
Limit  (cost=15397.55..15397.58 rows=10 width=36) (actual time=338.400..363.009 rows=10.00 loops=1)
  Buffers: shared hit=6991
  ->  Sort  (cost=15397.55..15408.85 rows=4520 width=36) (actual time=338.397..363.003 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6991
        ->  Finalize HashAggregate  (cost=15243.38..15299.88 rows=4520 width=36) (actual time=334.743..361.745 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6991
              ->  Gather  (cost=14020.72..15162.02 rows=10848 width=36) (actual time=322.039..350.817 rows=8145.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6991
                    ->  Partial HashAggregate  (cost=13020.72..13077.22 rows=4520 width=36) (actual time=242.923..245.050 rows=2715.00 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6991
                          Worker 0:  Batches: 1  Memory Usage: 1297kB
                          Worker 1:  Batches: 1  Memory Usage: 1041kB
                          ->  Hash Join  (cost=121.70..11906.87 rows=222770 width=20) (actual time=3.767..168.962 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6991
                                ->  Parallel Append  (cost=0.00..11199.85 rows=222771 width=20) (actual time=0.038..94.253 rows=178043.00 loops=3)
                                      Buffers: shared hit=6931
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1566.69 rows=48869 width=20) (actual time=0.029..33.994 rows=83077.00 loops=1)
                                            Buffers: shared hit=1078
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1123.36 rows=35136 width=20) (actual time=0.028..22.268 rows=59731.00 loops=1)
                                            Buffers: shared hit=772
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..935.36 rows=29236 width=20) (actual time=0.014..21.966 rows=49701.00 loops=1)
                                            Buffers: shared hit=643
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..790.35 rows=24535 width=20) (actual time=0.018..23.595 rows=41710.00 loops=1)
                                            Buffers: shared hit=545
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..736.88 rows=22988 width=20) (actual time=0.013..6.070 rows=13026.33 loops=3)
                                            Buffers: shared hit=507
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..688.93 rows=21493 width=20) (actual time=0.018..6.619 rows=18269.00 loops=2)
                                            Buffers: shared hit=474
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..686.26 rows=21426 width=20) (actual time=0.006..10.567 rows=36425.00 loops=1)
                                            Buffers: shared hit=472
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..682.90 rows=21290 width=20) (actual time=0.008..13.831 rows=36193.00 loops=1)
                                            Buffers: shared hit=470
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..657.47 rows=20447 width=20) (actual time=0.010..11.409 rows=34760.00 loops=1)
                                            Buffers: shared hit=453
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..656.48 rows=20548 width=20) (actual time=0.008..11.191 rows=34931.00 loops=1)
                                            Buffers: shared hit=451
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..555.18 rows=17318 width=20) (actual time=0.009..9.542 rows=29440.00 loops=1)
                                            Buffers: shared hit=382
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..516.89 rows=16089 width=20) (actual time=0.007..12.177 rows=27352.00 loops=1)
                                            Buffers: shared hit=356
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..476.19 rows=14819 width=20) (actual time=0.036..11.865 rows=25192.00 loops=1)
                                            Buffers: shared hit=328
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.06 rows=306 width=20) (actual time=0.008..0.008 rows=0.00 loops=1)
                                ->  Hash  (cost=65.20..65.20 rows=4520 width=8) (actual time=3.623..3.624 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..65.20 rows=4520 width=8) (actual time=0.387..1.794 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=4
Planning Time: 1.766 ms
Execution Time: 364.083 ms
```

## One month of sales (June 2011)

With indexes:
```
Aggregate  (cost=1018.83..1018.84 rows=1 width=32) (actual time=15.987..15.988 rows=1.00 loops=1)
  Buffers: shared hit=472
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1018.38 rows=182 width=16) (actual time=0.025..10.022 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=472
Planning:
  Buffers: shared hit=38
Planning Time: 0.325 ms
Execution Time: 16.022 ms
```

Index scans turned off:
```
Aggregate  (cost=1018.83..1018.84 rows=1 width=32) (actual time=15.449..15.451 rows=1.00 loops=1)
  Buffers: shared hit=472
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1018.38 rows=182 width=16) (actual time=0.021..9.735 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=472
Planning Time: 0.206 ms
Execution Time: 15.483 ms
```

## One customer's orders (point lookup)

With indexes:
```
Aggregate  (cost=5289.56..5289.57 rows=1 width=8) (actual time=1.631..1.637 rows=1.00 loops=1)
  Buffers: shared hit=6 read=26
  ->  Append  (cost=5.91..5282.88 rows=2675 width=0) (actual time=0.561..1.627 rows=40.00 loops=1)
        Buffers: shared hit=6 read=26
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..412.47 rows=209 width=0) (actual time=0.436..0.436 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_customer_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.144..0.144 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..343.16 rows=174 width=0) (actual time=0.123..0.125 rows=12.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=1
              Buffers: shared hit=1 read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_customer_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.104..0.104 rows=12.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..270.98 rows=137 width=0) (actual time=0.093..0.093 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_customer_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.081..0.081 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..356.63 rows=181 width=0) (actual time=0.088..0.089 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_customer_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.077..0.077 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..291.32 rows=147 width=0) (actual time=0.091..0.091 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_04_customer_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.080..0.080 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..360.66 rows=183 width=0) (actual time=0.086..0.087 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_customer_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.075..0.075 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..358.65 rows=182 width=0) (actual time=0.106..0.111 rows=26.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=2
              Buffers: shared hit=2 read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_customer_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.088..0.088 rows=26.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..384.42 rows=195 width=0) (actual time=0.100..0.101 rows=2.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=1
              Buffers: shared hit=1 read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_customer_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.086..0.086 rows=2.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..344.06 rows=175 width=0) (actual time=0.095..0.096 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_customer_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.084..0.084 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..487.87 rows=249 width=0) (actual time=0.088..0.088 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_customer_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.076..0.077 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..584.98 rows=299 width=0) (actual time=0.087..0.087 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_customer_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.076..0.077 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..812.97 rows=415 width=0) (actual time=0.109..0.109 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_customer_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.098..0.098 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..250.06 rows=126 width=0) (actual time=0.087..0.087 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_customer_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.075..0.075 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.013..0.013 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_customer_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.005..0.005 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=9 read=1
Planning Time: 1.556 ms
Execution Time: 2.619 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11880.81..11880.82 rows=1 width=8) (actual time=124.465..157.591 rows=1.00 loops=1)
  Buffers: shared hit=6931
  ->  Gather  (cost=11880.59..11880.80 rows=2 width=8) (actual time=123.702..157.580 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6931
        ->  Partial Aggregate  (cost=10880.59..10880.60 rows=1 width=8) (actual time=49.808..49.813 rows=1.00 loops=3)
              Buffers: shared hit=6931
              ->  Parallel Append  (cost=0.00..10877.81 rows=1113 width=0) (actual time=19.414..49.802 rows=13.33 loops=3)
                    Buffers: shared hit=6931
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=244 width=0) (actual time=9.240..9.240 rows=0.00 loops=3)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1078
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=176 width=0) (actual time=23.641..23.641 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=772
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=146 width=0) (actual time=18.675..18.675 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=643
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=123 width=0) (actual time=12.314..12.314 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=545
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=115 width=0) (actual time=11.324..11.377 rows=2.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 39077
                          Buffers: shared hit=507
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=108 width=0) (actual time=8.641..8.641 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=474
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=107 width=0) (actual time=0.010..7.006 rows=26.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36399
                          Buffers: shared hit=472
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=106 width=0) (actual time=7.903..7.903 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=470
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=102 width=0) (actual time=6.767..7.721 rows=12.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34748
                          Buffers: shared hit=453
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=103 width=0) (actual time=6.995..6.995 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=451
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=86 width=0) (actual time=6.517..6.517 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 29440
                          Buffers: shared hit=382
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=81 width=0) (actual time=5.896..5.896 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=356
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.24 rows=74 width=0) (actual time=4.920..4.920 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=328
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=2 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 1.055 ms
Execution Time: 157.786 ms
```

## One product's sales (point lookup)

With indexes:
```
Aggregate  (cost=5289.56..5289.57 rows=1 width=8) (actual time=1.823..1.835 rows=1.00 loops=1)
  Buffers: shared hit=73 read=26
  ->  Append  (cost=5.91..5282.88 rows=2675 width=0) (actual time=0.243..1.819 rows=71.00 loops=1)
        Buffers: shared hit=73 read=26
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..412.47 rows=209 width=0) (actual time=0.242..0.284 rows=30.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=30
              Buffers: shared hit=30 read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_product_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.201..0.201 rows=30.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..343.16 rows=174 width=0) (actual time=0.128..0.153 rows=21.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=21
              Buffers: shared hit=21 read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_product_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.109..0.109 rows=21.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..270.98 rows=137 width=0) (actual time=0.108..0.117 rows=7.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=7
              Buffers: shared hit=7 read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_product_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.090..0.090 rows=7.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..356.63 rows=181 width=0) (actual time=0.109..0.119 rows=8.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=8
              Buffers: shared hit=8 read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_product_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.092..0.093 rows=8.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..291.32 rows=147 width=0) (actual time=0.105..0.111 rows=5.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=5
              Buffers: shared hit=5 read=2
              ->  Bitmap Index Scan on fact_sales_2011_04_product_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.089..0.089 rows=5.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..360.66 rows=183 width=0) (actual time=0.091..0.091 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_product_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.077..0.078 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..358.65 rows=182 width=0) (actual time=0.089..0.089 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_product_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.074..0.074 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..384.42 rows=195 width=0) (actual time=0.089..0.090 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_product_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.077..0.077 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..344.06 rows=175 width=0) (actual time=0.084..0.085 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_product_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.072..0.072 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..487.87 rows=249 width=0) (actual time=0.149..0.149 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_product_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.129..0.129 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..584.98 rows=299 width=0) (actual time=0.172..0.173 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_product_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.145..0.145 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..812.97 rows=415 width=0) (actual time=0.161..0.162 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_product_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.142..0.143 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..250.06 rows=126 width=0) (actual time=0.146..0.146 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_product_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.130..0.130 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.025..0.026 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_product_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.011..0.011 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=4
Planning Time: 1.191 ms
Execution Time: 2.233 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11880.81..11880.82 rows=1 width=8) (actual time=113.828..126.991 rows=1.00 loops=1)
  Buffers: shared hit=6931
  ->  Gather  (cost=11880.59..11880.80 rows=2 width=8) (actual time=113.223..126.974 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6931
        ->  Partial Aggregate  (cost=10880.59..10880.60 rows=1 width=8) (actual time=43.465..43.470 rows=1.00 loops=3)
              Buffers: shared hit=6931
              ->  Parallel Append  (cost=0.00..10877.81 rows=1113 width=0) (actual time=8.419..43.440 rows=23.67 loops=3)
                    Buffers: shared hit=6931
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=244 width=0) (actual time=9.589..9.589 rows=0.00 loops=3)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1078
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=176 width=0) (actual time=9.369..9.369 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=772
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=146 width=0) (actual time=8.774..8.775 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=643
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=123 width=0) (actual time=0.047..11.493 rows=30.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 41680
                          Buffers: shared hit=545
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=115 width=0) (actual time=9.041..9.041 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 39079
                          Buffers: shared hit=507
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=108 width=0) (actual time=9.984..9.984 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=474
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=107 width=0) (actual time=8.614..8.614 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36425
                          Buffers: shared hit=472
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=106 width=0) (actual time=0.234..8.517 rows=8.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36185
                          Buffers: shared hit=470
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=102 width=0) (actual time=0.559..8.310 rows=21.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 34739
                          Buffers: shared hit=453
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=103 width=0) (actual time=8.173..8.173 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=451
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=86 width=0) (actual time=0.096..6.970 rows=5.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 29435
                          Buffers: shared hit=382
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=81 width=0) (actual time=0.963..6.443 rows=7.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 27345
                          Buffers: shared hit=356
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.24 rows=74 width=0) (actual time=5.754..5.755 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=328
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=2 width=0) (actual time=0.004..0.004 rows=0.00 loops=1)
                          Filter: (product_key = 1)
Planning:
  Buffers: shared hit=4
Planning Time: 1.064 ms
Execution Time: 127.103 ms
```

## One day's sales (point lookup)

With indexes:
```
Aggregate  (cost=5289.56..5289.57 rows=1 width=8) (actual time=1.713..1.721 rows=1.00 loops=1)
  Buffers: shared hit=19 read=27
  ->  Append  (cost=5.91..5282.88 rows=2675 width=0) (actual time=0.644..1.632 rows=1073.00 loops=1)
        Buffers: shared hit=19 read=27
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..412.47 rows=209 width=0) (actual time=0.187..0.187 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_date_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.168..0.168 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..343.16 rows=174 width=0) (actual time=0.102..0.102 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_date_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.091..0.091 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..270.98 rows=137 width=0) (actual time=0.087..0.087 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_date_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.076..0.076 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..356.63 rows=181 width=0) (actual time=0.086..0.086 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_date_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.074..0.074 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..291.32 rows=147 width=0) (actual time=0.179..0.336 rows=1073.00 loops=1)
              Recheck Cond: (date_key = 100)
              Heap Blocks: exact=17
              Buffers: shared hit=17 read=3
              ->  Bitmap Index Scan on fact_sales_2011_04_date_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.157..0.157 rows=1073.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=3
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..360.66 rows=183 width=0) (actual time=0.104..0.104 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_date_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.091..0.091 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..358.65 rows=182 width=0) (actual time=0.087..0.087 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_date_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.074..0.074 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..384.42 rows=195 width=0) (actual time=0.090..0.091 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_date_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.077..0.078 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..344.06 rows=175 width=0) (actual time=0.090..0.090 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_date_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.072..0.072 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..487.87 rows=249 width=0) (actual time=0.084..0.084 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_date_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.075..0.075 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..584.98 rows=299 width=0) (actual time=0.087..0.088 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_date_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.076..0.076 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..812.97 rows=415 width=0) (actual time=0.085..0.085 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_date_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.073..0.073 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..250.06 rows=126 width=0) (actual time=0.086..0.087 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_date_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.077..0.077 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.012..0.013 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_date_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.004..0.004 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=30
Planning Time: 0.953 ms
Execution Time: 2.024 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11880.81..11880.82 rows=1 width=8) (actual time=114.343..149.632 rows=1.00 loops=1)
  Buffers: shared hit=6931
  ->  Gather  (cost=11880.59..11880.80 rows=2 width=8) (actual time=113.893..149.618 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6931
        ->  Partial Aggregate  (cost=10880.59..10880.60 rows=1 width=8) (actual time=42.469..42.474 rows=1.00 loops=3)
              Buffers: shared hit=6931
              ->  Parallel Append  (cost=0.00..10877.81 rows=1113 width=0) (actual time=8.299..42.413 rows=357.67 loops=3)
                    Buffers: shared hit=6931
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=244 width=0) (actual time=7.442..7.442 rows=0.00 loops=3)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1078
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=176 width=0) (actual time=11.887..11.888 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=772
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=146 width=0) (actual time=8.382..8.382 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=643
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=123 width=0) (actual time=9.783..9.784 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=545
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=115 width=0) (actual time=8.172..8.172 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 39079
                          Buffers: shared hit=507
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=108 width=0) (actual time=6.651..6.651 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=474
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=107 width=0) (actual time=4.915..4.915 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36425
                          Buffers: shared hit=472
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=106 width=0) (actual time=22.941..22.941 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=470
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=102 width=0) (actual time=7.847..7.847 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 34760
                          Buffers: shared hit=453
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=103 width=0) (actual time=7.674..7.674 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=451
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=86 width=0) (actual time=0.011..6.931 rows=1073.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 28367
                          Buffers: shared hit=382
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=81 width=0) (actual time=5.488..5.488 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=356
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.24 rows=74 width=0) (actual time=4.037..4.037 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=328
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=2 width=0) (actual time=0.005..0.005 rows=0.00 loops=1)
                          Filter: (date_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 0.882 ms
Execution Time: 149.811 ms
```

## Monthly revenue by country, from the fact table

With indexes:
```
Finalize GroupAggregate  (cost=25574.05..40127.28 rows=39996 width=68) (actual time=417.252..661.923 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Buffers: shared hit=7025, temp read=2262 written=2269
  ->  Gather Merge  (cost=25574.05..38467.45 rows=95990 width=68) (actual time=417.239..660.397 rows=320.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=7025, temp read=2262 written=2269
        ->  Partial GroupAggregate  (cost=24574.03..26387.80 rows=39996 width=68) (actual time=243.599..398.390 rows=106.67 loops=3)
              Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
              Buffers: shared hit=7025, temp read=2262 written=2269
              ->  Sort  (cost=24574.03..24852.49 rows=111384 width=52) (actual time=243.516..301.558 rows=174959.33 loops=3)
                    Sort Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
                    Sort Method: external merge  Disk: 7200kB
                    Buffers: shared hit=7025, temp read=2262 written=2269
                    Worker 0:  Sort Method: external merge  Disk: 5576kB
                    Worker 1:  Sort Method: external merge  Disk: 5320kB
                    ->  Parallel Append  (cost=0.00..11429.16 rows=111384 width=52) (actual time=0.037..139.116 rows=174959.33 loops=3)
                          Buffers: shared hit=6931
                          ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=24434 width=52) (actual time=0.033..62.862 rows=82004.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1073
                                Buffers: shared hit=1078
                          ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=17568 width=52) (actual time=0.023..41.747 rows=58537.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1194
                                Buffers: shared hit=772
                          ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=14618 width=52) (actual time=0.015..27.038 rows=48900.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 801
                                Buffers: shared hit=643
                          ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=12268 width=52) (actual time=0.018..22.326 rows=40991.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 719
                                Buffers: shared hit=545
                          ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=11494 width=52) (actual time=0.013..27.518 rows=38395.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 684
                                Buffers: shared hit=507
                          ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=10746 width=52) (actual time=0.011..21.180 rows=35917.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 621
                                Buffers: shared hit=474
                          ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=10713 width=52) (actual time=0.011..9.581 rows=11905.33 loops=3)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 236
                                Buffers: shared hit=472
                          ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=10645 width=52) (actual time=0.006..19.369 rows=35497.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 696
                                Buffers: shared hit=470
                          ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=10224 width=52) (actual time=0.008..16.594 rows=34060.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 700
                                Buffers: shared hit=453
                          ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=10274 width=52) (actual time=0.006..28.738 rows=34264.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 667
                                Buffers: shared hit=451
                          ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=8659 width=52) (actual time=0.007..22.651 rows=28882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 558
                                Buffers: shared hit=382
                          ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=8045 width=52) (actual time=0.011..17.692 rows=26882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 470
                                Buffers: shared hit=356
                          ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.23 rows=7409 width=52) (actual time=0.035..19.770 rows=24833.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 359
                                Buffers: shared hit=328
                          ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=153 width=52) (actual time=0.007..0.007 rows=0.00 loops=1)
                                Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 0.920 ms
Execution Time: 666.203 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=25574.05..40127.28 rows=39996 width=68) (actual time=438.571..572.589 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Buffers: shared hit=7025, temp read=2262 written=2270
  ->  Gather Merge  (cost=25574.05..38467.45 rows=95990 width=68) (actual time=438.549..571.747 rows=328.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=7025, temp read=2262 written=2270
        ->  Partial GroupAggregate  (cost=24574.03..26387.80 rows=39996 width=68) (actual time=262.520..380.809 rows=109.33 loops=3)
              Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
              Buffers: shared hit=7025, temp read=2262 written=2270
              ->  Sort  (cost=24574.03..24852.49 rows=111384 width=52) (actual time=262.453..305.235 rows=174959.33 loops=3)
                    Sort Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
                    Sort Method: external merge  Disk: 5080kB
                    Buffers: shared hit=7025, temp read=2262 written=2270
                    Worker 0:  Sort Method: external merge  Disk: 6496kB
                    Worker 1:  Sort Method: external merge  Disk: 6520kB
                    ->  Parallel Append  (cost=0.00..11429.16 rows=111384 width=52) (actual time=0.025..153.889 rows=174959.33 loops=3)
                          Buffers: shared hit=6931
                          ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1688.86 rows=24434 width=52) (actual time=0.027..54.596 rows=82004.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1073
                                Buffers: shared hit=1078
                          ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1211.20 rows=17568 width=52) (actual time=0.019..35.635 rows=58537.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1194
                                Buffers: shared hit=772
                          ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1008.45 rows=14618 width=52) (actual time=0.011..30.385 rows=48900.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 801
                                Buffers: shared hit=643
                          ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..851.69 rows=12268 width=52) (actual time=0.016..22.515 rows=40991.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 719
                                Buffers: shared hit=545
                          ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..794.35 rows=11494 width=52) (actual time=0.011..26.265 rows=38395.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 684
                                Buffers: shared hit=507
                          ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..742.66 rows=10746 width=52) (actual time=0.013..17.929 rows=35917.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 621
                                Buffers: shared hit=474
                          ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..739.83 rows=10713 width=52) (actual time=0.014..19.252 rows=35716.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 709
                                Buffers: shared hit=472
                          ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..736.12 rows=10645 width=52) (actual time=0.010..7.780 rows=11832.33 loops=3)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 232
                                Buffers: shared hit=470
                          ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..708.59 rows=10224 width=52) (actual time=0.009..15.662 rows=17030.00 loops=2)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 350
                                Buffers: shared hit=453
                          ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..707.85 rows=10274 width=52) (actual time=0.008..45.736 rows=34264.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 667
                                Buffers: shared hit=451
                          ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..598.47 rows=8659 width=52) (actual time=0.008..30.901 rows=28882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 558
                                Buffers: shared hit=382
                          ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..557.12 rows=8045 width=52) (actual time=0.008..40.545 rows=26882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 470
                                Buffers: shared hit=356
                          ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..513.23 rows=7409 width=52) (actual time=0.015..19.755 rows=24833.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 359
                                Buffers: shared hit=328
                          ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.82 rows=153 width=52) (actual time=0.004..0.004 rows=0.00 loops=1)
                                Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 1.031 ms
Execution Time: 575.433 ms
```

## Monthly revenue by country, from the materialized view

With indexes:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.022..0.047 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning:
  Buffers: shared hit=7 read=1
Planning Time: 0.741 ms
Execution Time: 0.073 ms
```

Index scans turned off:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.018..0.043 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning Time: 0.073 ms
Execution Time: 0.054 ms
```
