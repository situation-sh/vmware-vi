# QueryVirtualDiskGeometryRequestType

The parameters of *VirtualDiskManager.QueryVirtualDiskGeometry*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk from which to get geometry information.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_virtual_disk_geometry_request_type import QueryVirtualDiskGeometryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVirtualDiskGeometryRequestType from a JSON string
query_virtual_disk_geometry_request_type_instance = QueryVirtualDiskGeometryRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVirtualDiskGeometryRequestType.to_json()

# convert the object into a dict
query_virtual_disk_geometry_request_type_dict = query_virtual_disk_geometry_request_type_instance.to_dict()
# create an instance of QueryVirtualDiskGeometryRequestType from a dict
query_virtual_disk_geometry_request_type_form_dict = query_virtual_disk_geometry_request_type.from_dict(query_virtual_disk_geometry_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


