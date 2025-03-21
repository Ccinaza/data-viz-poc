SELECT 
    user_id,
    username,
    department,
    access_level,
    join_date
FROM {{ source('warehouse', 'user_data') }}
