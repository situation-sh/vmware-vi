# ArrayOfVsanFault

A boxed array of *VsanFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanFault]**](VsanFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_fault import ArrayOfVsanFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanFault from a JSON string
array_of_vsan_fault_instance = ArrayOfVsanFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanFault.to_json()

# convert the object into a dict
array_of_vsan_fault_dict = array_of_vsan_fault_instance.to_dict()
# create an instance of ArrayOfVsanFault from a dict
array_of_vsan_fault_form_dict = array_of_vsan_fault.from_dict(array_of_vsan_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


