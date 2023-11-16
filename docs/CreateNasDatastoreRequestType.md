# CreateNasDatastoreRequestType

The parameters of *HostDatastoreSystem.CreateNasDatastore*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostNasVolumeSpec**](HostNasVolumeSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_nas_datastore_request_type import CreateNasDatastoreRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNasDatastoreRequestType from a JSON string
create_nas_datastore_request_type_instance = CreateNasDatastoreRequestType.from_json(json)
# print the JSON string representation of the object
print CreateNasDatastoreRequestType.to_json()

# convert the object into a dict
create_nas_datastore_request_type_dict = create_nas_datastore_request_type_instance.to_dict()
# create an instance of CreateNasDatastoreRequestType from a dict
create_nas_datastore_request_type_form_dict = create_nas_datastore_request_type.from_dict(create_nas_datastore_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


