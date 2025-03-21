SELECT 
    date,
    region,
    category,
    quantity,
    unit_price,
    discount,
    final_price,
    total_sale
FROM {{ source('warehouse', 'sales_data') }}
