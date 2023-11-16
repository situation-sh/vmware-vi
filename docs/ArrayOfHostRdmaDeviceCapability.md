# ArrayOfHostRdmaDeviceCapability

A boxed array of *HostRdmaDeviceCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostRdmaDeviceCapability]**](HostRdmaDeviceCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_rdma_device_capability import ArrayOfHostRdmaDeviceCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostRdmaDeviceCapability from a JSON string
array_of_host_rdma_device_capability_instance = ArrayOfHostRdmaDeviceCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostRdmaDeviceCapability.to_json()

# convert the object into a dict
array_of_host_rdma_device_capability_dict = array_of_host_rdma_device_capability_instance.to_dict()
# create an instance of ArrayOfHostRdmaDeviceCapability from a dict
array_of_host_rdma_device_capability_form_dict = array_of_host_rdma_device_capability.from_dict(array_of_host_rdma_device_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


