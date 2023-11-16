# MarkPerenniallyReservedExRequestType

The parameters of *HostStorageSystem.MarkPerenniallyReservedEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **List[str]** | The UUIDs of the ScsiLun devices that need a change in the perennially reserved flag state.  | [optional] 
**state** | **bool** | State of the ScsiLun perennially reserved flag to be set.  | 

## Example

```python
from vmware_vi.models.mark_perennially_reserved_ex_request_type import MarkPerenniallyReservedExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MarkPerenniallyReservedExRequestType from a JSON string
mark_perennially_reserved_ex_request_type_instance = MarkPerenniallyReservedExRequestType.from_json(json)
# print the JSON string representation of the object
print MarkPerenniallyReservedExRequestType.to_json()

# convert the object into a dict
mark_perennially_reserved_ex_request_type_dict = mark_perennially_reserved_ex_request_type_instance.to_dict()
# create an instance of MarkPerenniallyReservedExRequestType from a dict
mark_perennially_reserved_ex_request_type_form_dict = mark_perennially_reserved_ex_request_type.from_dict(mark_perennially_reserved_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


