CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts
USING fts5(
  app_area,
  dc_identifier,
  product,
  product_release_name,
  title,
  url UNINDEXED,
  contents,
  tokenize='porter unicode61 remove_diacritics 2'
);
