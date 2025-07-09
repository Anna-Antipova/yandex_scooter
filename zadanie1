SELECT c."login" AS courier_login, COUNT(o."id") AS orders_in_delivery
FROM "Orders" o
JOIN "Couriers" c ON o."courierId" = c."id"
WHERE o."inDelivery" = TRUE
GROUP BY c."login"
ORDER BY orders_in_delivery DESC;
