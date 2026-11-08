# Query plans

Generated 2026-11-08 20:59:40 by `scripts/performance.py`.

Each query is run twice: with index scans allowed, and with index scans turned off. The second run shows what the planner does without the indexes.

## Revenue by product category

With indexes:
```
Finalize GroupAggregate  (cost=13718.26..13719.54 rows=4 width=40) (actual time=356.319..391.632 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=6804
  ->  Gather Merge  (cost=13718.26..13719.42 rows=10 width=40) (actual time=356.303..391.612 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6804
        ->  Sort  (cost=12718.23..12718.24 rows=4 width=40) (actual time=284.730..284.736 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=6804
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=12718.14..12718.19 rows=4 width=40) (actual time=284.661..284.673 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=6788
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=123.13..11624.15 rows=218798 width=14) (actual time=2.675..187.485 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=6788
                          ->  Parallel Append  (cost=0.00..10926.04 rows=218798 width=10) (actual time=0.028..95.395 rows=174959.33 loops=3)
                                Buffers: shared hit=6677
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=48211 width=10) (actual time=0.014..45.407 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1037
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=34458 width=10) (actual time=0.043..26.493 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=741
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=28755 width=10) (actual time=0.008..20.494 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=618
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=24096 width=10) (actual time=0.022..15.566 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=527
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=22587 width=10) (actual time=0.009..15.120 rows=38395.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 684
                                      Buffers: shared hit=490
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=21136 width=10) (actual time=0.007..5.178 rows=11972.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 207
                                      Buffers: shared hit=456
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=21005 width=10) (actual time=0.008..6.251 rows=17858.00 loops=2)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 354
                                      Buffers: shared hit=455
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=20890 width=10) (actual time=0.006..14.195 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=452
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=20034 width=10) (actual time=0.009..14.032 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=438
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=20155 width=10) (actual time=0.008..15.419 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=435
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=16989 width=10) (actual time=0.006..9.999 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=368
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=15813 width=10) (actual time=0.008..9.291 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=343
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=14608 width=10) (actual time=0.013..10.444 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=317
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=156 width=20) (actual time=0.003..0.003 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=75.28..75.28 rows=3828 width=12) (actual time=2.611..2.611 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=111
                                ->  Seq Scan on dim_product p  (cost=0.00..75.28 rows=3828 width=12) (actual time=0.252..1.359 rows=3828.00 loops=3)
                                      Buffers: shared hit=111
Planning:
  Buffers: shared hit=155
Planning Time: 2.956 ms
Execution Time: 391.889 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=13718.26..13719.54 rows=4 width=40) (actual time=324.673..346.022 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=6804
  ->  Gather Merge  (cost=13718.26..13719.42 rows=10 width=40) (actual time=324.655..345.998 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6804
        ->  Sort  (cost=12718.23..12718.24 rows=4 width=40) (actual time=273.779..273.784 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=6804
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=12718.14..12718.19 rows=4 width=40) (actual time=273.732..273.739 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=6788
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=123.13..11624.15 rows=218798 width=14) (actual time=1.669..179.546 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=6788
                          ->  Parallel Append  (cost=0.00..10926.04 rows=218798 width=10) (actual time=0.016..91.578 rows=174959.33 loops=3)
                                Buffers: shared hit=6677
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=48211 width=10) (actual time=0.011..32.593 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1037
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=34458 width=10) (actual time=0.015..23.531 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=741
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=28755 width=10) (actual time=0.011..23.251 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=618
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=24096 width=10) (actual time=0.021..15.513 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=527
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=22587 width=10) (actual time=0.011..16.942 rows=38395.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 684
                                      Buffers: shared hit=490
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=21136 width=10) (actual time=0.011..17.237 rows=35917.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 621
                                      Buffers: shared hit=456
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=21005 width=10) (actual time=0.015..5.046 rows=11905.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 236
                                      Buffers: shared hit=455
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=20890 width=10) (actual time=0.006..14.235 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=452
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=20034 width=10) (actual time=0.006..14.674 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=438
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=20155 width=10) (actual time=0.006..13.880 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=435
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=16989 width=10) (actual time=0.007..10.974 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=368
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=15813 width=10) (actual time=0.007..10.571 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=343
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=14608 width=10) (actual time=0.011..9.238 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=317
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=156 width=20) (actual time=0.003..0.003 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=75.28..75.28 rows=3828 width=12) (actual time=1.628..1.629 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=111
                                ->  Seq Scan on dim_product p  (cost=0.00..75.28 rows=3828 width=12) (actual time=0.203..0.847 rows=3828.00 loops=3)
                                      Buffers: shared hit=111
Planning:
  Buffers: shared hit=4
Planning Time: 0.795 ms
Execution Time: 346.167 ms
```

