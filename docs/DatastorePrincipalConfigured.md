# DatastorePrincipalConfigured

This event records that a datastore principal was configured on a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_principal** | **str** |  | 

## Example

```python
from vmware_vi.models.datastore_principal_configured import DatastorePrincipalConfigured

# TODO update the JSON string below
json = "{}"
# create an instance of DatastorePrincipalConfigured from a JSON string
datastore_principal_configured_instance = DatastorePrincipalConfigured.from_json(json)
# print the JSON string representation of the object
print DatastorePrincipalConfigured.to_json()

# convert the object into a dict
datastore_principal_configured_dict = datastore_principal_configured_instance.to_dict()
# create an instance of DatastorePrincipalConfigured from a dict
datastore_principal_configured_form_dict = datastore_principal_configured.from_dict(datastore_principal_configured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


