# ArrayOfHostParallelScsiHba

A boxed array of *HostParallelScsiHba*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostParallelScsiHba]**](HostParallelScsiHba.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_parallel_scsi_hba import ArrayOfHostParallelScsiHba

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostParallelScsiHba from a JSON string
array_of_host_parallel_scsi_hba_instance = ArrayOfHostParallelScsiHba.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostParallelScsiHba.to_json()

# convert the object into a dict
array_of_host_parallel_scsi_hba_dict = array_of_host_parallel_scsi_hba_instance.to_dict()
# create an instance of ArrayOfHostParallelScsiHba from a dict
array_of_host_parallel_scsi_hba_form_dict = array_of_host_parallel_scsi_hba.from_dict(array_of_host_parallel_scsi_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