## Top 10 customers by revenue

With indexes:
```
Limit  (cost=15094.91..15094.93 rows=10 width=36) (actual time=262.994..272.279 rows=10.00 loops=1)
  Buffers: shared hit=6740
  ->  Sort  (cost=15094.91..15105.84 rows=4371 width=36) (actual time=262.992..272.276 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6740
        ->  Finalize HashAggregate  (cost=14945.81..15000.45 rows=4371 width=36) (actual time=259.930..271.278 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6737
              ->  Gather  (cost=13763.50..14867.14 rows=10490 width=36) (actual time=247.404..260.688 rows=8157.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6737
                    ->  Partial HashAggregate  (cost=12763.50..12818.14 rows=4371 width=36) (actual time=191.423..193.550 rows=2719.00 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6737
                          Worker 0:  Batches: 1  Memory Usage: 1297kB
                          Worker 1:  Batches: 1  Memory Usage: 1041kB
                          ->  Hash Join  (cost=118.35..11649.63 rows=222775 width=10) (actual time=2.566..130.738 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6737
                                ->  Parallel Append  (cost=0.00..10945.93 rows=222775 width=10) (actual time=0.021..71.104 rows=178043.00 loops=3)
                                      Buffers: shared hit=6677
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=48869 width=10) (actual time=0.017..26.190 rows=83077.00 loops=1)
                                            Buffers: shared hit=1037
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=35136 width=10) (actual time=0.020..22.330 rows=59731.00 loops=1)
                                            Buffers: shared hit=741
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=29236 width=10) (actual time=0.010..15.313 rows=49701.00 loops=1)
                                            Buffers: shared hit=618
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=24535 width=10) (actual time=0.013..11.945 rows=41710.00 loops=1)
                                            Buffers: shared hit=527
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=22988 width=10) (actual time=0.022..12.173 rows=39079.00 loops=1)
                                            Buffers: shared hit=490
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=21493 width=10) (actual time=0.008..3.873 rows=12179.33 loops=3)
                                            Buffers: shared hit=456
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=21426 width=10) (actual time=0.006..7.904 rows=36425.00 loops=1)
                                            Buffers: shared hit=455
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=21290 width=10) (actual time=0.004..8.066 rows=36193.00 loops=1)
                                            Buffers: shared hit=452
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=20447 width=10) (actual time=0.007..10.117 rows=34760.00 loops=1)
                                            Buffers: shared hit=438
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=20548 width=10) (actual time=0.006..12.018 rows=34931.00 loops=1)
                                            Buffers: shared hit=435
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=17318 width=10) (actual time=0.007..8.684 rows=29440.00 loops=1)
                                            Buffers: shared hit=368
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=16089 width=10) (actual time=0.006..7.451 rows=27352.00 loops=1)
                                            Buffers: shared hit=343
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=14819 width=10) (actual time=0.013..7.225 rows=25192.00 loops=1)
                                            Buffers: shared hit=317
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=312 width=20) (actual time=0.004..0.004 rows=0.00 loops=1)
                                ->  Hash  (cost=63.71..63.71 rows=4371 width=8) (actual time=2.482..2.482 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..63.71 rows=4371 width=8) (actual time=0.287..1.175 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=100
Planning Time: 1.872 ms
Execution Time: 272.883 ms
```

