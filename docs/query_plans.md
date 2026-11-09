# Query plans

Generated 2026-11-09 10:32:12 by `scripts/performance.py`.

Each query is run twice: with index scans allowed, and with index scans turned off. The second run shows what the planner does without the indexes.

## Revenue by product category

With indexes:
```
Finalize GroupAggregate  (cost=12338.46..12400.46 rows=200 width=64) (actual time=287.295..309.877 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=6767 read=37
  ->  Gather Merge  (cost=12338.46..12394.36 rows=480 width=64) (actual time=287.280..309.855 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6767 read=37
        ->  Sort  (cost=11338.43..11338.93 rows=200 width=64) (actual time=228.029..228.035 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=6767 read=37
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=11328.29..11330.79 rows=200 width=64) (actual time=227.964..227.973 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=6751 read=37
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=89.45..10771.35 rows=111387 width=48) (actual time=2.225..150.591 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=6751 read=37
                          ->  Parallel Append  (cost=0.00..10388.98 rows=111386 width=20) (actual time=0.025..79.471 rows=174959.33 loops=3)
                                Buffers: shared hit=6677
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=24434 width=20) (actual time=0.025..31.858 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1037
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=17568 width=20) (actual time=0.026..24.293 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=741
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=14618 width=20) (actual time=0.008..20.899 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=618
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=12268 width=20) (actual time=0.008..17.835 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=527
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=11494 width=20) (actual time=0.012..5.755 rows=12798.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 228
                                      Buffers: shared hit=490
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=10746 width=20) (actual time=0.013..6.641 rows=17958.50 loops=2)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 310
                                      Buffers: shared hit=456
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=10713 width=20) (actual time=0.013..8.896 rows=35716.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 709
                                      Buffers: shared hit=455
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=10645 width=20) (actual time=0.005..9.820 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=452
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=10224 width=20) (actual time=0.007..9.512 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=438
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=10274 width=20) (actual time=0.008..9.964 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=435
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=8659 width=20) (actual time=0.007..9.420 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=368
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=8045 width=20) (actual time=0.008..8.614 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=343
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=7409 width=20) (actual time=0.013..9.046 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=317
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=156 width=20) (actual time=0.003..0.004 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=60.31..60.31 rows=2331 width=36) (actual time=2.172..2.173 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=74 read=37
                                ->  Seq Scan on dim_product p  (cost=0.00..60.31 rows=2331 width=36) (actual time=0.338..1.332 rows=3828.00 loops=3)
                                      Buffers: shared hit=74 read=37
Planning:
  Buffers: shared hit=142 read=2
Planning Time: 1.710 ms
Execution Time: 310.095 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=12338.46..12400.46 rows=200 width=64) (actual time=298.783..333.667 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=6804
  ->  Gather Merge  (cost=12338.46..12394.36 rows=480 width=64) (actual time=298.766..333.647 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6804
        ->  Sort  (cost=11338.43..11338.93 rows=200 width=64) (actual time=244.601..244.612 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=6804
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=11328.29..11330.79 rows=200 width=64) (actual time=244.548..244.561 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=6788
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=89.45..10771.35 rows=111387 width=48) (actual time=1.859..161.944 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=6788
                          ->  Parallel Append  (cost=0.00..10388.98 rows=111386 width=20) (actual time=0.022..85.651 rows=174959.33 loops=3)
                                Buffers: shared hit=6677
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=24434 width=20) (actual time=0.019..30.505 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1037
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=17568 width=20) (actual time=0.017..23.869 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=741
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=14618 width=20) (actual time=0.010..23.193 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=618
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=12268 width=20) (actual time=0.010..19.443 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=527
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=11494 width=20) (actual time=0.011..5.989 rows=12798.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 228
                                      Buffers: shared hit=490
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=10746 width=20) (actual time=0.018..7.180 rows=17958.50 loops=2)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 310
                                      Buffers: shared hit=456
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=10713 width=20) (actual time=0.006..14.317 rows=35716.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 709
                                      Buffers: shared hit=455
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=10645 width=20) (actual time=0.005..9.801 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=452
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=10224 width=20) (actual time=0.006..8.610 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=438
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=10274 width=20) (actual time=0.008..9.403 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=435
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=8659 width=20) (actual time=0.008..12.989 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=368
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=8045 width=20) (actual time=0.009..10.443 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=343
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=7409 width=20) (actual time=0.018..11.459 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=317
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=156 width=20) (actual time=0.005..0.005 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=60.31..60.31 rows=2331 width=36) (actual time=1.809..1.810 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=111
                                ->  Seq Scan on dim_product p  (cost=0.00..60.31 rows=2331 width=36) (actual time=0.208..0.984 rows=3828.00 loops=3)
                                      Buffers: shared hit=111
Planning:
  Buffers: shared hit=4
Planning Time: 1.216 ms
Execution Time: 333.849 ms
```

