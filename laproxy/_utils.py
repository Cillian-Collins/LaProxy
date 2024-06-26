from nilsimsa import Nilsimsa, convert_hex_to_ints

def similarity(text1, text2):
    ns1 = Nilsimsa(text1)
    ns2 = Nilsimsa(text2)

    digest1_hex = ns1.hexdigest()
    digest2_hex = ns2.hexdigest()

    digest1 = convert_hex_to_ints(digest1_hex)
    digest2 = convert_hex_to_ints(digest2_hex)
    
    similarity_score = ns1.compare(digest2)

    similarity_percentage = (similarity_score + 128) / 256 * 100

    return similarity_percentage