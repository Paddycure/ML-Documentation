bacterial_blight_sug = open("suggestion/bacterial-blight-sug.txt", "r")
brown_spot_sug = open("suggestion/brown-spot-sug.txt", "r")
healthy_sug = open("suggestion/healthy-sug.txt", "r")
hispa_sug = open("suggestion/hispa-sug.txt", "r")
leaf_blast_sug = open("suggestion/leaf-blast-sug.txt", "r")
leaf_smut_sug = open("suggestion/leaf-smut-sug.txt", "r")
tungro_sug = open("suggestion/tungro-sug.txt", "r")

bacterial_blight_sug_read = bacterial_blight_sug.read()
brown_spot_sug_read = brown_spot_sug.read()
healthy_sug_read = healthy_sug.read()
hispa_sug_read = hispa_sug.read()
leaf_blast_sug_read = leaf_blast_sug.read()
leaf_smut_sug_read = leaf_smut_sug.read()
tungro_sug_read = tungro_sug.read()

bacterial_blight_sug.close()
brown_spot_sug.close()
healthy_sug.close()
hispa_sug.close()
leaf_blast_sug.close()
leaf_smut_sug.close()
tungro_sug.close()

def suggestion(result):
    if result == "Bacterial Blight":
        return bacterial_blight_sug_read
    elif result == "Brown Spot":
        return brown_spot_sug_read
    elif result == "Healthy":
        return healthy_sug_read
    elif result == "Hispa":
        return hispa_sug_read
    elif result == "Leaf Blast":
        return leaf_blast_sug_read
    elif result == "Leaf Smut":
        return leaf_smut_sug_read
    elif result == "Tungro":
        return tungro_sug_read
    else:
        return "Undefined"