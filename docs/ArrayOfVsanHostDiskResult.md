# ArrayOfVsanHostDiskResult

A boxed array of *VsanHostDiskResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostDiskResult]**](VsanHostDiskResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_disk_result import ArrayOfVsanHostDiskResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostDiskResult from a JSON string
array_of_vsan_host_disk_result_instance = ArrayOfVsanHostDiskResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostDiskResult.to_json()

# convert the object into a dict
array_of_vsan_host_disk_result_dict = array_of_vsan_host_disk_result_instance.to_dict()
# create an instance of ArrayOfVsanHostDiskResult from a dict
array_of_vsan_host_disk_result_form_dict = array_of_vsan_host_disk_result.from_dict(array_of_vsan_host_disk_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


