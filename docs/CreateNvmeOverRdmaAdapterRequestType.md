# CreateNvmeOverRdmaAdapterRequestType

The parameters of *HostStorageSystem.CreateNvmeOverRdmaAdapter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rdma_device_name** | **str** | The device name of the RDMA device to be used to create the software adapter. Can be obtained from *HostRdmaDevice.device*.  | 

## Example

```python
from vmware_vi.models.create_nvme_over_rdma_adapter_request_type import CreateNvmeOverRdmaAdapterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNvmeOverRdmaAdapterRequestType from a JSON string
create_nvme_over_rdma_adapter_request_type_instance = CreateNvmeOverRdmaAdapterRequestType.from_json(json)
# print the JSON string representation of the object
print CreateNvmeOverRdmaAdapterRequestType.to_json()

# convert the object into a dict
create_nvme_over_rdma_adapter_request_type_dict = create_nvme_over_rdma_adapter_request_type_instance.to_dict()
# create an instance of CreateNvmeOverRdmaAdapterRequestType from a dict
create_nvme_over_rdma_adapter_request_type_form_dict = create_nvme_over_rdma_adapter_request_type.from_dict(create_nvme_over_rdma_adapter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


