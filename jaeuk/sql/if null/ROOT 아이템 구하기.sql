select item_id, item_name
from item_info
where item_id in (select distinct t.ITEM_ID
                    from item_tree t
                    where t.parent_item_id is null)