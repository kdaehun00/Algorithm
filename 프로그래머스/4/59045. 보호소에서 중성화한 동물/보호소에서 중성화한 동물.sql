-- 보호소에서 중성화된 동물 정보 (들어올 땐 중성화 X -> 나갈 땐 중성화 O)
-- 1. 나간 테이블 안에서 중성화된 동물 출력
-- 2. 이 때, 들어올 때 중성화 안 된 동물들을 대상으로
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_OUTS O
JOIN (
    SELECT ANIMAL_ID
    FROM ANIMAL_INS
    WHERE SEX_UPON_INTAKE LIKE "Intact%") I
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE SEX_UPON_OUTCOME LIKE "Spayed%"
OR SEX_UPON_OUTCOME LIKE "Neutered%"