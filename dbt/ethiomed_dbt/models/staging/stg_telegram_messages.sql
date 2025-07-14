-- models/staging/stg_telegram_messages.sql
with raw as (

  select * from raw.telegram_messages

)

select
  id as message_id,
  channel,
  date::timestamp as message_date,
  text,
  has_image
from raw
