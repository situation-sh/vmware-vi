# CreateLocalDatastoreRequestType

The parameters of *HostDatastoreSystem.CreateLocalDatastore*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of a datastore to create on the local host.  | 
**path** | **str** | The file path for a directory in which the virtual machine data will be stored.  | 

## Example

```python
from vmware_vi.models.create_local_datastore_request_type import CreateLocalDatastoreRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLocalDatastoreRequestType from a JSON string
create_local_datastore_request_type_instance = CreateLocalDatastoreRequestType.from_json(json)
# print the JSON string representation of the object
print CreateLocalDatastoreRequestType.to_json()

# convert the object into a dict
create_local_datastore_request_type_dict = create_local_datastore_request_type_instance.to_dict()
# create an instance of CreateLocalDatastoreRequestType from a dict
create_local_datastore_request_type_form_dict = create_local_datastore_request_type.from_dict(create_local_datastore_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


