# ConfigureDatastorePrincipalRequestType

The parameters of *HostDatastoreSystem.ConfigureDatastorePrincipal*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Datastore principal user name.  | 
**password** | **str** | Optional password for systems that require password for user impersonation.  | [optional] 

## Example

```python
from vmware_vi.models.configure_datastore_principal_request_type import ConfigureDatastorePrincipalRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureDatastorePrincipalRequestType from a JSON string
configure_datastore_principal_request_type_instance = ConfigureDatastorePrincipalRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureDatastorePrincipalRequestType.to_json()

# convert the object into a dict
configure_datastore_principal_request_type_dict = configure_datastore_principal_request_type_instance.to_dict()
# create an instance of ConfigureDatastorePrincipalRequestType from a dict
configure_datastore_principal_request_type_form_dict = configure_datastore_principal_request_type.from_dict(configure_datastore_principal_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


