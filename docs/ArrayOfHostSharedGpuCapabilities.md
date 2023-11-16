# ArrayOfHostSharedGpuCapabilities

A boxed array of *HostSharedGpuCapabilities*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSharedGpuCapabilities]**](HostSharedGpuCapabilities.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_shared_gpu_capabilities import ArrayOfHostSharedGpuCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSharedGpuCapabilities from a JSON string
array_of_host_shared_gpu_capabilities_instance = ArrayOfHostSharedGpuCapabilities.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSharedGpuCapabilities.to_json()

# convert the object into a dict
array_of_host_shared_gpu_capabilities_dict = array_of_host_shared_gpu_capabilities_instance.to_dict()
# create an instance of ArrayOfHostSharedGpuCapabilities from a dict
array_of_host_shared_gpu_capabilities_form_dict = array_of_host_shared_gpu_capabilities.from_dict(array_of_host_shared_gpu_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


