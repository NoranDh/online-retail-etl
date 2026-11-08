# Query plans

Generated 2026-11-08 20:41:09 by `scripts/performance.py`.

Each query is run twice: with index scans allowed, and with index scans turned off. The second run shows what the planner does without the indexes.

## Revenue by product category

With indexes:
```
Finalize GroupAggregate  (cost=12338.46..12400.46 rows=200 width=64) (actual time=640.399..661.825 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=6803 read=1
  ->  Gather Merge  (cost=12338.46..12394.36 rows=480 width=64) (actual time=640.382..661.799 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6803 read=1
        ->  Sort  (cost=11338.43..11338.93 rows=200 width=64) (actual time=513.441..513.448 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=6803 read=1
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=11328.29..11330.79 rows=200 width=64) (actual time=513.037..513.048 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=6787 read=1
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=89.45..10771.35 rows=111387 width=48) (actual time=3.235..355.002 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=6787 read=1
                          ->  Parallel Append  (cost=0.00..10388.98 rows=111386 width=20) (actual time=0.025..150.735 rows=174959.33 loops=3)
                                Buffers: shared hit=6677
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=24434 width=20) (actual time=0.020..61.479 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1037
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=17568 width=20) (actual time=0.023..35.966 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=741
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=14618 width=20) (actual time=0.013..47.210 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=618
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=12268 width=20) (actual time=0.029..34.018 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=527
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=11494 width=20) (actual time=0.022..12.671 rows=12798.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 228
                                      Buffers: shared hit=490
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=10746 width=20) (actual time=0.028..12.228 rows=17958.50 loops=2)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 310
                                      Buffers: shared hit=456
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=10713 width=20) (actual time=0.008..20.739 rows=35716.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 709
                                      Buffers: shared hit=455
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=10645 width=20) (actual time=0.012..26.609 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=452
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=10224 width=20) (actual time=0.009..19.388 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=438
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=10274 width=20) (actual time=0.008..28.650 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=435
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=8659 width=20) (actual time=0.008..15.828 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=368
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=8045 width=20) (actual time=0.009..18.073 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=343
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=7409 width=20) (actual time=0.018..10.946 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=317
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=156 width=20) (actual time=0.004..0.005 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=60.31..60.31 rows=2331 width=36) (actual time=3.179..3.180 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=110 read=1
                                ->  Seq Scan on dim_product p  (cost=0.00..60.31 rows=2331 width=36) (actual time=0.381..1.769 rows=3828.00 loops=3)
                                      Buffers: shared hit=110 read=1
Planning:
  Buffers: shared hit=144
Planning Time: 3.608 ms
Execution Time: 662.107 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=12338.46..12400.46 rows=200 width=64) (actual time=539.572..564.131 rows=4.00 loops=1)
  Group Key: p.category
  Buffers: shared hit=6804
  ->  Gather Merge  (cost=12338.46..12394.36 rows=480 width=64) (actual time=539.546..564.101 rows=12.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6804
        ->  Sort  (cost=11338.43..11338.93 rows=200 width=64) (actual time=446.723..446.730 rows=4.00 loops=3)
              Sort Key: p.category
              Sort Method: quicksort  Memory: 25kB
              Buffers: shared hit=6804
              Worker 0:  Sort Method: quicksort  Memory: 25kB
              Worker 1:  Sort Method: quicksort  Memory: 25kB
              ->  Partial HashAggregate  (cost=11328.29..11330.79 rows=200 width=64) (actual time=446.459..446.526 rows=4.00 loops=3)
                    Group Key: p.category
                    Batches: 1  Memory Usage: 32kB
                    Buffers: shared hit=6788
                    Worker 0:  Batches: 1  Memory Usage: 32kB
                    Worker 1:  Batches: 1  Memory Usage: 32kB
                    ->  Hash Join  (cost=89.45..10771.35 rows=111387 width=48) (actual time=2.819..288.070 rows=174959.33 loops=3)
                          Hash Cond: (f.product_key = p.product_key)
                          Buffers: shared hit=6788
                          ->  Parallel Append  (cost=0.00..10388.98 rows=111386 width=20) (actual time=0.023..149.527 rows=174959.33 loops=3)
                                Buffers: shared hit=6677
                                ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=24434 width=20) (actual time=0.017..66.274 rows=82004.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1073
                                      Buffers: shared hit=1037
                                ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=17568 width=20) (actual time=0.021..36.335 rows=58537.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 1194
                                      Buffers: shared hit=741
                                ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=14618 width=20) (actual time=0.012..38.722 rows=48900.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 801
                                      Buffers: shared hit=618
                                ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=12268 width=20) (actual time=0.035..24.023 rows=40991.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 719
                                      Buffers: shared hit=527
                                ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=11494 width=20) (actual time=0.012..32.713 rows=38395.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 684
                                      Buffers: shared hit=490
                                ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=10746 width=20) (actual time=0.016..12.857 rows=11972.33 loops=3)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 207
                                      Buffers: shared hit=456
                                ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=10713 width=20) (actual time=0.014..10.646 rows=17858.00 loops=2)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 354
                                      Buffers: shared hit=455
                                ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=10645 width=20) (actual time=0.009..18.615 rows=35497.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 696
                                      Buffers: shared hit=452
                                ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=10224 width=20) (actual time=0.009..18.809 rows=34060.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 700
                                      Buffers: shared hit=438
                                ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=10274 width=20) (actual time=0.009..20.989 rows=34264.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 667
                                      Buffers: shared hit=435
                                ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=8659 width=20) (actual time=0.008..16.975 rows=28882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 558
                                      Buffers: shared hit=368
                                ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=8045 width=20) (actual time=0.010..22.351 rows=26882.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 470
                                      Buffers: shared hit=343
                                ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=7409 width=20) (actual time=0.017..10.978 rows=24833.00 loops=1)
                                      Filter: (NOT is_cancelled)
                                      Rows Removed by Filter: 359
                                      Buffers: shared hit=317
                                ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=156 width=20) (actual time=0.004..0.004 rows=0.00 loops=1)
                                      Filter: (NOT is_cancelled)
                          ->  Hash  (cost=60.31..60.31 rows=2331 width=36) (actual time=2.764..2.764 rows=3828.00 loops=3)
                                Buckets: 4096  Batches: 1  Memory Usage: 197kB
                                Buffers: shared hit=111
                                ->  Seq Scan on dim_product p  (cost=0.00..60.31 rows=2331 width=36) (actual time=0.348..1.546 rows=3828.00 loops=3)
                                      Buffers: shared hit=111
Planning:
  Buffers: shared hit=4
Planning Time: 1.511 ms
Execution Time: 564.397 ms
```

