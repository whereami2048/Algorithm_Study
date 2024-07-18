SELECT concat("/home/grep/src/", uf.board_id, "/", uf.file_id, uf.file_name, uf.file_ext) as FILE_PATH
from USED_GOODS_FILE as uf
join (select *
     from USED_GOODS_BOARD
     order by views DESC
     limit 1) as ub
on uf.board_id = ub.board_id
order by uf.file_id desc