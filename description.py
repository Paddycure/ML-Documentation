bacterial_blight_desc = open("description/bacterial-blight-desc.txt", "r")
brown_spot_desc = open("description/brown-spot-desc.txt", "r")
healthy_desc = open("description/healthy-desc.txt", "r")
hispa_desc = open("description/hispa-desc.txt", "r")
leaf_blast_desc = open("description/leaf-blast-desc.txt", "r")
leaf_smut_desc = open("description/leaf-smut-desc.txt", "r")
tungro_desc = open("description/tungro-desc.txt", "r")

bacterial_blight_desc_read = bacterial_blight_desc.read()
brown_spot_desc_read = brown_spot_desc.read()
healthy_desc_read = healthy_desc.read()
hispa_desc_read = hispa_desc.read()
leaf_blast_desc_read = leaf_blast_desc.read()
leaf_smut_desc_read = leaf_smut_desc.read()
tungro_desc_read = tungro_desc.read()

bacterial_blight_desc.close()
brown_spot_desc.close()
healthy_desc.close()
hispa_desc.close()
leaf_blast_desc.close()
leaf_smut_desc.close()
tungro_desc.close()

def description(result):
    if result == "Bacterial Blight":
        return bacterial_blight_desc_read
    elif result == "Brown Spot":
        return brown_spot_desc_read
    elif result == "Healthy":
        return healthy_desc_read
    elif result == "Hispa":
        return hispa_desc_read
    elif result == "Leaf Blast":
        return leaf_blast_desc_read
    elif result == "Leaf Smut":
        return leaf_smut_desc_read
    elif result == "Tungro":
        return tungro_desc_read
    else:
        return "Undefined"