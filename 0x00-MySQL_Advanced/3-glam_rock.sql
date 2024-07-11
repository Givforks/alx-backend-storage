-- using the flowchart knowledge, it will make the algorithm flexible
-- Import the table dump
-- This step depends on your SQL database management system. 
-- For MySQL, you can use the SOURCE command in the MySQL shell:
-- SOURCE /path/to/metal_bands.sql;

-- Query to list all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name AS band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
