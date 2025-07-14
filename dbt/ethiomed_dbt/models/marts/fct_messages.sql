-- models/marts/fct_messages.sql
select
  message_id,
  channel as channel_id,
  message_date,
  text,
  has_image
from {{ ref('stg_telegram_messages') }}
