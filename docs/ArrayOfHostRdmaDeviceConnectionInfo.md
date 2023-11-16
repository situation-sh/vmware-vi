# ArrayOfHostRdmaDeviceConnectionInfo

A boxed array of *HostRdmaDeviceConnectionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostRdmaDeviceConnectionInfo]**](HostRdmaDeviceConnectionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_rdma_device_connection_info import ArrayOfHostRdmaDeviceConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostRdmaDeviceConnectionInfo from a JSON string
array_of_host_rdma_device_connection_info_instance = ArrayOfHostRdmaDeviceConnectionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostRdmaDeviceConnectionInfo.to_json()

# convert the object into a dict
array_of_host_rdma_device_connection_info_dict = array_of_host_rdma_device_connection_info_instance.to_dict()
# create an instance of ArrayOfHostRdmaDeviceConnectionInfo from a dict
array_of_host_rdma_device_connection_info_form_dict = array_of_host_rdma_device_connection_info.from_dict(array_of_host_rdma_device_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


