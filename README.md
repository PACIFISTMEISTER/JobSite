# JobSite
 70% ready


trigger for db

```
CREATE OR REPLACE FUNCTION COUNTER() RETURNS TRIGGER AS $$
DECLARE
    new_Category_id bigint;
BEGIN
    IF    TG_OP = 'INSERT' THEN
        new_Category_id = NEW."Category_id";
        update companies_category set "AvalibleJob"="AvalibleJob"+1 where "id"=new_Category_id;
        RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
        new_Category_id = NEW."Category_id";
        update companies_category set "AvalibleJob"="AvalibleJob"-1 where "id"=new_Category_id;
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER Counter
AFTER INSERT OR DELETE ON companies_job FOR EACH ROW EXECUTE PROCEDURE COUNTER ();
```