## Top 10 customers by revenue

With indexes:
```
Limit  (cost=15143.67..15143.69 rows=10 width=36) (actual time=270.413..290.354 rows=10.00 loops=1)
  Buffers: shared hit=6720 read=20
  ->  Sort  (cost=15143.67..15154.97 rows=4520 width=36) (actual time=270.411..290.351 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6720 read=20
        ->  Finalize HashAggregate  (cost=14989.49..15045.99 rows=4520 width=36) (actual time=267.928..289.545 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6717 read=20
              ->  Gather  (cost=13766.83..14908.13 rows=10848 width=36) (actual time=255.884..279.595 rows=8111.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6717 read=20
                    ->  Partial HashAggregate  (cost=12766.83..12823.33 rows=4520 width=36) (actual time=203.870..205.900 rows=2703.67 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6717 read=20
                          Worker 0:  Batches: 1  Memory Usage: 1041kB
                          Worker 1:  Batches: 1  Memory Usage: 1297kB
                          ->  Hash Join  (cost=121.70..11652.96 rows=222775 width=20) (actual time=3.035..140.217 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6717 read=20
                                ->  Parallel Append  (cost=0.00..10945.93 rows=222775 width=20) (actual time=0.025..78.343 rows=178043.00 loops=3)
                                      Buffers: shared hit=6677
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=48869 width=20) (actual time=0.026..38.726 rows=83077.00 loops=1)
                                            Buffers: shared hit=1037
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=35136 width=20) (actual time=0.027..18.997 rows=59731.00 loops=1)
                                            Buffers: shared hit=741
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=29236 width=20) (actual time=0.009..17.061 rows=49701.00 loops=1)
                                            Buffers: shared hit=618
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=24535 width=20) (actual time=0.013..13.267 rows=41710.00 loops=1)
                                            Buffers: shared hit=527
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=22988 width=20) (actual time=0.013..12.998 rows=39079.00 loops=1)
                                            Buffers: shared hit=490
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=21493 width=20) (actual time=0.010..3.835 rows=12179.33 loops=3)
                                            Buffers: shared hit=456
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=21426 width=20) (actual time=0.008..8.244 rows=36425.00 loops=1)
                                            Buffers: shared hit=455
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=21290 width=20) (actual time=0.006..7.642 rows=36193.00 loops=1)
                                            Buffers: shared hit=452
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=20447 width=20) (actual time=0.007..9.383 rows=34760.00 loops=1)
                                            Buffers: shared hit=438
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=20548 width=20) (actual time=0.007..10.606 rows=34931.00 loops=1)
                                            Buffers: shared hit=435
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=17318 width=20) (actual time=0.007..14.995 rows=29440.00 loops=1)
                                            Buffers: shared hit=368
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=16089 width=20) (actual time=0.012..8.866 rows=27352.00 loops=1)
                                            Buffers: shared hit=343
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=14819 width=20) (actual time=0.012..8.615 rows=25192.00 loops=1)
                                            Buffers: shared hit=317
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=312 width=20) (actual time=0.003..0.003 rows=0.00 loops=1)
                                ->  Hash  (cost=65.20..65.20 rows=4520 width=8) (actual time=2.958..2.959 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=40 read=20
                                      ->  Seq Scan on dim_customer c  (cost=0.00..65.20 rows=4520 width=8) (actual time=0.362..1.556 rows=4371.00 loops=3)
                                            Buffers: shared hit=40 read=20
Planning:
  Buffers: shared hit=83 read=2
Planning Time: 2.016 ms
Execution Time: 291.741 ms
```

