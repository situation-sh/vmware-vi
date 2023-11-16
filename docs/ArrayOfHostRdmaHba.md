# ArrayOfHostRdmaHba

A boxed array of *HostRdmaHba*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostRdmaHba]**](HostRdmaHba.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_rdma_hba import ArrayOfHostRdmaHba

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostRdmaHba from a JSON string
array_of_host_rdma_hba_instance = ArrayOfHostRdmaHba.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostRdmaHba.to_json()

# convert the object into a dict
array_of_host_rdma_hba_dict = array_of_host_rdma_hba_instance.to_dict()
# create an instance of ArrayOfHostRdmaHba from a dict
array_of_host_rdma_hba_form_dict = array_of_host_rdma_hba.from_dict(array_of_host_rdma_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


