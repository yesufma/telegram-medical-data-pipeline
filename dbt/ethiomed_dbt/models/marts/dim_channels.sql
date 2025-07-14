-- models/marts/dim_channels.sql
select distinct
  channel
from {{ ref('stg_telegram_messages') }}
