def insert_or_replace_tenant_id(storage_path_dict, table_name, tenant_prefix, base_tenant_id, full_tenant_id):
    """
    Updates storage paths with a new tenant ID, either by inserting or replacing the tenant ID based on a given prefix.
    If the base tenant ID differs from the full tenant ID, this function searches for paths containing the tenant prefix
    and updates them accordingly. If the tenant prefix is found, the tenant ID in the path is replaced with the new
    full tenant ID. If the prefix is not found, the new tenant ID is inserted immediately after the domain. Regardless
    of tenant ID changes, the 'data_model_version' in each path is updated to match the version derived from the
    provided table name.

    Args:
        storage_path_dict (dict): A dictionary where keys are descriptive names of the storage paths and values are
                                  the actual storage paths as strings.
        table_name (str): The name of the table, used to derive the data model version. If the name starts with 'v',
                          the version is taken from the table name; otherwise, 'v1' is used as a default version.
        tenant_prefix (str): The prefix used to identify tenant IDs within the storage paths. This prefix is used
                             to determine whether a tenant ID already exists in the path.
        base_tenant_id (str): The original tenant ID. If this ID matches the full tenant ID, no tenant ID updates
                              are made to the paths; only the data model version is updated.
        full_tenant_id (str): The new tenant ID to be inserted or to replace the existing tenant ID in each path.

    Returns:
        str: A JSON string representation of the updated storage paths dictionary, formatted with an indent of 4
             spaces for readability.
