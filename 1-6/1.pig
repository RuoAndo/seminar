wikitext_input = LOAD 'logcat' USING TextLoader();
wikitext_token = FOREACH wikitext_input GENERATE FLATTEN(TOKENIZE($0));
wikitext_group = GROUP wikitext_token BY $0;
dump wikitext_group

