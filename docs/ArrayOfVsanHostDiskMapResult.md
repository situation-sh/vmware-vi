# ArrayOfVsanHostDiskMapResult

A boxed array of *VsanHostDiskMapResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostDiskMapResult]**](VsanHostDiskMapResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_disk_map_result import ArrayOfVsanHostDiskMapResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostDiskMapResult from a JSON string
array_of_vsan_host_disk_map_result_instance = ArrayOfVsanHostDiskMapResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostDiskMapResult.to_json()

# convert the object into a dict
array_of_vsan_host_disk_map_result_dict = array_of_vsan_host_disk_map_result_instance.to_dict()
# create an instance of ArrayOfVsanHostDiskMapResult from a dict
array_of_vsan_host_disk_map_result_form_dict = array_of_vsan_host_disk_map_result.from_dict(array_of_vsan_host_disk_map_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


