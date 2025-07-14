-- models/marts/dim_dates.sql
select distinct
  message_date::date as date
from {{ ref('stg_telegram_messages') }}