Index scans turned off:
```
Limit  (cost=15143.67..15143.69 rows=10 width=36) (actual time=254.281..275.196 rows=10.00 loops=1)
  Buffers: shared hit=6737
  ->  Sort  (cost=15143.67..15154.97 rows=4520 width=36) (actual time=254.279..275.193 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6737
        ->  Finalize HashAggregate  (cost=14989.49..15045.99 rows=4520 width=36) (actual time=250.688..274.008 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6737
              ->  Gather  (cost=13766.83..14908.13 rows=10848 width=36) (actual time=240.076..265.053 rows=8105.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6737
                    ->  Partial HashAggregate  (cost=12766.83..12823.33 rows=4520 width=36) (actual time=181.079..182.953 rows=2701.67 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6737
                          Worker 0:  Batches: 1  Memory Usage: 1297kB
                          Worker 1:  Batches: 1  Memory Usage: 1041kB
                          ->  Hash Join  (cost=121.70..11652.96 rows=222775 width=20) (actual time=1.962..124.771 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6737
                                ->  Parallel Append  (cost=0.00..10945.93 rows=222775 width=20) (actual time=0.021..70.254 rows=178043.00 loops=3)
                                      Buffers: shared hit=6677
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=48869 width=20) (actual time=0.022..25.136 rows=83077.00 loops=1)
                                            Buffers: shared hit=1037
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=35136 width=20) (actual time=0.017..19.949 rows=59731.00 loops=1)
                                            Buffers: shared hit=741
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=29236 width=20) (actual time=0.012..14.415 rows=49701.00 loops=1)
                                            Buffers: shared hit=618
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=24535 width=20) (actual time=0.013..15.936 rows=41710.00 loops=1)
                                            Buffers: shared hit=527
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=22988 width=20) (actual time=0.008..10.947 rows=39079.00 loops=1)
                                            Buffers: shared hit=490
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=21493 width=20) (actual time=0.011..3.785 rows=12179.33 loops=3)
                                            Buffers: shared hit=456
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=21426 width=20) (actual time=0.005..11.603 rows=36425.00 loops=1)
                                            Buffers: shared hit=455
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=21290 width=20) (actual time=0.006..7.146 rows=36193.00 loops=1)
                                            Buffers: shared hit=452
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=20447 width=20) (actual time=0.008..7.573 rows=34760.00 loops=1)
                                            Buffers: shared hit=438
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=20548 width=20) (actual time=0.006..8.917 rows=34931.00 loops=1)
                                            Buffers: shared hit=435
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=17318 width=20) (actual time=0.007..10.274 rows=29440.00 loops=1)
                                            Buffers: shared hit=368
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=16089 width=20) (actual time=0.008..9.074 rows=27352.00 loops=1)
                                            Buffers: shared hit=343
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=14819 width=20) (actual time=0.014..8.138 rows=25192.00 loops=1)
                                            Buffers: shared hit=317
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=312 width=20) (actual time=0.003..0.003 rows=0.00 loops=1)
                                ->  Hash  (cost=65.20..65.20 rows=4520 width=8) (actual time=1.898..1.898 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..65.20 rows=4520 width=8) (actual time=0.237..0.966 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=4
Planning Time: 0.825 ms
Execution Time: 275.801 ms
```

## One month of sales (June 2011)

