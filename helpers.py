REPLACE_LIST = {
	"a": ["á", "ã", "à"],
	"e": ["é", "ê"],
	"o": ["õ", "ó"],
	"u": ["ú", "û"],
	"c": ["ç"],
}


def format_header_to_db(header: list):
	result = []
	for item in header:
		item = item.replace(" ", "_")
		item = item.replace("/", "_")
		item = item.lower()

		for key, values in REPLACE_LIST.items():
			for word in values:
				if word in item:
					item = item.replace(word, key)

		result.append(item)

	return result
