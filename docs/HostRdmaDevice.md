# HostRdmaDevice

This data object represents a Remote Direct Memory Access device as seen by the primary operating system.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The linkable identifier.  ***Since:*** vSphere API 7.0  | 
**device** | **str** | The device name of the RDMA device.  ***Since:*** vSphere API 7.0  | 
**driver** | **str** | The short string name of the device driver, if available.  ***Since:*** vSphere API 7.0  | [optional] 
**description** | **str** | Device description, if available.  ***Since:*** vSphere API 7.0  | [optional] 
**backing** | [**HostRdmaDeviceBacking**](HostRdmaDeviceBacking.md) |  | [optional] 
**connection_info** | [**HostRdmaDeviceConnectionInfo**](HostRdmaDeviceConnectionInfo.md) |  | 
**capability** | [**HostRdmaDeviceCapability**](HostRdmaDeviceCapability.md) |  | 

## Example

```python
from vmware_vi.models.host_rdma_device import HostRdmaDevice

# TODO update the JSON string below
json = "{}"
# create an instance of HostRdmaDevice from a JSON string
host_rdma_device_instance = HostRdmaDevice.from_json(json)
# print the JSON string representation of the object
print HostRdmaDevice.to_json()

# convert the object into a dict
host_rdma_device_dict = host_rdma_device_instance.to_dict()
# create an instance of HostRdmaDevice from a dict
host_rdma_device_form_dict = host_rdma_device.from_dict(host_rdma_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