With indexes:
```
Aggregate  (cost=1001.83..1001.84 rows=1 width=32) (actual time=10.548..10.548 rows=1.00 loops=1)
  Buffers: shared hit=455
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1001.38 rows=182 width=16) (actual time=0.016..6.766 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=455
Planning:
  Buffers: shared hit=38
Planning Time: 0.231 ms
Execution Time: 10.571 ms
```

Index scans turned off:
```
Aggregate  (cost=1001.83..1001.84 rows=1 width=32) (actual time=16.649..16.651 rows=1.00 loops=1)
  Buffers: shared hit=455
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1001.38 rows=182 width=16) (actual time=0.015..10.567 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=455
Planning Time: 0.168 ms
Execution Time: 16.678 ms
```

## One customer's orders (point lookup)

With indexes:
```
Aggregate  (cost=5199.16..5199.17 rows=1 width=8) (actual time=1.577..1.589 rows=1.00 loops=1)
  Buffers: shared hit=7 read=26
  ->  Append  (cost=5.91..5192.47 rows=2675 width=0) (actual time=0.314..1.574 rows=40.00 loops=1)
        Buffers: shared hit=7 read=26
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..405.99 rows=209 width=0) (actual time=0.193..0.194 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_customer_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.164..0.165 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..338.93 rows=174 width=0) (actual time=0.119..0.122 rows=12.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=2
              Buffers: shared hit=2 read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_customer_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.097..0.097 rows=12.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..267.30 rows=137 width=0) (actual time=0.115..0.116 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_customer_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.100..0.100 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..350.13 rows=181 width=0) (actual time=0.104..0.105 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_customer_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.089..0.089 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..285.93 rows=147 width=0) (actual time=0.108..0.108 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_04_customer_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.094..0.095 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..354.12 rows=183 width=0) (actual time=0.100..0.101 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_customer_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.087..0.087 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..352.41 rows=182 width=0) (actual time=0.125..0.131 rows=26.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=2
              Buffers: shared hit=2 read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_customer_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.103..0.104 rows=26.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..378.20 rows=195 width=0) (actual time=0.110..0.111 rows=2.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=1
              Buffers: shared hit=1 read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_customer_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.094..0.094 rows=2.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..338.08 rows=175 width=0) (actual time=0.102..0.102 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_customer_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.088..0.088 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..479.32 rows=249 width=0) (actual time=0.107..0.108 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_customer_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.092..0.092 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..573.32 rows=299 width=0) (actual time=0.118..0.118 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_customer_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.101..0.102 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..797.12 rows=415 width=0) (actual time=0.107..0.107 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_customer_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.091..0.091 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..246.95 rows=126 width=0) (actual time=0.115..0.116 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_customer_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.098..0.098 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.016..0.016 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_customer_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.004..0.004 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=9 read=1
Planning Time: 1.188 ms
Execution Time: 1.959 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11626.88..11626.89 rows=1 width=8) (actual time=94.254..117.173 rows=1.00 loops=1)
  Buffers: shared hit=6677
  ->  Gather  (cost=11626.66..11626.87 rows=2 width=8) (actual time=93.879..117.163 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6677
        ->  Partial Aggregate  (cost=10626.66..10626.67 rows=1 width=8) (actual time=38.075..38.079 rows=1.00 loops=3)
              Buffers: shared hit=6677
              ->  Parallel Append  (cost=0.00..10623.88 rows=1113 width=0) (actual time=18.899..38.069 rows=13.33 loops=3)
                    Buffers: shared hit=6677
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=244 width=0) (actual time=16.501..16.502 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 83077
                          Buffers: shared hit=1037
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=176 width=0) (actual time=4.036..4.036 rows=0.00 loops=3)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 19910
                          Buffers: shared hit=741
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=146 width=0) (actual time=11.432..11.432 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=618
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=123 width=0) (actual time=9.798..9.798 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=527
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=115 width=0) (actual time=8.392..8.444 rows=2.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 39077
                          Buffers: shared hit=490
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=108 width=0) (actual time=7.329..7.329 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=456
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=107 width=0) (actual time=0.010..6.246 rows=26.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36399
                          Buffers: shared hit=455
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=106 width=0) (actual time=7.047..7.048 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=452
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=102 width=0) (actual time=6.000..6.855 rows=12.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34748
                          Buffers: shared hit=438
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=103 width=0) (actual time=7.490..7.491 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=435
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=86 width=0) (actual time=7.692..7.692 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 29440
                          Buffers: shared hit=368
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=81 width=0) (actual time=7.177..7.177 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=343
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.24 rows=74 width=0) (actual time=6.001..6.001 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=317
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=2 width=0) (actual time=0.006..0.006 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 1.021 ms
Execution Time: 117.294 ms
```

