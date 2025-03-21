SELECT 
    region,
    metric,
    month,
    value,
    target,
    year
FROM {{ source('warehouse', 'regional_data') }}