Index scans turned off:
```
Limit  (cost=15094.91..15094.93 rows=10 width=36) (actual time=263.945..289.667 rows=10.00 loops=1)
  Buffers: shared hit=6737
  ->  Sort  (cost=15094.91..15105.84 rows=4371 width=36) (actual time=263.943..289.663 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6737
        ->  Finalize HashAggregate  (cost=14945.81..15000.45 rows=4371 width=36) (actual time=261.277..288.797 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6737
              ->  Gather  (cost=13763.50..14867.14 rows=10490 width=36) (actual time=251.958..280.682 rows=8134.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6737
                    ->  Partial HashAggregate  (cost=12763.50..12818.14 rows=4371 width=36) (actual time=194.045..195.583 rows=2711.33 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6737
                          Worker 0:  Batches: 1  Memory Usage: 1297kB
                          Worker 1:  Batches: 1  Memory Usage: 1041kB
                          ->  Hash Join  (cost=118.35..11649.63 rows=222775 width=10) (actual time=2.524..131.786 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6737
                                ->  Parallel Append  (cost=0.00..10945.93 rows=222775 width=10) (actual time=0.018..71.917 rows=178043.00 loops=3)
                                      Buffers: shared hit=6677
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=48869 width=10) (actual time=0.015..26.934 rows=83077.00 loops=1)
                                            Buffers: shared hit=1037
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=35136 width=10) (actual time=0.017..19.147 rows=59731.00 loops=1)
                                            Buffers: shared hit=741
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=29236 width=10) (actual time=0.010..18.003 rows=49701.00 loops=1)
                                            Buffers: shared hit=618
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=24535 width=10) (actual time=0.019..15.836 rows=41710.00 loops=1)
                                            Buffers: shared hit=527
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=22988 width=10) (actual time=0.008..4.077 rows=13026.33 loops=3)
                                            Buffers: shared hit=490
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=21493 width=10) (actual time=0.007..5.518 rows=18269.00 loops=2)
                                            Buffers: shared hit=456
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=21426 width=10) (actual time=0.004..9.420 rows=36425.00 loops=1)
                                            Buffers: shared hit=455
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=21290 width=10) (actual time=0.005..9.154 rows=36193.00 loops=1)
                                            Buffers: shared hit=452
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=20447 width=10) (actual time=0.006..9.655 rows=34760.00 loops=1)
                                            Buffers: shared hit=438
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=20548 width=10) (actual time=0.006..7.833 rows=34931.00 loops=1)
                                            Buffers: shared hit=435
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=17318 width=10) (actual time=0.005..8.642 rows=29440.00 loops=1)
                                            Buffers: shared hit=368
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=16089 width=10) (actual time=0.005..8.028 rows=27352.00 loops=1)
                                            Buffers: shared hit=343
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=14819 width=10) (actual time=0.011..8.135 rows=25192.00 loops=1)
                                            Buffers: shared hit=317
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=312 width=20) (actual time=0.003..0.003 rows=0.00 loops=1)
                                ->  Hash  (cost=63.71..63.71 rows=4371 width=8) (actual time=2.452..2.452 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..63.71 rows=4371 width=8) (actual time=0.273..1.217 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=4
Planning Time: 0.769 ms
Execution Time: 290.285 ms
```

## One month of sales (June 2011)

With indexes:
```
Aggregate  (cost=1092.43..1092.44 rows=1 width=32) (actual time=11.621..11.622 rows=1.00 loops=1)
  Buffers: shared hit=455
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1001.38 rows=36420 width=6) (actual time=0.024..7.280 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=455
Planning:
  Buffers: shared hit=39
Planning Time: 0.326 ms
Execution Time: 11.647 ms
```

Index scans turned off:
```
Aggregate  (cost=1092.43..1092.44 rows=1 width=32) (actual time=10.177..10.178 rows=1.00 loops=1)
  Buffers: shared hit=455
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1001.38 rows=36420 width=6) (actual time=0.018..6.394 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=455
Planning Time: 0.182 ms
Execution Time: 10.201 ms
```