## Top 10 customers by revenue

With indexes:
```
Limit  (cost=15143.67..15143.69 rows=10 width=36) (actual time=491.833..527.435 rows=10.00 loops=1)
  Buffers: shared hit=6740
  ->  Sort  (cost=15143.67..15154.97 rows=4520 width=36) (actual time=491.831..527.432 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6740
        ->  Finalize HashAggregate  (cost=14989.49..15045.99 rows=4520 width=36) (actual time=486.481..525.570 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6737
              ->  Gather  (cost=13766.83..14908.13 rows=10848 width=36) (actual time=468.140..509.767 rows=7998.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6737
                    ->  Partial HashAggregate  (cost=12766.83..12823.33 rows=4520 width=36) (actual time=355.736..358.413 rows=2666.00 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6737
                          Worker 0:  Batches: 1  Memory Usage: 1041kB
                          Worker 1:  Batches: 1  Memory Usage: 1041kB
                          ->  Hash Join  (cost=121.70..11652.96 rows=222775 width=20) (actual time=2.955..227.007 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6737
                                ->  Parallel Append  (cost=0.00..10945.93 rows=222775 width=20) (actual time=0.023..121.427 rows=178043.00 loops=3)
                                      Buffers: shared hit=6677
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=48869 width=20) (actual time=0.017..62.581 rows=83077.00 loops=1)
                                            Buffers: shared hit=1037
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=35136 width=20) (actual time=0.021..32.201 rows=59731.00 loops=1)
                                            Buffers: shared hit=741
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=29236 width=20) (actual time=0.012..24.497 rows=49701.00 loops=1)
                                            Buffers: shared hit=618
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=24535 width=20) (actual time=0.029..40.310 rows=41710.00 loops=1)
                                            Buffers: shared hit=527
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=22988 width=20) (actual time=0.015..7.668 rows=13026.33 loops=3)
                                            Buffers: shared hit=490
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=21493 width=20) (actual time=0.018..9.177 rows=18269.00 loops=2)
                                            Buffers: shared hit=456
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=21426 width=20) (actual time=0.008..18.775 rows=36425.00 loops=1)
                                            Buffers: shared hit=455
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=21290 width=20) (actual time=0.008..15.217 rows=36193.00 loops=1)
                                            Buffers: shared hit=452
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=20447 width=20) (actual time=0.008..14.058 rows=34760.00 loops=1)
                                            Buffers: shared hit=438
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=20548 width=20) (actual time=0.009..13.124 rows=34931.00 loops=1)
                                            Buffers: shared hit=435
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=17318 width=20) (actual time=0.009..10.886 rows=29440.00 loops=1)
                                            Buffers: shared hit=368
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=16089 width=20) (actual time=0.008..13.508 rows=27352.00 loops=1)
                                            Buffers: shared hit=343
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=14819 width=20) (actual time=0.019..8.736 rows=25192.00 loops=1)
                                            Buffers: shared hit=317
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=312 width=20) (actual time=0.005..0.005 rows=0.00 loops=1)
                                ->  Hash  (cost=65.20..65.20 rows=4520 width=8) (actual time=2.865..2.866 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..65.20 rows=4520 width=8) (actual time=0.291..1.438 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=84 read=1
Planning Time: 2.475 ms
Execution Time: 528.509 ms
```

