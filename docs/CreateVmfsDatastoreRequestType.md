# CreateVmfsDatastoreRequestType

The parameters of *HostDatastoreSystem.CreateVmfsDatastore*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VmfsDatastoreCreateSpec**](VmfsDatastoreCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_vmfs_datastore_request_type import CreateVmfsDatastoreRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVmfsDatastoreRequestType from a JSON string
create_vmfs_datastore_request_type_instance = CreateVmfsDatastoreRequestType.from_json(json)
# print the JSON string representation of the object
print CreateVmfsDatastoreRequestType.to_json()

# convert the object into a dict
create_vmfs_datastore_request_type_dict = create_vmfs_datastore_request_type_instance.to_dict()
# create an instance of CreateVmfsDatastoreRequestType from a dict
create_vmfs_datastore_request_type_form_dict = create_vmfs_datastore_request_type.from_dict(create_vmfs_datastore_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