## One customer's orders (point lookup)

With indexes:
```
Aggregate  (cost=73.57..73.58 rows=1 width=8) (actual time=0.939..0.942 rows=1.00 loops=1)
  Buffers: shared hit=31
  ->  Append  (cost=0.29..72.91 rows=263 width=0) (actual time=0.415..0.935 rows=40.00 loops=1)
        Buffers: shared hit=31
        ->  Index Only Scan using fact_sales_2010_12_customer_key_idx on fact_sales_2010_12 fact_sales_1  (cost=0.29..4.62 rows=19 width=0) (actual time=0.037..0.037 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_01_customer_key_idx on fact_sales_2011_01 fact_sales_2  (cost=0.29..4.62 rows=19 width=0) (actual time=0.376..0.379 rows=12.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=3
        ->  Index Only Scan using fact_sales_2011_02_customer_key_idx on fact_sales_2011_02 fact_sales_3  (cost=0.29..4.58 rows=17 width=0) (actual time=0.021..0.021 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_03_customer_key_idx on fact_sales_2011_03 fact_sales_4  (cost=0.29..4.62 rows=19 width=0) (actual time=0.011..0.011 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_04_customer_key_idx on fact_sales_2011_04 fact_sales_5  (cost=0.29..4.60 rows=18 width=0) (actual time=0.011..0.011 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_05_customer_key_idx on fact_sales_2011_05 fact_sales_6  (cost=0.29..4.62 rows=19 width=0) (actual time=0.011..0.011 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_06_customer_key_idx on fact_sales_2011_06 fact_sales_7  (cost=0.29..4.60 rows=18 width=0) (actual time=0.209..0.212 rows=26.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=3
        ->  Index Only Scan using fact_sales_2011_07_customer_key_idx on fact_sales_2011_07 fact_sales_8  (cost=0.29..4.64 rows=20 width=0) (actual time=0.168..0.169 rows=2.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=3
        ->  Index Only Scan using fact_sales_2011_08_customer_key_idx on fact_sales_2011_08 fact_sales_9  (cost=0.29..4.62 rows=19 width=0) (actual time=0.014..0.014 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_09_customer_key_idx on fact_sales_2011_09 fact_sales_10  (cost=0.29..4.69 rows=23 width=0) (actual time=0.016..0.016 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_10_customer_key_idx on fact_sales_2011_10 fact_sales_11  (cost=0.29..4.75 rows=26 width=0) (actual time=0.011..0.011 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_11_customer_key_idx on fact_sales_2011_11 fact_sales_12  (cost=0.29..4.78 rows=28 width=0) (actual time=0.011..0.011 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Index Only Scan using fact_sales_2011_12_customer_key_idx on fact_sales_2011_12 fact_sales_13  (cost=0.29..4.55 rows=15 width=0) (actual time=0.010..0.010 rows=0.00 loops=1)
              Index Cond: (customer_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.012..0.012 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_customer_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.002..0.002 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=10
Planning Time: 0.653 ms
Execution Time: 1.099 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11619.36..11619.37 rows=1 width=8) (actual time=79.153..107.130 rows=1.00 loops=1)
  Buffers: shared hit=6677
  ->  Gather  (cost=11619.14..11619.35 rows=2 width=8) (actual time=78.685..107.120 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6677
        ->  Partial Aggregate  (cost=10619.14..10619.15 rows=1 width=8) (actual time=27.006..27.010 rows=1.00 loops=3)
              Buffers: shared hit=6677
              ->  Parallel Append  (cost=0.00..10618.87 rows=110 width=0) (actual time=8.487..26.998 rows=13.33 loops=3)
                    Buffers: shared hit=6677
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=16 width=0) (actual time=3.415..3.415 rows=0.00 loops=3)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1037
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=15 width=0) (actual time=9.532..9.532 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=741
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=14 width=0) (actual time=7.839..7.839 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=618
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=11 width=0) (actual time=6.070..6.070 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=527
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=12 width=0) (actual time=5.721..5.759 rows=2.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 39077
                          Buffers: shared hit=490
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=11 width=0) (actual time=6.438..6.438 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=456
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=11 width=0) (actual time=0.010..5.507 rows=26.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36399
                          Buffers: shared hit=455
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=11 width=0) (actual time=6.717..6.718 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=452
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=11 width=0) (actual time=4.949..5.705 rows=12.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34748
                          Buffers: shared hit=438
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=11 width=0) (actual time=5.238..5.238 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=435
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=11 width=0) (actual time=4.652..4.652 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 29440
                          Buffers: shared hit=368
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=10 width=0) (actual time=3.703..3.703 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=343
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.24 rows=9 width=0) (actual time=3.490..3.490 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=317
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=2 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 0.613 ms
Execution Time: 107.256 ms
```