Index scans turned off:
```
Limit  (cost=15143.67..15143.69 rows=10 width=36) (actual time=472.122..485.906 rows=10.00 loops=1)
  Buffers: shared hit=6737
  ->  Sort  (cost=15143.67..15154.97 rows=4520 width=36) (actual time=472.119..485.901 rows=10.00 loops=1)
        Sort Key: (sum(f.line_total)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        Buffers: shared hit=6737
        ->  Finalize HashAggregate  (cost=14989.49..15045.99 rows=4520 width=36) (actual time=465.550..483.886 rows=4371.00 loops=1)
              Group Key: c.customer_id
              Batches: 1  Memory Usage: 1937kB
              Buffers: shared hit=6737
              ->  Gather  (cost=13766.83..14908.13 rows=10848 width=36) (actual time=446.318..466.073 rows=8172.00 loops=1)
                    Workers Planned: 2
                    Workers Launched: 2
                    Buffers: shared hit=6737
                    ->  Partial HashAggregate  (cost=12766.83..12823.33 rows=4520 width=36) (actual time=356.295..359.057 rows=2724.00 loops=3)
                          Group Key: c.customer_id
                          Batches: 1  Memory Usage: 1297kB
                          Buffers: shared hit=6737
                          Worker 0:  Batches: 1  Memory Usage: 1297kB
                          Worker 1:  Batches: 1  Memory Usage: 1041kB
                          ->  Hash Join  (cost=121.70..11652.96 rows=222775 width=20) (actual time=3.234..240.792 rows=133854.67 loops=3)
                                Hash Cond: (f.customer_key = c.customer_key)
                                Buffers: shared hit=6737
                                ->  Parallel Append  (cost=0.00..10945.93 rows=222775 width=20) (actual time=0.025..125.452 rows=178043.00 loops=3)
                                      Buffers: shared hit=6677
                                      ->  Parallel Seq Scan on fact_sales_2011_11 f_12  (cost=0.00..1525.69 rows=48869 width=20) (actual time=0.016..52.329 rows=83077.00 loops=1)
                                            Buffers: shared hit=1037
                                      ->  Parallel Seq Scan on fact_sales_2011_10 f_11  (cost=0.00..1092.36 rows=35136 width=20) (actual time=0.026..43.244 rows=59731.00 loops=1)
                                            Buffers: shared hit=741
                                      ->  Parallel Seq Scan on fact_sales_2011_09 f_10  (cost=0.00..910.36 rows=29236 width=20) (actual time=0.022..26.721 rows=49701.00 loops=1)
                                            Buffers: shared hit=618
                                      ->  Parallel Seq Scan on fact_sales_2010_12 f_1  (cost=0.00..772.35 rows=24535 width=20) (actual time=0.013..24.158 rows=41710.00 loops=1)
                                            Buffers: shared hit=527
                                      ->  Parallel Seq Scan on fact_sales_2011_07 f_8  (cost=0.00..719.88 rows=22988 width=20) (actual time=0.025..17.370 rows=39079.00 loops=1)
                                            Buffers: shared hit=490
                                      ->  Parallel Seq Scan on fact_sales_2011_05 f_6  (cost=0.00..670.93 rows=21493 width=20) (actual time=0.011..5.499 rows=12179.33 loops=3)
                                            Buffers: shared hit=456
                                      ->  Parallel Seq Scan on fact_sales_2011_06 f_7  (cost=0.00..669.26 rows=21426 width=20) (actual time=0.012..13.027 rows=18212.50 loops=2)
                                            Buffers: shared hit=455
                                      ->  Parallel Seq Scan on fact_sales_2011_03 f_4  (cost=0.00..664.90 rows=21290 width=20) (actual time=0.009..16.434 rows=36193.00 loops=1)
                                            Buffers: shared hit=452
                                      ->  Parallel Seq Scan on fact_sales_2011_01 f_2  (cost=0.00..642.47 rows=20447 width=20) (actual time=0.008..22.609 rows=34760.00 loops=1)
                                            Buffers: shared hit=438
                                      ->  Parallel Seq Scan on fact_sales_2011_08 f_9  (cost=0.00..640.48 rows=20548 width=20) (actual time=0.010..17.038 rows=34931.00 loops=1)
                                            Buffers: shared hit=435
                                      ->  Parallel Seq Scan on fact_sales_2011_04 f_5  (cost=0.00..541.18 rows=17318 width=20) (actual time=0.008..12.627 rows=29440.00 loops=1)
                                            Buffers: shared hit=368
                                      ->  Parallel Seq Scan on fact_sales_2011_02 f_3  (cost=0.00..503.89 rows=16089 width=20) (actual time=0.008..11.996 rows=27352.00 loops=1)
                                            Buffers: shared hit=343
                                      ->  Parallel Seq Scan on fact_sales_2011_12 f_13  (cost=0.00..465.19 rows=14819 width=20) (actual time=0.018..9.146 rows=25192.00 loops=1)
                                            Buffers: shared hit=317
                                      ->  Parallel Seq Scan on fact_sales_default f_14  (cost=0.00..13.12 rows=312 width=20) (actual time=0.005..0.005 rows=0.00 loops=1)
                                ->  Hash  (cost=65.20..65.20 rows=4520 width=8) (actual time=3.146..3.147 rows=4371.00 loops=3)
                                      Buckets: 8192  Batches: 1  Memory Usage: 235kB
                                      Buffers: shared hit=60
                                      ->  Seq Scan on dim_customer c  (cost=0.00..65.20 rows=4520 width=8) (actual time=0.336..1.682 rows=4371.00 loops=3)
                                            Buffers: shared hit=60
Planning:
  Buffers: shared hit=4
Planning Time: 1.552 ms
Execution Time: 487.019 ms
```

