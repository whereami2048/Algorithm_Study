SELECT ao.ANIMAL_ID, ao.NAME
FROM ANIMAL_OUTS as ao
LEFT JOIN ANIMAL_INS as ai
ON ai.animal_id = ao.animal_id
WHERE ai.animal_id is NULL
ORDER BY ao.ANIMAL_ID