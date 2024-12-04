from app.app import db

def author_info_from_id(author_key):
    print(author_key)
    query = f"""
        LET auth = document("authors/{author_key}")

        // Retrieve associated software and document IDs
        LET softwareDocs = (
            FOR edge_doc IN edge_doc_to_author
                FILTER edge_doc._to == auth._id
                FOR edge_soft IN edge_doc_to_software
                    FILTER edge_soft._from == edge_doc._from
                    LET software = DOCUMENT(edge_soft._to)
                    LET doc = DOCUMENT(edge_doc._from)
                    RETURN [software.software_name.normalizedForm, doc.file_hal_id]
        )
        
        // Retrieve associated structures
        LET structures_list = (
            FOR edge_stru IN edge_auth_to_struc
                FILTER edge_stru._from == auth._id
                LET struc = DOCUMENT(edge_stru._to)
                RETURN struc
        )
        
        // Return the consolidated result
        RETURN {{
            author: auth,
            software_names: UNIQUE(softwareDocs),
            structures: structures_list
        }}
    """

    author_info_data = db.AQLQuery(query, rawResults=True)
    return author_info_data