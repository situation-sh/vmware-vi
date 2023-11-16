# MarkPerenniallyReservedRequestType

The parameters of *HostStorageSystem.MarkPerenniallyReserved*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **str** | The UUID of the ScsiLun device to be marked as perennially reserved.  | 
**state** | **bool** | State of the ScsiLun perennially reserved flag to be set.  | 

## Example

```python
from vmware_vi.models.mark_perennially_reserved_request_type import MarkPerenniallyReservedRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MarkPerenniallyReservedRequestType from a JSON string
mark_perennially_reserved_request_type_instance = MarkPerenniallyReservedRequestType.from_json(json)
# print the JSON string representation of the object
print MarkPerenniallyReservedRequestType.to_json()

# convert the object into a dict
mark_perennially_reserved_request_type_dict = mark_perennially_reserved_request_type_instance.to_dict()
# create an instance of MarkPerenniallyReservedRequestType from a dict
mark_perennially_reserved_request_type_form_dict = mark_perennially_reserved_request_type.from_dict(mark_perennially_reserved_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


