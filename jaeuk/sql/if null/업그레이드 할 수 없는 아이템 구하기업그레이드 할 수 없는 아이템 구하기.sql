select ITEM_ID, ITEM_NAME, RARITY
from item_info
where item_id not in (select distinct parent_item_id
                        from item_tree
                        where parent_item_id is not null)
order by item_id desc