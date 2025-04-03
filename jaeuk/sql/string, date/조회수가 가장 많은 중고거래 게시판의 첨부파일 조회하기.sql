select CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
from used_goods_file
where board_id = (select BOARD_ID
                from used_goods_board
                order by views desc
                limit 1)
order by FILE_ID desc