## One month of sales (June 2011)

With indexes:
```
Aggregate  (cost=1001.83..1001.84 rows=1 width=32) (actual time=28.635..28.636 rows=1.00 loops=1)
  Buffers: shared hit=455
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1001.38 rows=182 width=16) (actual time=0.040..19.024 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=455
Planning:
  Buffers: shared hit=38
Planning Time: 0.415 ms
Execution Time: 28.673 ms
```

Index scans turned off:
```
Aggregate  (cost=1001.83..1001.84 rows=1 width=32) (actual time=22.461..22.462 rows=1.00 loops=1)
  Buffers: shared hit=455
  ->  Seq Scan on fact_sales_2011_06 fact_sales  (cost=0.00..1001.38 rows=182 width=16) (actual time=0.030..14.425 rows=36425.00 loops=1)
        Filter: ((invoice_date >= '2011-06-01 00:00:00'::timestamp without time zone) AND (invoice_date < '2011-07-01 00:00:00'::timestamp without time zone))
        Buffers: shared hit=455
Planning Time: 0.241 ms
Execution Time: 22.496 ms
```

## One customer's orders (point lookup)

With indexes:
```
Aggregate  (cost=5199.16..5199.17 rows=1 width=8) (actual time=1.590..1.599 rows=1.00 loops=1)
  Buffers: shared hit=7 read=26
  ->  Append  (cost=5.91..5192.47 rows=2675 width=0) (actual time=0.319..1.585 rows=40.00 loops=1)
        Buffers: shared hit=7 read=26
        ->  Bitmap Heap Scan on fact_sales_2010_12 fact_sales_1  (cost=5.91..405.99 rows=209 width=0) (actual time=0.189..0.190 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2010_12_customer_key_idx  (cost=0.00..5.86 rows=209 width=0) (actual time=0.164..0.164 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_01 fact_sales_2  (cost=5.64..338.93 rows=174 width=0) (actual time=0.128..0.132 rows=12.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=2
              Buffers: shared hit=2 read=2
              ->  Bitmap Index Scan on fact_sales_2011_01_customer_key_idx  (cost=0.00..5.59 rows=174 width=0) (actual time=0.105..0.105 rows=12.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_02 fact_sales_3  (cost=5.35..267.30 rows=137 width=0) (actual time=0.113..0.114 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_02_customer_key_idx  (cost=0.00..5.31 rows=137 width=0) (actual time=0.099..0.099 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_03 fact_sales_4  (cost=5.69..350.13 rows=181 width=0) (actual time=0.113..0.113 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_03_customer_key_idx  (cost=0.00..5.65 rows=181 width=0) (actual time=0.098..0.099 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_04 fact_sales_5  (cost=5.43..285.93 rows=147 width=0) (actual time=0.104..0.104 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_04_customer_key_idx  (cost=0.00..5.39 rows=147 width=0) (actual time=0.090..0.090 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_05 fact_sales_6  (cost=5.71..354.12 rows=183 width=0) (actual time=0.104..0.104 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_05_customer_key_idx  (cost=0.00..5.66 rows=183 width=0) (actual time=0.089..0.090 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_06 fact_sales_7  (cost=5.70..352.41 rows=182 width=0) (actual time=0.127..0.133 rows=26.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=2
              Buffers: shared hit=2 read=2
              ->  Bitmap Index Scan on fact_sales_2011_06_customer_key_idx  (cost=0.00..5.66 rows=182 width=0) (actual time=0.097..0.097 rows=26.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_07 fact_sales_8  (cost=5.80..378.20 rows=195 width=0) (actual time=0.111..0.112 rows=2.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Heap Blocks: exact=1
              Buffers: shared hit=1 read=2
              ->  Bitmap Index Scan on fact_sales_2011_07_customer_key_idx  (cost=0.00..5.75 rows=195 width=0) (actual time=0.094..0.094 rows=2.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_08 fact_sales_9  (cost=5.65..338.08 rows=175 width=0) (actual time=0.120..0.121 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_08_customer_key_idx  (cost=0.00..5.60 rows=175 width=0) (actual time=0.103..0.103 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_09 fact_sales_10  (cost=6.22..479.32 rows=249 width=0) (actual time=0.102..0.102 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_09_customer_key_idx  (cost=0.00..6.16 rows=249 width=0) (actual time=0.088..0.088 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_10 fact_sales_11  (cost=6.61..573.32 rows=299 width=0) (actual time=0.101..0.101 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_10_customer_key_idx  (cost=0.00..6.53 rows=299 width=0) (actual time=0.087..0.087 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_11 fact_sales_12  (cost=7.51..797.12 rows=415 width=0) (actual time=0.111..0.112 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_11_customer_key_idx  (cost=0.00..7.41 rows=415 width=0) (actual time=0.100..0.100 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_2011_12 fact_sales_13  (cost=5.26..246.95 rows=126 width=0) (actual time=0.116..0.117 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared read=2
              ->  Bitmap Index Scan on fact_sales_2011_12_customer_key_idx  (cost=0.00..5.23 rows=126 width=0) (actual time=0.102..0.102 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared read=2
        ->  Bitmap Heap Scan on fact_sales_default fact_sales_14  (cost=4.17..11.28 rows=3 width=0) (actual time=0.015..0.015 rows=0.00 loops=1)
              Recheck Cond: (customer_key = 100)
              Buffers: shared hit=2
              ->  Bitmap Index Scan on fact_sales_default_customer_key_idx  (cost=0.00..4.17 rows=3 width=0) (actual time=0.005..0.005 rows=0.00 loops=1)
                    Index Cond: (customer_key = 100)
                    Index Searches: 1
                    Buffers: shared hit=2
Planning:
  Buffers: shared hit=9 read=1
Planning Time: 1.316 ms
Execution Time: 1.956 ms
```

