# ArrayOfWipeDiskFault

A boxed array of *WipeDiskFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[WipeDiskFault]**](WipeDiskFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_wipe_disk_fault import ArrayOfWipeDiskFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfWipeDiskFault from a JSON string
array_of_wipe_disk_fault_instance = ArrayOfWipeDiskFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfWipeDiskFault.to_json()

# convert the object into a dict
array_of_wipe_disk_fault_dict = array_of_wipe_disk_fault_instance.to_dict()
# create an instance of ArrayOfWipeDiskFault from a dict
array_of_wipe_disk_fault_form_dict = array_of_wipe_disk_fault.from_dict(array_of_wipe_disk_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


