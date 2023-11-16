# ArrayOfHostRdmaDevice

A boxed array of *HostRdmaDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostRdmaDevice]**](HostRdmaDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_rdma_device import ArrayOfHostRdmaDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostRdmaDevice from a JSON string
array_of_host_rdma_device_instance = ArrayOfHostRdmaDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostRdmaDevice.to_json()

# convert the object into a dict
array_of_host_rdma_device_dict = array_of_host_rdma_device_instance.to_dict()
# create an instance of ArrayOfHostRdmaDevice from a dict
array_of_host_rdma_device_form_dict = array_of_host_rdma_device.from_dict(array_of_host_rdma_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


