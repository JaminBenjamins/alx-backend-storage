-- SQL scripts that lists band with glam rock as mainstyle
-- ranked by longevity.
SELECT band_name,
(IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
