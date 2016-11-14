CREATE TABLE url (
  /* Creating a new row for every hash/device type combination
   * instead of having a single row containing all redirect urls
   * for a specific hash makes it easier to scale for more
   * devices (no migration needed, just a new device_type value)
   */
  hashid TEXT,
  redirect_url TEXT,
  device_type INTEGER,
  -- NOTE: TIMESTAMP columns in sqlite actually have a NUMERIC type
  --       sqlite3 handles the conversion between python datetime
  created TIMESTAMP
);

CREATE UNIQUE INDEX url__idx1 on url (hashid, device_type);

CREATE TABLE redirect (
  /* No need for any explicit primary key
   * Any queries on this table will be aggregate full table scans
   * An index on created might help, but can always be added later
   */
  hashid TEXT,
  device_type INTEGER,
  user_agent TEXT,
  created TIMESTAMP,
  FOREIGN KEY(hashid, device_type) REFERENCES url(hashid, device_type)
);
