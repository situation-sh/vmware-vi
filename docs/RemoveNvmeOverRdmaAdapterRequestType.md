# RemoveNvmeOverRdmaAdapterRequestType

The parameters of *HostStorageSystem.RemoveNvmeOverRdmaAdapter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hba_device_name** | **str** | The device name of the NVME over RDMA adapter to be removed.  | 

## Example

```python
from vmware_vi.models.remove_nvme_over_rdma_adapter_request_type import RemoveNvmeOverRdmaAdapterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveNvmeOverRdmaAdapterRequestType from a JSON string
remove_nvme_over_rdma_adapter_request_type_instance = RemoveNvmeOverRdmaAdapterRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveNvmeOverRdmaAdapterRequestType.to_json()

# convert the object into a dict
remove_nvme_over_rdma_adapter_request_type_dict = remove_nvme_over_rdma_adapter_request_type_instance.to_dict()
# create an instance of RemoveNvmeOverRdmaAdapterRequestType from a dict
remove_nvme_over_rdma_adapter_request_type_form_dict = remove_nvme_over_rdma_adapter_request_type.from_dict(remove_nvme_over_rdma_adapter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


