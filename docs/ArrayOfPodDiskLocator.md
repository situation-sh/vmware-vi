# ArrayOfPodDiskLocator

A boxed array of *PodDiskLocator*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PodDiskLocator]**](PodDiskLocator.md) |  | 

## Example

```python
from vmware_vi.models.array_of_pod_disk_locator import ArrayOfPodDiskLocator

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPodDiskLocator from a JSON string
array_of_pod_disk_locator_instance = ArrayOfPodDiskLocator.from_json(json)
# print the JSON string representation of the object
print ArrayOfPodDiskLocator.to_json()

# convert the object into a dict
array_of_pod_disk_locator_dict = array_of_pod_disk_locator_instance.to_dict()
# create an instance of ArrayOfPodDiskLocator from a dict
array_of_pod_disk_locator_form_dict = array_of_pod_disk_locator.from_dict(array_of_pod_disk_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


