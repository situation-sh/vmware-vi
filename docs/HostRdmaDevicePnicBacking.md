# HostRdmaDevicePnicBacking

This data object represents a physical NIC backing for an RDMA device.  When an RDMA device is backed by a physical NIC, it can be associated with the virtual NICs connected to a virtual switch which has the backing physical NIC as an uplink. The actual bindings are created and destroyed dynamically based on application usage of the RDMA device.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paired_uplink** | [**PhysicalNic**](PhysicalNic.md) |  | 

## Example

```python
from vmware_vi.models.host_rdma_device_pnic_backing import HostRdmaDevicePnicBacking

# TODO update the JSON string below
json = "{}"
# create an instance of HostRdmaDevicePnicBacking from a JSON string
host_rdma_device_pnic_backing_instance = HostRdmaDevicePnicBacking.from_json(json)
# print the JSON string representation of the object
print HostRdmaDevicePnicBacking.to_json()

# convert the object into a dict
host_rdma_device_pnic_backing_dict = host_rdma_device_pnic_backing_instance.to_dict()
# create an instance of HostRdmaDevicePnicBacking from a dict
host_rdma_device_pnic_backing_form_dict = host_rdma_device_pnic_backing.from_dict(host_rdma_device_pnic_backing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


