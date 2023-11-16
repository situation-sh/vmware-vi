# HostRdmaDeviceBacking

This data object represents the physical backing of an RDMA device.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_rdma_device_backing import HostRdmaDeviceBacking

# TODO update the JSON string below
json = "{}"
# create an instance of HostRdmaDeviceBacking from a JSON string
host_rdma_device_backing_instance = HostRdmaDeviceBacking.from_json(json)
# print the JSON string representation of the object
print HostRdmaDeviceBacking.to_json()

# convert the object into a dict
host_rdma_device_backing_dict = host_rdma_device_backing_instance.to_dict()
# create an instance of HostRdmaDeviceBacking from a dict
host_rdma_device_backing_form_dict = host_rdma_device_backing.from_dict(host_rdma_device_backing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


