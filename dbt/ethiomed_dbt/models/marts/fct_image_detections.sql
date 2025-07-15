{{ config(materialized='table') }}

SELECT
    r.message_id,
    m.channel,              -- changed from channel_id to channel
    m.message_date AS date_id,  -- assuming date_id is the message_date; adjust if different
    r.detected_object_class,
    r.confidence_score
FROM {{ source('raw', 'image_detections') }} r
LEFT JOIN {{ ref('stg_telegram_messages') }} m
    ON r.message_id = m.message_id::text
WHERE r.confidence_score >= 0.5
