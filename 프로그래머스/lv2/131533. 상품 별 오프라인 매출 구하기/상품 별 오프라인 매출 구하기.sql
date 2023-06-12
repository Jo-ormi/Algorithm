-- 코드를 입력하세요
SELECT PRODUCT_CODE, PRICE*SUM(SALES_AMOUNT) AS SALES
FROM PRODUCT p
JOIN OFFLINE_SALE o ON p.PRODUCT_ID = o.PRODUCT_ID
GROUP BY o.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE;