Index scans turned off:
```
Finalize Aggregate  (cost=11626.88..11626.89 rows=1 width=8) (actual time=129.739..164.556 rows=1.00 loops=1)
  Buffers: shared hit=6677
  ->  Gather  (cost=11626.66..11626.87 rows=2 width=8) (actual time=128.602..164.541 rows=3.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6677
        ->  Partial Aggregate  (cost=10626.66..10626.67 rows=1 width=8) (actual time=52.168..52.173 rows=1.00 loops=3)
              Buffers: shared hit=6677
              ->  Parallel Append  (cost=0.00..10623.88 rows=1113 width=0) (actual time=20.000..52.162 rows=13.33 loops=3)
                    Buffers: shared hit=6677
                    ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=244 width=0) (actual time=10.329..10.329 rows=0.00 loops=3)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 27692
                          Buffers: shared hit=1037
                    ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=176 width=0) (actual time=9.457..9.457 rows=0.00 loops=2)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 29866
                          Buffers: shared hit=741
                    ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=146 width=0) (actual time=20.440..20.440 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 49701
                          Buffers: shared hit=618
                    ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=123 width=0) (actual time=14.849..14.849 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 41710
                          Buffers: shared hit=527
                    ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=115 width=0) (actual time=14.530..14.590 rows=2.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 39077
                          Buffers: shared hit=490
                    ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=108 width=0) (actual time=7.872..7.872 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36538
                          Buffers: shared hit=456
                    ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=107 width=0) (actual time=0.013..8.453 rows=26.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36399
                          Buffers: shared hit=455
                    ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=106 width=0) (actual time=8.643..8.643 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 36193
                          Buffers: shared hit=452
                    ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=102 width=0) (actual time=6.859..8.046 rows=12.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34748
                          Buffers: shared hit=438
                    ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=103 width=0) (actual time=6.931..6.931 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 34931
                          Buffers: shared hit=435
                    ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=86 width=0) (actual time=5.983..5.983 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 29440
                          Buffers: shared hit=368
                    ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=81 width=0) (actual time=5.325..5.326 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 27352
                          Buffers: shared hit=343
                    ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.24 rows=74 width=0) (actual time=5.359..5.360 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
                          Rows Removed by Filter: 25192
                          Buffers: shared hit=317
                    ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=2 width=0) (actual time=0.004..0.004 rows=0.00 loops=1)
                          Filter: (customer_key = 100)
Planning:
  Buffers: shared hit=4
Planning Time: 1.140 ms
Execution Time: 164.760 ms
```