## One product's sales (point lookup)

With indexes:
```
Aggregate  (cost=5199.16..5199.17 rows=1 width=8) (actual time=1.326..1.334 rows=1.00 loops=1)
  Buffers: shared hit=72 read=26
  ->  Append  (cost=5.91..5192.47 rows=2675 width=0) (actual time=0.218..1.321 rows=71.00 loops=1)
        Buffers: shared hit=72 read=26
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..405.99 rows=209 width=0) (actual time=0.217..0.253 rows=30.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=30
              Buffers: shared hit=30 read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_product_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.189..0.190 rows=30.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..338.93 rows=174 width=0) (actual time=0.106..0.130 rows=21.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=20
              Buffers: shared hit=20 read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_product_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.089..0.089 rows=21.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..267.30 rows=137 width=0) (actual time=0.095..0.103 rows=7.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=7
              Buffers: shared hit=7 read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_product_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.078..0.079 rows=7.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..350.13 rows=181 width=0) (actual time=0.110..0.119 rows=8.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=8
              Buffers: shared hit=8 read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_product_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.092..0.092 rows=8.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..285.93 rows=147 width=0) (actual time=0.088..0.093 rows=5.00 loops=1)
              Recheck Cond: (product_key = 1)
              Heap Blocks: exact=5
              Buffers: shared hit=5 read=2
              ->  Bitmap Index Scan on fact_sales_2011_04_product_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.076..0.077 rows=5.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..354.12 rows=183 width=0) (actual time=0.079..0.079 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_product_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.068..0.068 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..352.41 rows=182 width=0) (actual time=0.076..0.077 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_product_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.063..0.064 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..378.20 rows=195 width=0) (actual time=0.073..0.074 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_product_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.064..0.064 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..338.08 rows=175 width=0) (actual time=0.075..0.076 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_product_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.065..0.065 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..479.32 rows=249 width=0) (actual time=0.072..0.073 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_product_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.061..0.062 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..573.32 rows=299 width=0) (actual time=0.073..0.073 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_product_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.062..0.063 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..797.12 rows=415 width=0) (actual time=0.075..0.076 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_product_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.065..0.065 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..246.95 rows=126 width=0) (actual time=0.071..0.071 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_product_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.061..0.061 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.010..0.011 rows=0.00 loops=1)
              Recheck Cond: (product_key = 1)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_product_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                    Index Cond: (product_key = 1)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=4
Planning Time: 0.964 ms
Execution Time: 1.604 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11626.88..11626.89 rows=1 width=8) (actual time=79.947..101.542 rows=1.00 loops=1)
  Buffers: shared hit=6677
  ->  Gather  (cost=11626.66..11626.87 rows=2 width=8) (actual time=79.383..101.498 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6677
        ->  Partial Aggregate  (cost=10626.66..10626.67 rows=1 width=8) (actual time=32.220..32.224 rows=1.00 loops=3)
              Buffers: shared hit=6677
              ->  Parallel Append  (cost=0.00..10623.88 rows=1113 width=0) (actual time=7.685..32.191 rows=23.67 loops=3)
                    Buffers: shared hit=6677
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=244 width=0) (actual time=12.867..12.867 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 83077
                          Buffers: shared hit=1037
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=176 width=0) (actual time=4.294..4.295 rows=0.00 loops=3)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 19910
                          Buffers: shared hit=741
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=146 width=0) (actual time=9.709..9.709 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=618
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=123 width=0) (actual time=0.029..6.548 rows=30.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 41680
                          Buffers: shared hit=527
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=115 width=0) (actual time=7.109..7.109 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 39079
                          Buffers: shared hit=490
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=108 width=0) (actual time=6.572..6.573 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=456
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=107 width=0) (actual time=6.932..6.932 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36425
                          Buffers: shared hit=455
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=106 width=0) (actual time=0.174..7.392 rows=8.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 36185
                          Buffers: shared hit=452
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=102 width=0) (actual time=0.399..6.270 rows=21.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 34739
                          Buffers: shared hit=438
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=103 width=0) (actual time=5.735..5.735 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=435
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=86 width=0) (actual time=0.070..5.497 rows=5.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 29435
                          Buffers: shared hit=368
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=81 width=0) (actual time=0.848..5.298 rows=7.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 27345
                          Buffers: shared hit=343
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.24 rows=74 width=0) (actual time=3.676..3.676 rows=0.00 loops=1)
                          Filter: (product_key = 1)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=317
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=2 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                          Filter: (product_key = 1)
Planning:
  Buffers: shared hit=4
Planning Time: 0.703 ms
Execution Time: 101.664 ms
```

