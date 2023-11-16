# ConfigureDatastoreIORMRequestType

The parameters of *StorageResourceManager.ConfigureDatastoreIORM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**StorageIORMConfigSpec**](StorageIORMConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.configure_datastore_iorm_request_type import ConfigureDatastoreIORMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureDatastoreIORMRequestType from a JSON string
configure_datastore_iorm_request_type_instance = ConfigureDatastoreIORMRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureDatastoreIORMRequestType.to_json()

# convert the object into a dict
configure_datastore_iorm_request_type_dict = configure_datastore_iorm_request_type_instance.to_dict()
# create an instance of ConfigureDatastoreIORMRequestType from a dict
configure_datastore_iorm_request_type_form_dict = configure_datastore_iorm_request_type.from_dict(configure_datastore_iorm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