## Monthly revenue by country, from the fact table

With indexes:
```
Finalize GroupAggregate  (cost=25320.32..39873.57 rows=39996 width=68) (actual time=644.512..868.494 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Buffers: shared hit=6771, temp read=2260 written=2267
  ->  Gather Merge  (cost=25320.32..38213.74 rows=95990 width=68) (actual time=644.500..866.742 rows=324.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6771, temp read=2260 written=2267
        ->  Partial GroupAggregate  (cost=24320.30..26134.09 rows=39996 width=68) (actual time=370.381..557.183 rows=108.00 loops=3)
              Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
              Buffers: shared hit=6771, temp read=2260 written=2267
              ->  Sort  (cost=24320.30..24598.76 rows=111386 width=52) (actual time=370.268..435.609 rows=174959.33 loops=3)
                    Sort Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
                    Sort Method: external merge  Disk: 7240kB
                    Buffers: shared hit=6771, temp read=2260 written=2267
                    Worker 0:  Sort Method: external merge  Disk: 4992kB
                    Worker 1:  Sort Method: external merge  Disk: 5848kB
                    ->  Parallel Append  (cost=0.00..11175.25 rows=111386 width=52) (actual time=0.027..211.142 rows=174959.33 loops=3)
                          Buffers: shared hit=6677
                          ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=24434 width=52) (actual time=0.022..99.310 rows=82004.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1073
                                Buffers: shared hit=1037
                          ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=17568 width=52) (actual time=0.027..70.668 rows=58537.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1194
                                Buffers: shared hit=741
                          ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=14618 width=52) (actual time=0.016..42.418 rows=48900.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 801
                                Buffers: shared hit=618
                          ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=12268 width=52) (actual time=0.026..32.046 rows=40991.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 719
                                Buffers: shared hit=527
                          ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=11494 width=52) (actual time=0.014..12.345 rows=12798.33 loops=3)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 228
                                Buffers: shared hit=490
                          ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=10746 width=52) (actual time=0.015..30.135 rows=35917.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 621
                                Buffers: shared hit=456
                          ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=10713 width=52) (actual time=0.014..18.277 rows=17858.00 loops=2)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 354
                                Buffers: shared hit=455
                          ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=10645 width=52) (actual time=0.010..55.112 rows=35497.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 696
                                Buffers: shared hit=452
                          ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=10224 width=52) (actual time=0.014..31.120 rows=34060.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 700
                                Buffers: shared hit=438
                          ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=10274 width=52) (actual time=0.009..38.032 rows=34264.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 667
                                Buffers: shared hit=435
                          ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=8659 width=52) (actual time=0.009..26.242 rows=28882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 558
                                Buffers: shared hit=368
                          ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=8045 width=52) (actual time=0.010..31.889 rows=26882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 470
                                Buffers: shared hit=343
                          ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.23 rows=7409 width=52) (actual time=0.018..21.490 rows=24833.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 359
                                Buffers: shared hit=317
                          ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=156 width=52) (actual time=0.004..0.004 rows=0.00 loops=1)
                                Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 1.115 ms
Execution Time: 872.494 ms
```

