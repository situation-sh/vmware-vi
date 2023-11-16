# QueryMemoryOverheadExRequestType

The parameters of *HostSystem.QueryMemoryOverheadEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_config_info** | [**VirtualMachineConfigInfo**](VirtualMachineConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.query_memory_overhead_ex_request_type import QueryMemoryOverheadExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMemoryOverheadExRequestType from a JSON string
query_memory_overhead_ex_request_type_instance = QueryMemoryOverheadExRequestType.from_json(json)
# print the JSON string representation of the object
print QueryMemoryOverheadExRequestType.to_json()

# convert the object into a dict
query_memory_overhead_ex_request_type_dict = query_memory_overhead_ex_request_type_instance.to_dict()
# create an instance of QueryMemoryOverheadExRequestType from a dict
query_memory_overhead_ex_request_type_form_dict = query_memory_overhead_ex_request_type.from_dict(query_memory_overhead_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