## One product's sales (point lookup)

With indexes:
```
Aggregate  (cost=71.37..71.38 rows=1 width=8) (actual time=10.338..10.343 rows=1.00 loops=1)
  Buffers: shared hit=7 read=26
  ->  Append  (cost=0.29..70.93 rows=175 width=0) (actual time=2.849..10.329 rows=71.00 loops=1)
        Buffers: shared hit=7 read=26
        ->  Index Only Scan using fact_sales_2010_12_product_key_idx on fact_sales_2010_12 fact_sales_1  (cost=0.29..4.52 rows=13 width=0) (actual time=2.847..2.852 rows=30.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=1 read=2
        ->  Index Only Scan using fact_sales_2011_01_product_key_idx on fact_sales_2011_01 fact_sales_2  (cost=0.29..4.50 rows=12 width=0) (actual time=0.431..0.434 rows=21.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=1 read=2
        ->  Index Only Scan using fact_sales_2011_02_product_key_idx on fact_sales_2011_02 fact_sales_3  (cost=0.29..4.44 rows=9 width=0) (actual time=0.668..0.670 rows=7.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=1 read=2
        ->  Index Only Scan using fact_sales_2011_03_product_key_idx on fact_sales_2011_03 fact_sales_4  (cost=0.29..4.50 rows=12 width=0) (actual time=0.789..0.791 rows=8.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=1 read=2
        ->  Index Only Scan using fact_sales_2011_04_product_key_idx on fact_sales_2011_04 fact_sales_5  (cost=0.29..4.46 rows=10 width=0) (actual time=1.172..1.174 rows=5.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=1 read=2
        ->  Index Only Scan using fact_sales_2011_05_product_key_idx on fact_sales_2011_05 fact_sales_6  (cost=0.29..4.50 rows=12 width=0) (actual time=0.611..0.611 rows=0.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_06_product_key_idx on fact_sales_2011_06 fact_sales_7  (cost=0.29..4.48 rows=11 width=0) (actual time=0.558..0.558 rows=0.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_07_product_key_idx on fact_sales_2011_07 fact_sales_8  (cost=0.29..4.50 rows=12 width=0) (actual time=0.547..0.547 rows=0.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_08_product_key_idx on fact_sales_2011_08 fact_sales_9  (cost=0.29..4.48 rows=11 width=0) (actual time=0.574..0.574 rows=0.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_09_product_key_idx on fact_sales_2011_09 fact_sales_10  (cost=0.29..4.57 rows=16 width=0) (actual time=0.534..0.534 rows=0.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_10_product_key_idx on fact_sales_2011_10 fact_sales_11  (cost=0.29..4.62 rows=19 width=0) (actual time=0.615..0.615 rows=0.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_11_product_key_idx on fact_sales_2011_11 fact_sales_12  (cost=0.29..4.75 rows=26 width=0) (actual time=0.449..0.449 rows=0.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_12_product_key_idx on fact_sales_2011_12 fact_sales_13  (cost=0.29..4.44 rows=9 width=0) (actual time=0.460..0.460 rows=0.00 loops=1)
              Index Cond: (product_key = 1)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.034..0.035 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_product_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.006..0.006 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=4
Planning Time: 0.761 ms
Execution Time: 10.536 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11619.07..11619.08 rows=1 width=8) (actual time=73.716..83.237 rows=1.00 loops=1)
  Buffers: shared hit=6677
  ->  Gather  (cost=11618.86..11619.07 rows=2 width=8) (actual time=73.218..83.225 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6677
        ->  Partial Aggregate  (cost=10618.86..10618.87 rows=1 width=8) (actual time=25.922..25.926 rows=1.00 loops=3)
              Buffers: shared hit=6677
              ->  Parallel Append  (cost=0.00..10618.68 rows=72 width=0) (actual time=3.160..25.907 rows=23.67 loops=3)
                    Buffers: shared hit=6677
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=15 width=0) (actual time=4.439..4.440 rows=0.00 loops=3)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1037
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=11 width=0) (actual time=8.769..8.769 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=741
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=9 width=0) (actual time=7.687..7.687 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=618
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=8 width=0) (actual time=0.014..6.873 rows=30.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 41680
                          Buffers: shared hit=527
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=7 width=0) (actual time=3.687..3.687 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 39079
                          Buffers: shared hit=490
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=7 width=0) (actual time=3.798..3.799 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=456
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=6 width=0) (actual time=4.786..4.786 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36425
                          Buffers: shared hit=455
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=7 width=0) (actual time=0.176..6.548 rows=8.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36185
                          Buffers: shared hit=452
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=7 width=0) (actual time=0.362..5.611 rows=21.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 34739
                          Buffers: shared hit=438
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=6 width=0) (actual time=5.600..5.600 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=435
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=6 width=0) (actual time=0.051..3.948 rows=5.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 29435
                          Buffers: shared hit=368
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=5 width=0) (actual time=0.540..3.646 rows=7.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 27345
                          Buffers: shared hit=343
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.24 rows=5 width=0) (actual time=3.373..3.373 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=317
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=2 width=0) (actual time=0.004..0.004 rows=0.00 loops=1)
                          Filter: (product_key = 1)
Planning:
  Buffers: shared hit=4
Planning Time: 0.606 ms
Execution Time: 83.376 ms
```