## One day's sales (point lookup)

With indexes:
```
Aggregate  (cost=5199.16..5199.17 rows=1 width=8) (actual time=2.133..2.140 rows=1.00 loops=1)
  Buffers: shared hit=18 read=27
  ->  Append  (cost=5.91..5192.47 rows=2675 width=0) (actual time=1.410..2.079 rows=1073.00 loops=1)
        Buffers: shared hit=18 read=27
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..405.99 rows=209 width=0) (actual time=0.397..0.398 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_date_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.373..0.373 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..338.93 rows=174 width=0) (actual time=0.340..0.340 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_date_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.325..0.325 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..267.30 rows=137 width=0) (actual time=0.219..0.220 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_date_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.205..0.205 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..350.13 rows=181 width=0) (actual time=0.328..0.328 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_date_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.316..0.316 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..285.93 rows=147 width=0) (actual time=0.122..0.220 rows=1073.00 loops=1)
              Recheck Cond: (date_key = 100)
              Heap Blocks: exact=16
              Buffers: shared hit=16 read=3
              ->  Bitmap Index Scan on fact_sales_2011_04_date_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.105..0.105 rows=1073.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=3
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..354.12 rows=183 width=0) (actual time=0.065..0.065 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_date_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.055..0.055 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..352.41 rows=182 width=0) (actual time=0.063..0.063 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_date_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.051..0.051 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..378.20 rows=195 width=0) (actual time=0.069..0.069 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_date_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.061..0.061 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..338.08 rows=175 width=0) (actual time=0.056..0.056 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_date_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.048..0.048 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..479.32 rows=249 width=0) (actual time=0.059..0.060 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_date_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.051..0.051 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..573.32 rows=299 width=0) (actual time=0.064..0.064 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_date_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.055..0.056 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..797.12 rows=415 width=0) (actual time=0.057..0.057 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_date_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.049..0.049 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..246.95 rows=126 width=0) (actual time=0.058..0.058 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_date_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.050..0.050 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.009..0.009 rows=0.00 loops=1)
              Recheck Cond: (date_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_date_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                    Index Cond: (date_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=30
Planning Time: 0.676 ms
Execution Time: 2.332 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11626.88..11626.89 rows=1 width=8) (actual time=76.904..86.676 rows=1.00 loops=1)
  Buffers: shared hit=6677
  ->  Gather  (cost=11626.66..11626.87 rows=2 width=8) (actual time=76.396..86.667 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6677
        ->  Partial Aggregate  (cost=10626.66..10626.67 rows=1 width=8) (actual time=28.534..28.537 rows=1.00 loops=3)
              Buffers: shared hit=6677
              ->  Parallel Append  (cost=0.00..10623.88 rows=1113 width=0) (actual time=5.655..28.506 rows=357.67 loops=3)
                    Buffers: shared hit=6677
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=244 width=0) (actual time=4.930..4.930 rows=0.00 loops=3)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1037
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=176 width=0) (actual time=10.151..10.151 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 59731
                          Buffers: shared hit=741
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=146 width=0) (actual time=7.991..7.991 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=618
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=123 width=0) (actual time=5.738..5.739 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=527
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=115 width=0) (actual time=6.585..6.585 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 39079
                          Buffers: shared hit=490
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=108 width=0) (actual time=6.359..6.359 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=456
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=107 width=0) (actual time=6.134..6.134 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36425
                          Buffers: shared hit=455
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=106 width=0) (actual time=7.050..7.050 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=452
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=102 width=0) (actual time=5.570..5.570 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 34760
                          Buffers: shared hit=438
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=103 width=0) (actual time=4.687..4.687 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=435
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=86 width=0) (actual time=0.005..3.589 rows=1073.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 28367
                          Buffers: shared hit=368
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=81 width=0) (actual time=3.475..3.475 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=343
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.24 rows=74 width=0) (actual time=3.264..3.264 rows=0.00 loops=1)
                          Filter: (date_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=317
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=2 width=0) (actual time=0.003..0.003 rows=0.00 loops=1)
                          Filter: (date_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 0.562 ms
Execution Time: 86.755 ms
```

