-- Creates tha index idx_name_first_score on tha table names and
-- tha first letter of name and tha score.
CREATE INDEX idx_name_first_score ON names(name(1), score);
