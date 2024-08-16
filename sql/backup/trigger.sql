CREATE OR REPLACE FUNCTION backup_on_change()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'DELETE' THEN
        INSERT INTO urls_backup (short_code, original_url, created_at, last_updated_at, expiration_date, access_count)
        VALUES (OLD.short_code, OLD.original_url, OLD.created_at, OLD.last_updated_at, OLD.expiration_date, OLD.access_count);
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO urls_backup (short_code, original_url, created_at, last_updated_at, expiration_date, access_count)
        VALUES (OLD.short_code, OLD.original_url, OLD.created_at, OLD.last_updated_at, OLD.expiration_date, OLD.access_count);
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO urls_backup (short_code, original_url, created_at, last_updated_at, expiration_date, access_count)
        VALUES (NEW.short_code, NEW.original_url, NEW.created_at, NEW.last_updated_at, NEW.expiration_date, NEW.access_count);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER backuptrigger
AFTER INSERT OR UPDATE OR DELETE ON urls
FOR EACH ROW
EXECUTE FUNCTION backup_on_change();