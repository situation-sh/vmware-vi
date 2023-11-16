# HostRdmaDeviceCapability

Represents device capabilies, e.g.  supported protocols.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roce_v1_capable** | **bool** | Indicates whether ROCEv1 is supported by the device.  ***Since:*** vSphere API 7.0  | 
**roce_v2_capable** | **bool** | Indicates whether ROCEv2 is supported by the device.  ***Since:*** vSphere API 7.0  | 
**i_warp_capable** | **bool** | Indicates whether iWARP is supported by the device.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.host_rdma_device_capability import HostRdmaDeviceCapability

# TODO update the JSON string below
json = "{}"
# create an instance of HostRdmaDeviceCapability from a JSON string
host_rdma_device_capability_instance = HostRdmaDeviceCapability.from_json(json)
# print the JSON string representation of the object
print HostRdmaDeviceCapability.to_json()

# convert the object into a dict
host_rdma_device_capability_dict = host_rdma_device_capability_instance.to_dict()
# create an instance of HostRdmaDeviceCapability from a dict
host_rdma_device_capability_form_dict = host_rdma_device_capability.from_dict(host_rdma_device_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