Index scans turned off:
```
Finalize GroupAggregate  (cost=25320.32..39873.57 rows=39996 width=68) (actual time=724.419..972.337 rows=302.00 loops=1)
  Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
  Buffers: shared hit=6771, temp read=2259 written=2266
  ->  Gather Merge  (cost=25320.32..38213.74 rows=95990 width=68) (actual time=724.398..971.434 rows=315.00 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        Buffers: shared hit=6771, temp read=2259 written=2266
        ->  Partial GroupAggregate  (cost=24320.30..26134.09 rows=39996 width=68) (actual time=490.642..658.885 rows=105.00 loops=3)
              Group Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
              Buffers: shared hit=6771, temp read=2259 written=2266
              ->  Sort  (cost=24320.30..24598.76 rows=111386 width=52) (actual time=490.533..551.304 rows=174959.33 loops=3)
                    Sort Key: ((date_trunc('month'::text, fact_sales.invoice_date))::date), fact_sales.country
                    Sort Method: external merge  Disk: 7560kB
                    Buffers: shared hit=6771, temp read=2259 written=2266
                    Worker 0:  Sort Method: external merge  Disk: 4952kB
                    Worker 1:  Sort Method: external merge  Disk: 5560kB
                    ->  Parallel Append  (cost=0.00..11175.25 rows=111386 width=52) (actual time=0.027..264.032 rows=174959.33 loops=3)
                          Buffers: shared hit=6677
                          ->  Parallel Seq Scan on fact_sales_2011_11 fact_sales_12  (cost=0.00..1647.86 rows=24434 width=52) (actual time=0.020..96.116 rows=82004.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1073
                                Buffers: shared hit=1037
                          ->  Parallel Seq Scan on fact_sales_2011_10 fact_sales_11  (cost=0.00..1180.20 rows=17568 width=52) (actual time=0.029..105.299 rows=58537.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 1194
                                Buffers: shared hit=741
                          ->  Parallel Seq Scan on fact_sales_2011_09 fact_sales_10  (cost=0.00..983.45 rows=14618 width=52) (actual time=0.013..90.634 rows=48900.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 801
                                Buffers: shared hit=618
                          ->  Parallel Seq Scan on fact_sales_2010_12 fact_sales_1  (cost=0.00..833.69 rows=12268 width=52) (actual time=0.026..53.847 rows=40991.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 719
                                Buffers: shared hit=527
                          ->  Parallel Seq Scan on fact_sales_2011_07 fact_sales_8  (cost=0.00..777.35 rows=11494 width=52) (actual time=0.016..17.789 rows=12798.33 loops=3)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 228
                                Buffers: shared hit=490
                          ->  Parallel Seq Scan on fact_sales_2011_05 fact_sales_6  (cost=0.00..724.66 rows=10746 width=52) (actual time=0.014..54.765 rows=35917.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 621
                                Buffers: shared hit=456
                          ->  Parallel Seq Scan on fact_sales_2011_06 fact_sales_7  (cost=0.00..722.83 rows=10713 width=52) (actual time=0.064..22.998 rows=17858.00 loops=2)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 354
                                Buffers: shared hit=455
                          ->  Parallel Seq Scan on fact_sales_2011_03 fact_sales_4  (cost=0.00..718.12 rows=10645 width=52) (actual time=0.011..46.844 rows=35497.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 696
                                Buffers: shared hit=452
                          ->  Parallel Seq Scan on fact_sales_2011_01 fact_sales_2  (cost=0.00..693.59 rows=10224 width=52) (actual time=0.009..50.283 rows=34060.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 700
                                Buffers: shared hit=438
                          ->  Parallel Seq Scan on fact_sales_2011_08 fact_sales_9  (cost=0.00..691.85 rows=10274 width=52) (actual time=0.010..30.871 rows=34264.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 667
                                Buffers: shared hit=435
                          ->  Parallel Seq Scan on fact_sales_2011_04 fact_sales_5  (cost=0.00..584.47 rows=8659 width=52) (actual time=0.009..27.191 rows=28882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 558
                                Buffers: shared hit=368
                          ->  Parallel Seq Scan on fact_sales_2011_02 fact_sales_3  (cost=0.00..544.12 rows=8045 width=52) (actual time=0.009..26.328 rows=26882.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 470
                                Buffers: shared hit=343
                          ->  Parallel Seq Scan on fact_sales_2011_12 fact_sales_13  (cost=0.00..502.23 rows=7409 width=52) (actual time=0.019..20.991 rows=24833.00 loops=1)
                                Filter: (NOT is_cancelled)
                                Rows Removed by Filter: 359
                                Buffers: shared hit=317
                          ->  Parallel Seq Scan on fact_sales_default fact_sales_14  (cost=0.00..13.90 rows=156 width=52) (actual time=0.004..0.004 rows=0.00 loops=1)
                                Filter: (NOT is_cancelled)
Planning:
  Buffers: shared hit=4
Planning Time: 1.241 ms
Execution Time: 977.216 ms
```

## Monthly revenue by country, from the materialized view

With indexes:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.038..0.103 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning:
  Buffers: shared hit=7 read=1
Planning Time: 1.186 ms
Execution Time: 0.125 ms
```

Index scans turned off:
```
Seq Scan on mv_monthly_revenue  (cost=0.00..5.78 rows=2 width=68) (actual time=0.034..0.085 rows=13.00 loops=1)
  Filter: (country = 'United Kingdom'::text)
  Rows Removed by Filter: 289
  Buffers: shared hit=2
Planning Time: 0.120 ms
Execution Time: 0.105 ms
```
