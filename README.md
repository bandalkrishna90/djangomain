def insert_or_replace_tenant_id(storage_path_dict, table_name, tenant_prefix, base_tenant_id, full_tenant_id):
    """
    Modifies storage paths in a dictionary by either inserting or replacing the tenant ID, based on the specified
    tenant prefix. This function updates the tenant ID if it differs from the base to the full tenant ID, and adjusts
    the 'data_model_version' according to the table name provided. If the tenant prefix is detected, the existing
    tenant ID is replaced; otherwise, the new tenant ID is added after the domain. The data model version is
    consistently updated in all paths.

    Args:
        storage_path_dict (dict): Dictionary with storage path names and URLs.
        table_name (str): Name of the table to derive the version.
        tenant_prefix (str): Prefix indicating the presence of a tenant ID.
        base_tenant_id (str): Original tenant ID for comparison.
        full_tenant_id (str): New tenant ID for insertion or replacement.

    Returns:
        str: Updated storage paths as a JSON string.

    Example:
        >>> updated_storage_paths_json = insert_or_replace_tenant_id(...)
        >>> print(updated_storage_paths_json)
    """
