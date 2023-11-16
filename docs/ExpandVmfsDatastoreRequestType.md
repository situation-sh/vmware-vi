# ExpandVmfsDatastoreRequestType

The parameters of *HostDatastoreSystem.ExpandVmfsDatastore*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**VmfsDatastoreExpandSpec**](VmfsDatastoreExpandSpec.md) |  | 

## Example

```python
from vmware_vi.models.expand_vmfs_datastore_request_type import ExpandVmfsDatastoreRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandVmfsDatastoreRequestType from a JSON string
expand_vmfs_datastore_request_type_instance = ExpandVmfsDatastoreRequestType.from_json(json)
# print the JSON string representation of the object
print ExpandVmfsDatastoreRequestType.to_json()

# convert the object into a dict
expand_vmfs_datastore_request_type_dict = expand_vmfs_datastore_request_type_instance.to_dict()
# create an instance of ExpandVmfsDatastoreRequestType from a dict
expand_vmfs_datastore_request_type_form_dict = expand_vmfs_datastore_request_type.from_dict(expand_vmfs_datastore_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


