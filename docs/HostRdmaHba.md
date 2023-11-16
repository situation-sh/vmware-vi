# HostRdmaHba

This data object describes the Remote Direct Memory Access (RDMA) host bus adapter interface.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_rdma_device** | **str** | Device name of the associated RDMA device, if any.  Should match the *HostRdmaDevice.device* property of the corresponding RDMA device.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_rdma_hba import HostRdmaHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostRdmaHba from a JSON string
host_rdma_hba_instance = HostRdmaHba.from_json(json)
# print the JSON string representation of the object
print HostRdmaHba.to_json()

# convert the object into a dict
host_rdma_hba_dict = host_rdma_hba_instance.to_dict()
# create an instance of HostRdmaHba from a dict
host_rdma_hba_form_dict = host_rdma_hba.from_dict(host_rdma_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


