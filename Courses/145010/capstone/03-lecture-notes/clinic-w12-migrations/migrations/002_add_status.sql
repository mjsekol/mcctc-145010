-- 002: the coordinator can mark a report restocked.
-- Existing rows get status 'open', so nothing already reported disappears.
ALTER TABLE low_reports ADD COLUMN status TEXT NOT NULL DEFAULT 'open';
ALTER TABLE low_reports ADD COLUMN restocked_at TEXT;