## One day's sales (point lookup)

With indexes:
```
Aggregate  (cost=98.19..98.20 rows=1 width=8) (actual time=6.990..6.994 rows=1.00 loops=1)
  Buffers: shared hit=3 read=27
  ->  Append  (cost=0.29..95.47 rows=1088 width=0) (actual time=2.968..6.933 rows=1073.00 loops=1)
        Buffers: shared hit=3 read=27
        ->  Index Only Scan using fact_sales_2010_12_date_key_idx on fact_sales_2010_12 fact_sales_1  (cost=0.29..4.31 rows=1 width=0) (actual time=0.889..0.889 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_01_date_key_idx on fact_sales_2011_01 fact_sales_2  (cost=0.29..4.31 rows=1 width=0) (actual time=0.534..0.534 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_02_date_key_idx on fact_sales_2011_02 fact_sales_3  (cost=0.29..4.30 rows=1 width=0) (actual time=0.573..0.573 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_03_date_key_idx on fact_sales_2011_03 fact_sales_4  (cost=0.29..4.31 rows=1 width=0) (actual time=0.536..0.536 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_04_date_key_idx on fact_sales_2011_04 fact_sales_5  (cost=0.29..27.07 rows=1073 width=0) (actual time=0.429..0.712 rows=1073.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared hit=1 read=3
        ->  Index Only Scan using fact_sales_2011_05_date_key_idx on fact_sales_2011_05 fact_sales_6  (cost=0.29..4.31 rows=1 width=0) (actual time=0.387..0.387 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_06_date_key_idx on fact_sales_2011_06 fact_sales_7  (cost=0.29..4.31 rows=1 width=0) (actual time=0.416..0.416 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_07_date_key_idx on fact_sales_2011_07 fact_sales_8  (cost=0.29..4.31 rows=1 width=0) (actual time=0.468..0.468 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_08_date_key_idx on fact_sales_2011_08 fact_sales_9  (cost=0.29..4.31 rows=1 width=0) (actual time=0.654..0.654 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_09_date_key_idx on fact_sales_2011_09 fact_sales_10  (cost=0.29..4.31 rows=1 width=0) (actual time=0.432..0.432 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_10_date_key_idx on fact_sales_2011_10 fact_sales_11  (cost=0.29..4.31 rows=1 width=0) (actual time=0.425..0.425 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_11_date_key_idx on fact_sales_2011_11 fact_sales_12  (cost=0.29..4.31 rows=1 width=0) (actual time=0.399..0.399 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Index Only Scan using fact_sales_2011_12_date_key_idx on fact_sales_2011_12 fact_sales_13  (cost=0.29..4.30 rows=1 width=0) (actual time=0.405..0.405 rows=0.00 loops=1)
              Index Cond: (date_key = 100)
              Heap Fetches: 0
              Index Searches: 1
              Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.021..0.022 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_date_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.005..0.005 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=43
Planning Time: 0.901 ms
Execution Time: 7.173 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11621.98..11621.99 rows=1 width=8) (actual time=83.574..110.300 rows=1.00 loops=1)
  Buffers: shared hit=6677
  ->  Gather  (cost=11621.77..11621.98 rows=2 width=8) (actual time=78.785..110.285 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6677
        ->  Partial Aggregate  (cost=10621.77..10621.78 rows=1 width=8) (actual time=25.919..25.921 rows=1.00 loops=3)
              Buffers: shared hit=6677
              ->  Parallel Append  (cost=0.00..10620.62 rows=460 width=0) (actual time=2.128..25.890 rows=357.67 loops=3)
                    Buffers: shared hit=6677
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=1 width=0) (actual time=9.039..9.039 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 83077
                          Buffers: shared hit=1037
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=1 width=0) (actual time=8.213..8.213 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=741
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=1 width=0) (actual time=7.428..7.429 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=618
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=1 width=0) (actual time=7.316..7.316 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=527
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=1 width=0) (actual time=6.174..6.174 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 39079
                          Buffers: shared hit=490
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=1 width=0) (actual time=5.033..5.033 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=456
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=1 width=0) (actual time=7.691..7.692 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36425
                          Buffers: shared hit=455
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=1 width=0) (actual time=5.756..5.757 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=452
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=1 width=0) (actual time=6.069..6.069 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 34760
                          Buffers: shared hit=438
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=1 width=0) (actual time=4.788..4.789 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=435
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=631 width=0) (actual time=0.006..3.671 rows=1073.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 28367
                          Buffers: shared hit=368
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=1 width=0) (actual time=3.046..3.047 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=343
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.24 rows=1 width=0) (actual time=3.318..3.318 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=317
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=2 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                          Filter: (date_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 0.578 ms
Execution Time: 110.416 ms
```

