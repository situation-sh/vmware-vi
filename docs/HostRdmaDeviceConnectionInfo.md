# HostRdmaDeviceConnectionInfo

Represents connection information for the RDMA device.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | RDMA device connection state.  The set of possible values is described in *HostRdmaDeviceConnectionState_enum*.  ***Since:*** vSphere API 7.0  | 
**mtu** | **int** | Maximum Transmission Unit in bytes.  ***Since:*** vSphere API 7.0  | 
**speed_in_mbps** | **int** | Bit rate in Mbps.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.host_rdma_device_connection_info import HostRdmaDeviceConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostRdmaDeviceConnectionInfo from a JSON string
host_rdma_device_connection_info_instance = HostRdmaDeviceConnectionInfo.from_json(json)
# print the JSON string representation of the object
print HostRdmaDeviceConnectionInfo.to_json()

# convert the object into a dict
host_rdma_device_connection_info_dict = host_rdma_device_connection_info_instance.to_dict()
# create an instance of HostRdmaDeviceConnectionInfo from a dict
host_rdma_device_connection_info_form_dict = host_rdma_device_connection_info.from_dict(host_rdma_device_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


