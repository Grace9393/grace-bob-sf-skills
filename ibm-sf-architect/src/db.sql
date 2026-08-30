CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts
USING fts5(
  title,
  url UNINDEXED,
  contents,
  images_text,
  images UNINDEXED,
  vlm_model UNINDEXED,
  tokenize='porter unicode61 remove_diacritics 2'
);
