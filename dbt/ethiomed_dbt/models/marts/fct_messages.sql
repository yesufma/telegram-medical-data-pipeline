{{ config(materialized='table') }}

SELECT
    m.message_id::text AS message_id,
    m.channel,
    m.message_date
FROM {{ ref('stg_telegram_messages') }} m
