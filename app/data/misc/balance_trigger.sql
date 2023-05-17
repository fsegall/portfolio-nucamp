CREATE OR REPLACE FUNCTION creates_customer_balance_with_first_income_transaction()
  RETURNS TRIGGER 
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
/*     IF EXISTS (SELECT FROM trackers_balance tb WHERE tb.customer = NEW.customer) THEN
        UPDATE trackers_balance
        SET 
        WHERE trackers_balance.customer = NEW.customer

    RETURN NEW;
    END IF; */
    INSERT INTO trackers_balance(current_balance, previous_balance, transaction_date, customer_id, transaction_id)
    VALUES (NEW.amount, 0.0, now(), NEW.customer_id, NEW.income_id)
END;
$$

CREATE TRIGGER customer_first_income_transaction()
  BEFORE INSERT
  ON trackers_income
  FOR EACH ROW
  EXECUTE PROCEDURE creates_customer_balance_with_first_income_transaction();


