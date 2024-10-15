

INSERT INTO `geek_text`.`user`
(`id`,
`name`,
`email`,
`password`)
VALUES
(1,
'testuser',
'testuser@email',
'testuserpassword');

INSERT INTO `geek_text`.`user_card`
(`UserID`,
`CreditCardNum`,
`ExpMonth`,
`ExpYear`,
`CVS`,
`NameOnCard`)
VALUES
(1,
12344523,
11,
22,
685,
"testname");

INSERT INTO `geek_text`.`user_card`
(`UserID`,
`CreditCardNum`,
`ExpMonth`,
`ExpYear`,
`CVS`,
`NameOnCard`)
VALUES
(1,
12344523,
11,
22,
685,
"testname2");

INSERT INTO `geek_text`.`user_card`
(`UserID`,
`CreditCardNum`,
`ExpMonth`,
`ExpYear`,
`CVS`,
`NameOnCard`)
VALUES
(1,
12344523,
11,
22,
685,
"testname3");



INSERT INTO `geek_text`.`user_shipping`
(`UserID`,
`ShippingAddr`,
`ShippingCity`,
`ShippingState`,
`ShippingZip`)
VALUES
(1,
"another address",
"another city",
"FL",
"33141");

INSERT INTO `geek_text`.`user_shipping`
(`UserID`,
`ShippingAddr`,
`ShippingCity`,
`ShippingState`,
`ShippingZip`)
VALUES
(1,
"another address2",
"another city2",
"FL",
"33141");