## Monthly revenue by country, from the fact table

With indexes:
```
Finalize GroupAggregate  (cost=25320.32..39873.57 rows=39996 width=68) (actual time=300.129..370.912 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Buffers: shared hit=6771, temp read=2260 written=2267
  ->  Gather Merge  (cost=25320.32..38213.74 rows=95990 width=68) (actual time=300.113..370.551 rows=332.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6771, temp read=2260 written=2267
        ->  Partial GroupAggregate  (cost=24320.30..26134.09 rows=39996 width=68) (actual time=180.837..245.080 rows=110.67 loops=3)
              Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
              Buffers: shared hit=6771, temp read=2260 written=2267
              ->  Sort  (cost=24320.30..24598.76 rows=111386 width=52) (actual time=180.770..205.868 rows=174959.33 loops=3)
                    Sort Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
                    Sort Method: external merge  Disk: 6792kB
                    Buffers: shared hit=6771, temp read=2260 written=2267
                    Worker 0:  Sort Method: external merge  Disk: 5760kB
                    Worker 1:  Sort Method: external merge  Disk: 5528kB
                    ->  Parallel Append  (cost=0.00..11175.25 rows=111386 width=52) (actual time=0.023..103.311 rows=174959.33 loops=3)
                          Buffers: shared hit=6677
                          ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=24434 width=52) (actual time=0.024..35.015 rows=82004.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1073
                                Buffers: shared hit=1037
                          ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=17568 width=52) (actual time=0.020..28.173 rows=58537.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1194
                                Buffers: shared hit=741
                          ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=14618 width=52) (actual time=0.010..22.557 rows=48900.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 801
                                Buffers: shared hit=618
                          ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=12268 width=52) (actual time=0.009..18.874 rows=40991.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 719
                                Buffers: shared hit=527
                          ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=11494 width=52) (actual time=0.009..14.632 rows=38395.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 684
                                Buffers: shared hit=490
                          ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=10746 width=52) (actual time=0.016..20.270 rows=35917.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 621
                                Buffers: shared hit=456
                          ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=10713 width=52) (actual time=0.010..6.857 rows=11905.33 loops=3)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 236
                                Buffers: shared hit=455
                          ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=10645 width=52) (actual time=0.008..20.523 rows=35497.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 696
                                Buffers: shared hit=452
                          ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=10224 width=52) (actual time=0.007..19.010 rows=34060.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 700
                                Buffers: shared hit=438
                          ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=10274 width=52) (actual time=0.006..17.377 rows=34264.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 667
                                Buffers: shared hit=435
                          ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=8659 width=52) (actual time=0.007..15.737 rows=28882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 558
                                Buffers: shared hit=368
                          ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=8045 width=52) (actual time=0.010..15.789 rows=26882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 470
                                Buffers: shared hit=343
                          ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.23 rows=7409 width=52) (actual time=0.015..18.062 rows=24833.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 359
                                Buffers: shared hit=317
                          ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=156 width=52) (actual time=0.003..0.003 rows=0.00 loops=1)
                                Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 1.007 ms
Execution Time: 372.901 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=25320.32..39873.57 rows=39996 width=68) (actual time=361.849..594.661 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Buffers: shared hit=6771, temp read=2262 written=2269
  ->  Gather Merge  (cost=25320.32..38213.74 rows=95990 width=68) (actual time=361.826..593.712 rows=332.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6771, temp read=2262 written=2269
        ->  Partial GroupAggregate  (cost=24320.30..26134.09 rows=39996 width=68) (actual time=189.861..310.407 rows=110.67 loops=3)
              Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
              Buffers: shared hit=6771, temp read=2262 written=2269
              ->  Sort  (cost=24320.30..24598.76 rows=111386 width=52) (actual time=189.775..235.196 rows=174959.33 loops=3)
                    Sort Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
                    Sort Method: external merge  Disk: 9400kB
                    Buffers: shared hit=6771, temp read=2262 written=2269
                    Worker 0:  Sort Method: external merge  Disk: 2064kB
                    Worker 1:  Sort Method: external merge  Disk: 6632kB
                    ->  Parallel Append  (cost=0.00..11175.25 rows=111386 width=52) (actual time=0.023..106.726 rows=174959.33 loops=3)
                          Buffers: shared hit=6677
                          ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=24434 width=52) (actual time=0.020..33.637 rows=82004.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1073
                                Buffers: shared hit=1037
                          ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=17568 width=52) (actual time=0.009..24.518 rows=58537.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1194
                                Buffers: shared hit=741
                          ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=14618 width=52) (actual time=0.029..37.804 rows=48900.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 801
                                Buffers: shared hit=618
                          ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=12268 width=52) (actual time=0.010..31.020 rows=40991.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 719
                                Buffers: shared hit=527
                          ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=11494 width=52) (actual time=0.014..10.099 rows=12798.33 loops=3)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 228
                                Buffers: shared hit=490
                          ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=10746 width=52) (actual time=0.006..23.979 rows=35917.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 621
                                Buffers: shared hit=456
                          ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=10713 width=52) (actual time=0.006..15.431 rows=35716.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 709
                                Buffers: shared hit=455
                          ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=10645 width=52) (actual time=0.005..13.270 rows=35497.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 696
                                Buffers: shared hit=452
                          ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=10224 width=52) (actual time=0.006..10.606 rows=34060.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 700
                                Buffers: shared hit=438
                          ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=10274 width=52) (actual time=0.008..16.053 rows=34264.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 667
                                Buffers: shared hit=435
                          ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=8659 width=52) (actual time=0.006..12.421 rows=28882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 558
                                Buffers: shared hit=368
                          ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=8045 width=52) (actual time=0.010..11.425 rows=26882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 470
                                Buffers: shared hit=343
                          ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.23 rows=7409 width=52) (actual time=0.010..15.228 rows=24833.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 359
                                Buffers: shared hit=317
                          ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=156 width=52) (actual time=0.003..0.003 rows=0.00 loops=1)
                                Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 0.606 ms
Execution Time: 597.693 ms
```

## Monthly revenue by country, from the materialized view

With indexes:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.030..0.082 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning:
  Buffers: shared hit=7 read=1
Planning Time: 1.022 ms
Execution Time: 0.101 ms
```

Index scans turned off:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.019..0.046 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning Time: 0.095 ms
Execution Time: 0.061 ms
```