## Monthly revenue by country, from the fact table

With indexes:
```
HashAggregate  (cost=21223.12..21923.12 rows=40000 width=50) (actual time=582.067..582.272 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Batches: 1  Memory Usage: 673kB
  Buffers: shared hit=6677
  ->  Append  (cost=0.00..17284.75 rows=525116 width=24) (actual time=0.028..314.183 rows=524878.00 loops=1)
        Buffers: shared hit=6677
        ->  Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..1148.91 rows=40963 width=24) (actual time=0.027..15.471 rows=40991.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 719
              Buffers: shared hit=527
        ->  Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..955.88 rows=34057 width=24) (actual time=0.034..16.935 rows=34060.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 700
              Buffers: shared hit=438
        ->  Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..750.93 rows=26882 width=24) (actual time=0.038..12.303 rows=26882.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 470
              Buffers: shared hit=343
        ->  Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..991.50 rows=35513 width=24) (actual time=0.036..17.313 rows=35497.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 696
              Buffers: shared hit=452
        ->  Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..806.81 rows=28882 width=24) (actual time=0.031..13.830 rows=28882.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 558
              Buffers: shared hit=368
        ->  Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..1001.03 rows=35931 width=24) (actual time=0.035..20.515 rows=35917.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 621
              Buffers: shared hit=456
        ->  Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..997.80 rows=35709 width=24) (actual time=0.035..16.428 rows=35716.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 709
              Buffers: shared hit=455
        ->  Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..1072.78 rows=38398 width=24) (actual time=0.034..18.509 rows=38395.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 684
              Buffers: shared hit=490
        ->  Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..955.63 rows=34264 width=24) (actual time=0.034..13.651 rows=34264.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 667
              Buffers: shared hit=435
        ->  Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1359.42 rows=48883 width=24) (actual time=0.049..24.871 rows=48900.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 801
              Buffers: shared hit=618
        ->  Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1631.20 rows=58578 width=24) (actual time=0.056..32.425 rows=58537.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 1194
              Buffers: shared hit=741
        ->  Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..2277.56 rows=81958 width=24) (actual time=0.050..51.971 rows=82004.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 1073
              Buffers: shared hit=1037
        ->  Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..693.09 rows=24833 width=24) (actual time=0.048..12.839 rows=24833.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 359
              Buffers: shared hit=317
        ->  Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..16.62 rows=265 width=24) (actual time=0.037..0.037 rows=0.00 loops=1)
              Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 0.722 ms
Execution Time: 582.749 ms
```

