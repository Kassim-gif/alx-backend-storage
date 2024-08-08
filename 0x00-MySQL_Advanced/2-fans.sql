-- Ranks country origins of tha bands, ordered by tha number of (non-unique) fans.
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
