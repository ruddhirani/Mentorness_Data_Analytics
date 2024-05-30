use hotel_reservation;
SHOW TABLES;

SELECT * 
FROM hotel_reservation_dataset;

/*What is the total number of reservations in the dataset?*/
SELECT COUNT(DISTINCT Booking_ID) AS total_reservations
FROM hotel_reservation_dataset; 

/*Which meal plan is the most popular among guests?*/
SELECT type_of_meal_plan, COUNT(*) AS count
FROM hotel_reservation_dataset
GROUP BY type_of_meal_plan
ORDER BY count DESC
LIMIT 1;

/*What is the average price per room for reservations involving children?*/
SELECT AVG(avg_price_per_room) AS average_price_per_room
FROM hotel_reservation_dataset
WHERE no_of_children > 0;

/*How many reservations were made for the year 2018?*/
SELECT COUNT(*) AS total_reservations_2018
FROM hotel_reservation_dataset
WHERE YEAR(STR_TO_DATE(arrival_date, '%Y-%m-%d')) = 2018;

/*What is the most commonly booked room type?*/
SELECT room_type_reserved, COUNT(*) AS number_of_reservations
FROM hotel_reservation_dataset
GROUP BY room_type_reserved
ORDER BY number_of_reservations DESC
LIMIT 1;

/*How many reservations fall on a weekend (no_of_weekend_nights > 0)?*/
SELECT COUNT(*) AS reservations_fall_on_weekend
FROM hotel_reservation_dataset
WHERE no_of_weekend_nights > 0;

/*What is the highest and lowest lead time for reservations?*/
SELECT MAX(lead_time) AS highest_lead_time, MIN(lead_time) AS lowest_lead_time
FROM hotel_reservation_dataset;

/*What is the most common market segment type for reservations?*/
SELECT market_segment_type, COUNT(*) AS segment_count
FROM hotel_reservation_dataset
GROUP BY market_segment_type
ORDER BY segment_count DESC
LIMIT 1;

/*How many reservations have a booking status of "Canceled"?*/
SELECT COUNT(*) AS canceled_reservations
FROM hotel_reservation_dataset
WHERE booking_status = 'Canceled';

/*What is the total number of adults and children across all reservations?*/
SELECT 
    SUM(no_of_adults) AS total_adults,
    SUM(no_of_children) AS total_children
FROM hotel_reservation_dataset;

/*What is the average number of weekend nights for reservations involving children?*/
SELECT AVG(no_of_weekend_nights) AS avg_weekend_nights_with_children
FROM hotel_reservation_dataset
WHERE no_of_children >0;

/*How many reservations were made in each month of the year?*/
SELECT 
    YEAR(STR_TO_DATE(arrival_date, '%Y-%m-%d')) AS year,
    MONTH(STR_TO_DATE(arrival_date, '%Y-%m-%d')) AS month,
    COUNT(*) AS reservations_count
FROM hotel_reservation_dataset
GROUP BY YEAR(STR_TO_DATE(arrival_date, '%Y-%m-%d')), MONTH(STR_TO_DATE(arrival_date, '%Y-%m-%d'))
ORDER BY year, month;

/*What is the average number of nights (both weekend and weekday) spent by guests for each room type?*/
SELECT 
    room_type_reserved,
    AVG(no_of_weekend_nights + no_of_week_nights) AS avg_nights_per_room
FROM hotel_reservation_dataset
GROUP BY room_type_reserved;

/*For reservations involving children, what is the most common room type, and what is the average price for that room type?*/
SELECT 
    room_type_reserved AS most_common_room_type,
    AVG(avg_price_per_room) AS average_price_for_room_type,
    COUNT(*) AS number_of_rooms_reserved
FROM hotel_reservation_dataset
WHERE Booking_ID IN (
    SELECT Booking_ID
    FROM hotel_reservation_dataset
    WHERE no_of_children > 0
)
GROUP BY room_type_reserved
ORDER BY COUNT(*) DESC
LIMIT 1;

/*Find the market segment type that generates the highest average price per room.*/
SELECT 
    market_segment_type,
    AVG(avg_price_per_room) AS average_price_per_room
FROM hotel_reservation_dataset
GROUP BY market_segment_type
ORDER BY average_price_per_room DESC
LIMIT 1;