Index scans turned off:
```
HashAggregate  (cost=21223.12..21923.12 rows=40000 width=50) (actual time=753.373..753.644 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Batches: 1  Memory Usage: 673kB
  Buffers: shared hit=6677
  ->  Append  (cost=0.00..17284.75 rows=525116 width=24) (actual time=0.032..415.071 rows=524878.00 loops=1)
        Buffers: shared hit=6677
        ->  Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..1148.91 rows=40963 width=24) (actual time=0.031..18.014 rows=40991.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 719
              Buffers: shared hit=527
        ->  Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..955.88 rows=34057 width=24) (actual time=0.037..26.663 rows=34060.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 700
              Buffers: shared hit=438
        ->  Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..750.93 rows=26882 width=24) (actual time=0.067..19.049 rows=26882.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 470
              Buffers: shared hit=343
        ->  Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..991.50 rows=35513 width=24) (actual time=0.065..24.764 rows=35497.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 696
              Buffers: shared hit=452
        ->  Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..806.81 rows=28882 width=24) (actual time=0.049..20.915 rows=28882.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 558
              Buffers: shared hit=368
        ->  Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..1001.03 rows=35931 width=24) (actual time=0.053..22.621 rows=35917.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 621
              Buffers: shared hit=456
        ->  Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..997.80 rows=35709 width=24) (actual time=0.049..25.571 rows=35716.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 709
              Buffers: shared hit=455
        ->  Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..1072.78 rows=38398 width=24) (actual time=0.072..25.016 rows=38395.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 684
              Buffers: shared hit=490
        ->  Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..955.63 rows=34264 width=24) (actual time=0.060..18.900 rows=34264.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 667
              Buffers: shared hit=435
        ->  Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..1359.42 rows=48883 width=24) (actual time=0.065..34.239 rows=48900.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 801
              Buffers: shared hit=618
        ->  Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1631.20 rows=58578 width=24) (actual time=0.069..40.853 rows=58537.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 1194
              Buffers: shared hit=741
        ->  Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..2277.56 rows=81958 width=24) (actual time=0.046..62.670 rows=82004.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 1073
              Buffers: shared hit=1037
        ->  Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..693.09 rows=24833 width=24) (actual time=0.054..14.799 rows=24833.00 loops=1)
              Filter: (NOT is_cancelled)
              Rows Removed by Filter: 359
              Buffers: shared hit=317
        ->  Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..16.62 rows=265 width=24) (actual time=0.050..0.050 rows=0.00 loops=1)
              Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 0.773 ms
Execution Time: 754.158 ms
```

## Monthly revenue by country, from the materialized view

With indexes:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.039..0.100 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning:
  Buffers: shared hit=7 read=1
Planning Time: 1.367 ms
Execution Time: 0.124 ms
```

Index scans turned off:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.027..0.090 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning Time: 0.106 ms
Execution Time: 0.108 ms
```
