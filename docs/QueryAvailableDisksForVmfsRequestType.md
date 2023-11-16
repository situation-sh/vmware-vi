# QueryAvailableDisksForVmfsRequestType

The parameters of *HostDatastoreSystem.QueryAvailableDisksForVmfs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_available_disks_for_vmfs_request_type import QueryAvailableDisksForVmfsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAvailableDisksForVmfsRequestType from a JSON string
query_available_disks_for_vmfs_request_type_instance = QueryAvailableDisksForVmfsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryAvailableDisksForVmfsRequestType.to_json()

# convert the object into a dict
query_available_disks_for_vmfs_request_type_dict = query_available_disks_for_vmfs_request_type_instance.to_dict()
# create an instance of QueryAvailableDisksForVmfsRequestType from a dict
query_available_disks_for_vmfs_request_type_form_dict = query_available_disks_for_vmfs_request_type.from_dict(query_available_disks_for_vmfs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


