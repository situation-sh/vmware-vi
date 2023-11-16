# QueryVirtualDiskFragmentationRequestType

The parameters of *VirtualDiskManager.QueryVirtualDiskFragmentation*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk for which to return the percentage of fragmentation.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_virtual_disk_fragmentation_request_type import QueryVirtualDiskFragmentationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVirtualDiskFragmentationRequestType from a JSON string
query_virtual_disk_fragmentation_request_type_instance = QueryVirtualDiskFragmentationRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVirtualDiskFragmentationRequestType.to_json()

# convert the object into a dict
query_virtual_disk_fragmentation_request_type_dict = query_virtual_disk_fragmentation_request_type_instance.to_dict()
# create an instance of QueryVirtualDiskFragmentationRequestType from a dict
query_virtual_disk_fragmentation_request_type_form_dict = query_virtual_disk_fragmentation_request_type.from_dict(query_virtual_disk_fragmentation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


